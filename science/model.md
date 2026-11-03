# Model and main result

Two laboratories supply independent preparations of unknown thermal states. The question is whether the sources prepare the same state, or states separated by a specified global trace norm. Their Hamiltonians need not commute. The interaction operators and temperature are known, while every coupling may be unknown in both laboratories.

This page states the promised model and the result. The proof proceeds through [thermal geometry](thermal-geometry.md), a [local-measurement covariance bound](covariance-bound.md), the [testing algorithm](testing-algorithm.md), and a [collective-measurement lower bound](collective-lower-bound.md). [Interpretation](interpretation.md) explains which physical conclusions the model supports.

## Known interaction menu and unknown sources

Fix $`n\geq 1`$ qubits and $`M\geq 1`$ distinct, nonidentity Pauli strings $`P_1,\ldots,P_M`$. A Pauli string is a phase-free tensor product of $`I,X,Y,Z`$; consequently these Hermitian operators are traceless, square to the identity, and are orthogonal in normalized Hilbert–Schmidt inner product. In particular, neither an identity coupling nor a duplicate signed coordinate is included.

Each string has weight at most $`k`$. The support-overlap graph has one vertex per string and an edge whenever two different strings act nontrivially on a common qubit. Write $`\Delta`$ for a bound on its maximum degree and $`d=\Delta+1`$. The theorem treats $`k`$ and $`\Delta`$ as fixed constants; its dependence on them is not suppressed when specifying an implementation.

For $`h\in[-1,1]^M`$, define

```math
H_h=\sum_{a=1}^{M}h_aP_a,
\qquad
Z_h=\mathrm{Tr}e^{-\beta H_h},
\qquad
\rho_h=Z_h^{-1}e^{-\beta H_h}.
```

Both sources obey this model, with unknown $`h,g\in[-1,1]^M`$ and the same known inverse temperature $`\beta>0`$. Distinct coefficients give distinct states: equality of their logarithms makes $`H_h-H_g`$ a multiple of the identity, and traceless Pauli orthogonality forces $`h=g`$.

The measurement device receives independently prepared copies from either source. Couplings, partition functions, purifications, coherent preparation inverses and Hamiltonian dynamics are not additional inputs. The upper bound uses independent single-qubit measurements and classical processing. The lower bound allows arbitrary joint quantum measurements, quantum memory and adaptive source choices, subject to a deterministic bound on the total number of input copies.

## Equality versus trace-norm separation

For a given $`0\lt \varepsilon\leq 2`$, decide between the promised cases

```math
\mathsf{EQUAL}:\quad \rho_h=\rho_g,
\qquad
\mathsf{FAR}:\quad \lVert\rho_h-\rho_g\rVert_1\geq\varepsilon.
```

The trace norm here is **unhalved**. Thus the convention often called trace distance is half the displayed norm. No guarantee is requested for unequal sources below the specified separation. Success probability is at least $`2/3`$ in each promised case. The total copy count includes copies of both sources.

The supplied value of $`\Delta`$ may be an upper bound. The sufficient uniform temperature condition is

```math
0\lt \beta\leq\beta_*:=\frac{1}{100e^6d^8}.
```

This is the conservative high-temperature condition imported from the current Haah–Kothari–Tang analysis; it is not claimed to locate an optimal physical boundary. [Thermal geometry](thermal-geometry.md) gives the exact imported statement and the separate elementary treatment of disjoint interactions.

## Theorem: optimal copy complexity with local readout

**Upper bound.** For every known menu satisfying the stated assumptions and every promised pair at $`0\lt \beta\leq\beta_*`$, a test using independent random single-qubit Pauli measurements succeeds with probability at least $`2/3`$ using

```math
O_{k,\Delta}\!\left(\frac{\sqrt M}{\varepsilon^2}\right)
```

total copies. An explicit conservative implementation uses

```math
C_0=2+d3^k,
\qquad
N=\max\left\{2,\left\lceil
\frac{512C_0\lceil\sqrt M\rceil}{\varepsilon^2}
\right\rceil\right\},
```

