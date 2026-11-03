# Deterministic small-system validation

[Project overview](../README.md) · [Model](../science/model.md) · [Recorded output](results.json)

The analytic proofs establish the uniform result. This directory checks the identities on which those proofs depend, using complete finite outcome enumeration and dense matrix calculations. It does not use Monte Carlo sampling.

## Run

From the repository root, with Python 3, NumPy, and SciPy installed:

```bash
python verification/validate.py
```

The script exits with an error if an identity or inequality fails its numerical tolerance. A successful run writes [results.json](results.json), including the dependency versions, input menus and coefficients, numerical errors, signed minimum eigenvalues, and the SHA-256 hash of the validation script. To preserve the checked-in output while running locally, choose another destination:

```bash
python verification/validate.py --output /tmp/gibbs-validation.json
```

The recorded run used NumPy 2.3.5 and SciPy 1.17.0. All calculations use double-precision floating-point arithmetic. Complete enumeration means every basis and outcome is included; it does not mean exact rational arithmetic. Identity checks use a default tolerance of $2\times10^{-10}$ times the larger of one and the maximum absolute reference entry. Positive-semidefinite checks allow an absolute eigenvalue tolerance of $2\times10^{-10}$. The exhaustive U-statistic and sign-mixture comparisons use tolerances of $2\times10^{-9}$ and $2\times10^{-12}$, respectively, with the same reference scaling.

## Thermal geometry and Pauli measurement covariance

The two-, three-, and four-qubit examples contain noncommuting terms and both compatible and incompatible overlapping Pauli strings. The script enumerates all $3^n2^n=6^n$ measurement records, computes their Born probabilities, and compares the resulting vector moments with the analytic formulas.

| Calculation | Independent comparison or bound |
| --- | --- |
| Normalized Hessian of $\log Z$ | Spectral BKM covariance versus Fréchet derivatives of the matrix exponential |
| Ordinary thermal covariance | BKM lower bound and Harris upper bound with the $\beta/12$ double-commutator coefficient |
| Double commutator | Exhaustive nonzero triple pattern, the fixed-index count $2(\Delta+1)^2$, and the quadratic-form bound $8(\Delta+1)^2$ |
| Snapshot means and second moments | Complete Born-outcome sum versus the local Pauli formulas |
| Snapshot correction | Vanishing off the support-overlap graph and row bound $(\Delta+1)3^k$ |
| Full snapshot covariance | Positive semidefiniteness and the stated formula for $C_\beta$ on the selected examples |

The BKM calculation uses logarithmic means of Gibbs eigenvalues, evaluated with a stable $\sinh(x)/x$ formula. The independent curvature calculation differentiates in the coordinates $\theta=\beta h$ directly. Neither calculation estimates a tiny Hessian by finite differences and then divides it by $\beta^2$.

Each menu is evaluated at two temperatures:

- **Inside the proved regime:** $\beta$ is half the explicit sufficient threshold $[100e^6(\Delta+1)^8]^{-1}$. The script also checks that the normalized curvature eigenvalues lie between $1/2$ and $3/2$.
- **Moderate-temperature illustration:** $\beta=0.2$ makes the noncommuting effects numerically visible. These finite examples are outside the declared theorem promise. Their passing checks do not establish a larger uniform temperature range.

The distinction is recorded explicitly for every example in `results.json`. At the tiny proved temperatures, differences between ordinary and BKM covariance can be below floating-point resolution. Small negative minimum eigenvalues near machine precision are recorded rather than hidden; the spectral argument in [covariance-bound.md](../science/covariance-bound.md) establishes their exact positivity.

One deliberately included case is $XX$ paired with $YY$. The two operators commute globally, but their local axes conflict, so their two snapshot coordinates never contribute a nonzero product in one local Pauli record. At $\beta=0.2$ in the two-qubit example, the enumerated snapshot product expectation is exactly zero, while the thermal symmetrized product expectation is approximately $0.02134$. This checks the incompatible-overlap case that would be missed by treating global commutation as product-basis compatibility.

## U-statistic moments

For a two-qubit Gibbs model with two noncommuting observed terms, the script enumerates the distribution of $D=X-Y$ for both equal and different sources. It then enumerates every sequence of two or three independent paired snapshots and evaluates

$$
U=\frac{\left\|\sum_{t=1}^N D_t\right\|_2^2-\sum_{t=1}^N\|D_t\|_2^2}{N(N-1)}.
$$

The enumerated mean and variance are compared with

$$
\mathbb E U=\|\mu\|_2^2,\qquad
\operatorname{Var}(U)=\frac4N\mu^\mathsf T\Sigma\mu
+\frac{2}{N(N-1)}\operatorname{Tr}(\Sigma^2),
$$

where $\mu=\mathbb E D$ and $\Sigma=\operatorname{Cov}(D)$. This identity is valid for independent, identically distributed finite-variance vectors regardless of temperature. The illustrative $\beta=0.25$ used here is not a claim that the theorem's high-temperature promise extends to that value.

## Fixed-source sign mixture

For the commuting product alternatives in the [collective-measurement lower bound](../science/collective-lower-bound.md), the script holds each hidden sign vector fixed across all source copies before averaging over signs. It enumerates every transcript for three coordinates and one, two, or three copies, verifying normalization and

$$
1+\chi^2
=\left(\frac{(1+a^2)^N+(1-a^2)^N}{2}\right)^m.
$$

The illustrative bias $a=0.17$ makes the second moment visible in double precision. Feasibility of the lower-bound alternatives under the temperature and coefficient constraints is proved analytically in the lower-bound page; this algebraic check does not replace it.

## Scope

The checks can detect sign, normalization, commutator-counting, local-measurement, and finite-statistic errors. They do not prove dimension-independent estimates, minimax optimality, novelty, or practical sample sizes. In particular, the snapshot constant and the sufficient temperature threshold are conservative analytic guarantees, not constants fitted to these examples.
