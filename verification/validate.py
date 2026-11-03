#!/usr/bin/env python3
"""Deterministic finite-dimensional checks for Quantum Gibbs Testing.

All Born outcomes are enumerated for the small systems below. Computation uses
floating-point arithmetic: "enumeration" does not mean exact rational arithmetic.
The checks do not establish a temperature threshold or the asymptotic theorem.

Run from the repository root:
    python verification/validate.py
Optional:
    python verification/validate.py --output /tmp/gibbs-results.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm, expm_frechet
from scipy.special import logsumexp

I = np.eye(2, dtype=complex)
PAULI = {
    "I": I,
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def kron_all(factors):
    out = np.array([[1]], dtype=complex)
    for factor in factors:
        out = np.kron(out, factor)
    return out


def pauli_word(word):
    return kron_all(PAULI[letter] for letter in word)


def comm(a, b):
    return a @ b - b @ a


def real(value):
    if abs(np.imag(value)) > 1e-9:
        raise AssertionError(f"Unexpected imaginary part: {value}")
    return float(np.real(value))


def assert_close(actual, expected, *, atol=2e-10, name="identity"):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    scale = max(1.0, float(np.max(np.abs(expected))))
    if error > atol * scale:
        raise AssertionError(f"{name}: error {error} exceeds {atol * scale}")
    return error


def assert_psd(matrix, *, atol=2e-10, name="positive semidefinite"):
    minimum = float(np.linalg.eigvalsh((matrix + matrix.T) / 2)[0])
    if minimum < -atol:
        raise AssertionError(f"{name}: minimum eigenvalue {minimum}")
    return minimum


def graph_data(words):
    supports = [{j for j, p in enumerate(word) if p != "I"} for word in words]
    overlap = np.array(
        [[bool(a & b) for b in supports] for a in supports], dtype=bool
    )
    # All menu strings are nonidentity, so the diagonal is True.
    degree = int(np.max(np.sum(overlap, axis=1))) - 1
    return supports, overlap, degree


def gibbs(words, coefficients, beta):
    ops = [pauli_word(word) for word in words]
    hamiltonian = sum(h * p for h, p in zip(coefficients, ops))
    energies, vectors = np.linalg.eigh(hamiltonian)
    log_probabilities = -beta * energies
    log_probabilities -= logsumexp(log_probabilities)
    probabilities = np.exp(log_probabilities)
    rho = (vectors * probabilities) @ vectors.conj().T
    return rho, hamiltonian, ops, energies, vectors, probabilities, log_probabilities


def sinhc(x):
    """sinh(x)/x, stable in the tiny-beta regime and at degeneracies."""
    x = np.asarray(x, dtype=float)
    small = np.abs(x) < 1e-4
    out = np.empty_like(x)
    y = x[small] ** 2
    out[small] = 1 + y / 6 + y * y / 120 + y * y * y / 5040
    out[~small] = np.sinh(x[~small]) / x[~small]
    return out


def thermal_matrices(data, beta):
    rho, hamiltonian, ops, _, vectors, _, log_probabilities = data
    m = np.array([real(np.trace(rho @ p)) for p in ops])
    centered = [p - v * np.eye(len(rho)) for p, v in zip(ops, m)]
    eigenbasis_ops = [vectors.conj().T @ a @ vectors for a in centered]
    lp = log_probabilities
    # The logarithmic mean is evaluated directly, without subtracting nearly
    # equal probabilities or dividing a numerically differenced Hessian by beta^2.
    weights = np.exp((lp[:, None] + lp[None, :]) / 2) * sinhc(
        (lp[:, None] - lp[None, :]) / 2
    )
    bkm = np.array([
        [real(np.sum(weights * a * b.T)) for b in eigenbasis_ops]
        for a in eigenbasis_ops
    ])
    thermal = np.array([
        [real(np.trace(rho @ (a @ b + b @ a) / 2)) for b in centered]
        for a in centered
    ])
    nested = np.array([
        [real(np.trace(rho @ (comm(a, comm(hamiltonian, b))
                              + comm(b, comm(hamiltonian, a))) / 2))
         for b in ops]
        for a in ops
    ])
    # Independent computation of curvature in theta=beta*h coordinates.
    # d <P_i> / d theta_j = - BKM_ij. Frechet derivatives avoid a
    # finite-difference step, including at tiny beta.
    exponent = -beta * hamiltonian
    exponential = expm(exponent)
    partition = real(np.trace(exponential))
    curvature = np.empty((len(ops), len(ops)))
    for j, p in enumerate(ops):
        derivative = expm_frechet(exponent, -p, compute_expm=False)
        derivative_rho = (
            derivative - rho * real(np.trace(derivative))
        ) / partition
        for i, q in enumerate(ops):
            curvature[i, j] = -real(np.trace(derivative_rho @ q))
    return m, bkm, thermal, nested, curvature


def enumerate_snapshots(words, rho):
    n = len(words[0])
    weights = [sum(p != "I" for p in word) for word in words]
    probabilities, features = [], []
    for axes in itertools.product("XYZ", repeat=n):
        for signs in itertools.product((-1, 1), repeat=n):
            projector = kron_all(
                (I + sign * PAULI[axis]) / 2
                for axis, sign in zip(axes, signs)
            )
            probability = real(np.trace(rho @ projector)) / (3 ** n)
            if probability < -1e-12:
                raise AssertionError("Negative Born probability")
            probability = max(0.0, probability)
            row = []
            for word, weight in zip(words, weights):
                support = [j for j, p in enumerate(word) if p != "I"]
                compatible = all(axes[j] == word[j] for j in support)
                row.append(
                    3 ** weight * math.prod(signs[j] for j in support)
                    if compatible else 0
                )
            probabilities.append(probability)
            features.append(row)
    probabilities = np.array(probabilities)
    features = np.array(features, dtype=float)
    mean = probabilities @ features
    second = features.T @ (probabilities[:, None] * features)
    covariance = second - np.outer(mean, mean)
    return probabilities, features, mean, second, covariance


def analytic_snapshot_second(words, rho, ops):
    out = np.zeros((len(words), len(words)))
    for i, left in enumerate(words):
        for j, right in enumerate(words):
            incompatible = any(
                a != "I" and b != "I" and a != b
                for a, b in zip(left, right)
            )
            if incompatible:
                out[i, j] = 0.0
            else:
                shared = sum(
                    a != "I" and b != "I"
                    for a, b in zip(left, right)
                )
                out[i, j] = 3 ** shared * real(np.trace(rho @ ops[i] @ ops[j]))
    return out


def geometry_case(words, beta, label):
    m_count = len(words)
    coefficients = np.array([0.74 * math.sin(i + 0.4) for i in range(m_count)])
    data = gibbs(words, coefficients, beta)
    rho, hamiltonian, ops, *_ = data
    mean, bkm, thermal, nested, curvature = thermal_matrices(data, beta)
    probability, features, sample_mean, second, covariance = enumerate_snapshots(words, rho)
    _, overlap, delta = graph_data(words)
    d = delta + 1
    k = max(sum(p != "I" for p in word) for word in words)
    c_beta = 1.5 + (2 / 3) * beta * d * d + d * 3 ** k
    sufficient_threshold = 1 / (100 * math.exp(6) * d ** 8)
    correction = covariance - thermal

    # Check the actual nonzero triple pattern against both counting bounds.
    counts_j = np.zeros(m_count, dtype=int)
    counts_i = np.zeros(m_count, dtype=int)
    actual_nonzero_triples = 0
    for i, j, ell in itertools.product(range(m_count), repeat=3):
        allowed = overlap[ell, j] and (overlap[i, ell] or overlap[i, j])
        value = comm(ops[i], comm(ops[ell], ops[j]))
        nonzero = np.linalg.norm(value, ord=2) > 1e-10
        if nonzero and not allowed:
            raise AssertionError("A nonzero nested commutator escaped locality")
        if allowed:
            counts_j[j] += 1
            counts_i[i] += 1
        actual_nonzero_triples += int(nonzero)
    if max(np.max(counts_i), np.max(counts_j)) > 2 * d * d:
        raise AssertionError("Triple-count bound failed")

    errors = {
        "born_probability_sum": assert_close(probability.sum(), 1.0),
        "snapshot_mean": assert_close(sample_mean, mean),
        "snapshot_second_moment": assert_close(
            second, analytic_snapshot_second(words, rho, ops)
        ),
        "bkm_vs_frechet_curvature": assert_close(bkm, curvature),
        "disjoint_covariance_correction": assert_close(
            correction[~overlap], np.zeros(np.count_nonzero(~overlap))
        ) if np.any(~overlap) else 0.0,
    }
    minima = {
        "bkm": assert_psd(bkm, name="BKM"),
        "ordinary_minus_bkm": assert_psd(thermal - bkm, name="ordinary >= BKM"),
        "harris_slack": assert_psd(
            bkm + beta * nested / 12 - thermal, name="Harris inequality"
        ),
        "nested_commutator": assert_psd(nested, name="double commutator"),
        "snapshot_covariance": assert_psd(covariance, name="snapshot covariance"),
        "nested_operator_bound_slack": assert_psd(
            8 * d * d * np.eye(m_count) - nested, name="locality bound"
        ),
        "covariance_bound_formula_slack": assert_psd(
            c_beta * np.eye(m_count) - covariance, name="snapshot bound"
        ),
    }
    row_bound = float(np.max(np.sum(np.abs(correction), axis=1)))
    if row_bound > d * 3 ** k + 1e-10:
        raise AssertionError("Snapshot correction row bound failed")
    bkm_eigenvalues = np.linalg.eigvalsh(bkm)
    in_proved_regime = beta <= sufficient_threshold
    if (label == "proved_temperature_example") != in_proved_regime:
        raise AssertionError("Temperature-regime label disagrees with the explicit threshold")
    if in_proved_regime:
        assert_psd(bkm - 0.5 * np.eye(m_count), name="HKT lower bound")
        assert_psd(1.5 * np.eye(m_count) - bkm, name="HKT upper bound")
    # This pair commutes as whole operators but has incompatible local axes.
    incompatible_pair = next(
        (i, j) for i in range(m_count) for j in range(i)
        if any(a != "I" and b != "I" and a != b
               for a, b in zip(words[i], words[j]))
        and np.linalg.norm(comm(ops[i], ops[j])) < 1e-10
    )
    i, j = incompatible_pair
    return {
        "qubits": len(words[0]),
        "menu": words,
        "coefficients": coefficients.tolist(),
        "beta": beta,
        "interpretation": label,
        "outcomes_enumerated": len(probability),
        "maximum_overlap_degree": delta,
        "normalized_curvature_eigenvalue_range": [
            float(bkm_eigenvalues[0]), float(bkm_eigenvalues[-1])
        ],
        "maximum_identity_errors": errors,
        "minimum_eigenvalues": minima,
        "snapshot_covariance_operator_norm": float(np.linalg.eigvalsh(covariance)[-1]),
        "covariance_bound_formula_C_beta": c_beta,
        "sufficient_temperature_threshold": sufficient_threshold,
        "within_proved_temperature_regime": in_proved_regime,
        "snapshot_correction_maximum_absolute_row_sum": row_bound,
        "snapshot_correction_row_bound": d * 3 ** k,
        "nested_nonzero_triples": actual_nonzero_triples,
        "maximum_admissible_triples_at_fixed_i_or_j": int(
            max(np.max(counts_i), np.max(counts_j))
        ),
        "triple_count_bound": 2 * d * d,
        "incompatible_but_commuting_pair": {
            "words": [words[i], words[j]],
            "snapshot_product_expectation": float(second[i, j]),
            "thermal_symmetrized_product_expectation": real(
                np.trace(rho @ (ops[i] @ ops[j] + ops[j] @ ops[i]) / 2)
            ),
        },
        "limitations": (
            "A finite example inside the explicit sufficient temperature regime."
            if in_proved_regime else
            "Illustrative moderate-temperature check only; no enlarged "
            "temperature theorem is inferred."
        ),
    }


def aggregate_difference(p, x, q, y):
    mass = {}
    for i, j in itertools.product(range(len(p)), range(len(q))):
        value = tuple(int(z) for z in x[i] - y[j])
        mass[value] = mass.get(value, 0.0) + float(p[i] * q[j])
    values = np.array(list(mass), dtype=float)
    probabilities = np.array(list(mass.values()))
    keep = probabilities > 0
    probabilities, values = probabilities[keep], values[keep]
    assert_close(probabilities.sum(), 1)
    return probabilities, values


def u_statistic_case(equal):
    # Two noncommuting local features on a two-qubit state. The second qubit
    # is a spectator, allowing complete enumeration of three paired snapshots.
    words = ["XI", "ZI"]
    beta = 0.25
    h = [0.6, -0.4]
    g = h if equal else [-0.3, 0.7]
    rho_h = gibbs(words, h, beta)[0]
    rho_g = gibbs(words, g, beta)[0]
    p, x, *_ = enumerate_snapshots(words, rho_h)
    q, y, *_ = enumerate_snapshots(words, rho_g)
    mass, values = aggregate_difference(p, x, q, y)
    mu = mass @ values
    sigma = values.T @ (mass[:, None] * values) - np.outer(mu, mu)
    results = []
    for count in (2, 3):
        u_mean = 0.0
        u_second = 0.0
        for indices in itertools.product(range(len(mass)), repeat=count):
            probability = math.prod(mass[i] for i in indices)
            vectors = values[list(indices)]
            total = np.sum(vectors, axis=0)
            value = (
                float(total @ total) - float(np.sum(vectors * vectors))
            ) / (count * (count - 1))
            u_mean += probability * value
            u_second += probability * value * value
        variance = u_second - u_mean * u_mean
        predicted = (
            4 / count * float(mu @ sigma @ mu)
            + 2 / (count * (count - 1)) * float(np.trace(sigma @ sigma))
        )
        results.append({
            "paired_snapshots": count,
            "joint_outcomes_enumerated": len(mass) ** count,
            "mean": u_mean,
            "mean_identity_error": assert_close(u_mean, mu @ mu, atol=2e-9),
            "variance": variance,
            "variance_from_formula": predicted,
            "variance_identity_error": assert_close(variance, predicted, atol=2e-9),
        })
    return {
        "hypothesis": "equal" if equal else "different",
        "qubits": 2,
        "menu": words,
        "beta": beta,
        "difference_vector_support_size": len(mass),
        "interpretation": "Finite statistical identity; moderate beta is illustrative.",
        "cases": results,
    }


def sign_mixture_case():
    # Commuting product alternatives: s is held fixed across all source copies,
    # and averaged only after forming the complete fixed-source transcript law.
    coordinates = 3
    bias = 0.17
    signs = np.array(list(itertools.product((-1, 1), repeat=coordinates)))
    cases = []
    for copies in (1, 2, 3):
        likelihood_ratios = []
        for bits in itertools.product((-1, 1), repeat=coordinates * copies):
            transcript = np.array(bits).reshape(copies, coordinates)
            ratios = [
                float(np.prod(1 + bias * transcript * sign[None, :]))
                for sign in signs
            ]
            likelihood_ratios.append(sum(ratios) / len(ratios))
        likelihood_ratios = np.array(likelihood_ratios)
        chi_square = float(np.mean((likelihood_ratios - 1) ** 2))
        formula = (
            ((1 + bias ** 2) ** copies + (1 - bias ** 2) ** copies) / 2
        ) ** coordinates - 1
        cases.append({
            "copies": copies,
            "transcripts_enumerated": len(likelihood_ratios),
            "likelihood_normalization_error": assert_close(
                np.mean(likelihood_ratios), 1
            ),
            "chi_square": chi_square,
            "chi_square_formula": formula,
            "identity_error": assert_close(chi_square, formula, atol=2e-12),
        })
    return {
        "coordinates": coordinates,
        "bias": bias,
        "signs_are_fixed_across_copies": True,
        "interpretation": (
            "Algebraic sign-mixture identity. The moderate bias makes the "
            "identity numerically visible; theorem feasibility at the declared "
            "temperature is established analytically in the lower-bound proof."
        ),
        "cases": cases,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().with_name("results.json")
    )
    args = parser.parse_args()
    menus = [
        ["XI", "ZI", "IX", "IZ", "XX", "YY"],
        ["XII", "ZII", "IXI", "IIZ", "XXI", "YYI", "IZZ", "ZIZ"],
        ["XIII", "ZIII", "IXII", "IIZI", "IIIX",
         "XXII", "YYII", "IZZI", "IIZZ", "ZIIZ"],
    ]
    geometry = []
    for menu in menus:
        delta = graph_data(menu)[2]
        beta_hkt = 1 / (100 * math.exp(6) * (delta + 1) ** 8)
        geometry.append(geometry_case(
            menu, beta_hkt / 2, "proved_temperature_example"
        ))
        geometry.append(geometry_case(
            menu, 0.2, "moderate_temperature_illustration"
        ))
    result = {
        "status": "passed",
        "arithmetic": "IEEE double-precision floating point",
        "method": "Deterministic enumeration and dense linear algebra; no Monte Carlo.",
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__},
        "source_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "scope": (
            "Finite-dimensional checks of load-bearing identities and selected "
            "inequalities, not a proof of asymptotic optimality or a numerical "
            "extension of the stated temperature range."
        ),
        "geometry_and_snapshot_cases": geometry,
        "u_statistic_cases": [u_statistic_case(True), u_statistic_case(False)],
        "sign_mixture": sign_mixture_case(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(f"All deterministic checks passed. Results: {args.output}")
    print(
        "Scope: 2–4 qubit geometry and Pauli readout; finite U-statistic moments; "
        "fixed-source sign-mixture identity."
    )


if __name__ == "__main__":
    main()