with $`N`$ copies of each source, for $`2N`$ copies in all. The statistic can be accumulated exactly from integer Pauli scores, using a vector sum and one scalar sum of squared scores. The constant is sufficient for the proof and is not optimized.

**Lower bound.** For every such fixed known menu, if

```math
0\lt \varepsilon\leq
\min\left\{\frac1{16},\frac{\beta}{8}(M/d)^{1/2}\right\},
```

any test that succeeds uniformly with probability at least $`2/3`$ needs

```math
\Omega_{\Delta}\!\left(\frac{\sqrt M}{\varepsilon^2}\right)
```

total copies, even when arbitrary collective quantum measurements are permitted. More explicitly, the proof excludes a total budget at most $`\sqrt L/(64\varepsilon^2)`$ for a support-disjoint subfamily of size $`L\geq M/d`$.

Hence the minimax copy complexity in this explicit nonvacuous gap range is

```math
\boxed{\displaystyle
\Theta_{k,\Delta}\!\left(\frac{\sqrt M}{\varepsilon^2}\right).}
```

For any fixed admissible positive $`\beta`$, the lower-bound range includes fixed $`\varepsilon\leq1/16`$ when $`M`$ is large enough. The theorem does not assert a matching lower bound for every separation at every finite $`M`$. When $`M=\Theta(n)`$, the copy rate becomes $`\Theta(\sqrt n/\varepsilon^2)`$.

## Why the rate is possible

Let $`\mu(h)_a=\mathrm{Tr}(\rho_hP_a)`$. Uniform curvature of the log partition function and symmetric relative entropy imply

```math
\lVert\rho_h-\rho_g\rVert_1^2
\leq 2\lVert\mu(h)-\mu(g)\rVert_2^2.
```

Local measurements provide an unbiased vector of estimates of these moments. Its covariance operator has a dimension-independent bound. This combination permits an unbiased estimate of the **squared difference of the mean vectors**; estimating every coupling accurately is unnecessary for the promised decision problem. The resulting quadratic statistic has null variance proportional to $`M/N^2`$, which gives the $`\sqrt M`$ copy rate.

For the converse, a bounded-degree graph always contains a large support-disjoint set of strings. Restricting the Hamiltonian to that set embeds independent, weakly biased classical bits. Their random-sign mixture is difficult to distinguish from the maximally mixed state until the same copy scale. Every state in this subfamily is diagonal in one fixed joint basis, so an arbitrary quantum measurement cannot extract more information than its full classical basis record.

## Resource and scope summary

| Resource or promise | Precise meaning |
|---|---|
| Preparations | $`2N`$ independent full-register state copies for the explicit one-run test. |
| Measurement | Separate single-qubit Pauli bases; no entangling detector or quantum memory across copies. |
| Readout | At most $`O(nN)`$ one-qubit measurements; qubits absent from every interaction can be ignored. |
| Classical work | $`O(kMN+nN)`$ elementary acquisition and processing operations for full-register readout; fixed-locality processing is $`O(MN)`$. |
| Storage | $`O(M)`$ working words for fixed locality, plus the known menu and the current-shot acquisition representation; bit lengths grow logarithmically with the sample count. |
| Temperature | One explicit sufficient high-temperature window, common to both sources. |
| Source promise | Both states belong to the same known-menu Gibbs family with bounded coefficients. |
| Separation | Exact equality against a global unhalved trace-norm gap; no fixed-gap tolerant completeness claim. |

The rate concerns copies. It does not provide a preparation-time theorem, an end-to-end physical speedup, or verification against arbitrary departures from the Gibbs promise. The [algorithm](testing-algorithm.md) accounts for implementation costs, and [interpretation](interpretation.md) gives an explicit failure mode outside the promise.

The imported results and precise comparison with prior Gibbs and classical distribution testers are documented in [Related work](../references/RELATED_WORK.md). The finite [verification suite](../verification/README.md) tests the identities and measurement conventions on specified examples; analytical proofs establish the universal statements.
