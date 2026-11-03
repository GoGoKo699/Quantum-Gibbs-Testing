# Quantum Gibbs Testing

## Can two unknown thermal sources be compared with local measurements?

This repository gives an optimal copy-complexity theorem for comparing two unknown, potentially noncommuting Gibbs states. Both states share a **known menu of $`M`$ bounded-weight Pauli interactions with bounded support-overlap degree**, bounded coupling coefficients, and a common known sufficiently high temperature.

For exact equality versus an unhalved global trace-norm separation $`\varepsilon`$, independent single-qubit Pauli measurements attain

```math
\Theta\!\left(\frac{\sqrt M}{\varepsilon^2}\right)
```

total copies in the explicit matching regime below. An arbitrary collective quantum measurement cannot improve this worst-case order. The test compares interaction moments with a quadratic statistic; it does not reconstruct either Hamiltonian.

### Exact scope

Write $`\Delta`$ for the support-overlap degree bound, $`d=\Delta+1`$, and $`\beta`$ for inverse temperature. The sufficient temperature window is

```math
0\lt \beta\leq\frac{1}{100e^6d^8}.
```

The upper bound holds for the promised equality-versus-separation problem throughout this window. The matching lower bound applies when

```math
0\lt \varepsilon\leq
\min\left\{\frac1{16},\frac{\beta}{8}\sqrt{\frac M d}\right\}.
```

Constants depend on fixed interaction weight and overlap degree. The temperature condition is conservative. Both inputs must obey the same known-menu Gibbs promise; this is not certification against arbitrary nonthermal alternatives. The [precise model and theorem](science/model.md) state all quantifiers and resource conventions.

## Results and reading route

| Scientific question | Authoritative account |
|---|---|
| What is known, what is unknown, and what is proved? | [Model and main result](science/model.md) |
| Why can local moments control global thermal-state separation? | [Thermal geometry](science/thermal-geometry.md) |
| How is noncommuting measurement noise controlled? | [Covariance bound](science/covariance-bound.md) |
| What is the tester, and what does it cost? | [Testing algorithm](science/testing-algorithm.md) |
| Why can collective measurements do no better in the worst case? | [Collective lower bound](science/collective-lower-bound.md) |
| What does the theorem mean for source comparison? | [Interpretation and limits](science/interpretation.md) |
| Which ingredients are inherited, and how does this compare with earlier work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The proof connects uniform high-temperature log-partition curvature to a dimension-independent covariance bound for local Pauli scores. An unbiased quadratic statistic detects a squared moment displacement with variance of order $`M/N^2`$ under equality. A random-sign commuting subfamily supplies the converse against unrestricted quantum measurements. The existing curvature theorem, Harris inequality, Pauli estimator, quadratic statistic and product-testing mechanism are credited in their respective proof pages.

When $`M`$ is proportional to the qubit count $`n`$, the copy rate is order $`\sqrt n/\varepsilon^2`$. Full-register readout and processing still require order $`n^{3/2}/\varepsilon^2`$ elementary work for fixed locality and success probability. The copy-access model does not establish a physical thermalization-time bound.

## Learn the argument

The [learning guide](tutorial/README.md) starts with the source-comparison task and connects the proof mechanisms. The [Watrous bridge](tutorial/watrous-bridge.md) maps the selected 2018 source to this project, and the [30-milestone map](tutorial/milestones.md) gives a complete conceptual route from quantum states and measurements to the optimal testing law.

## Reproduce the finite checks

The [verification guide](verification/README.md) gives dependencies, commands, cases and expected output. Its deterministic examples check noncommuting thermal geometry, the local-Pauli measurement model and the statistical identities. They support the implementation and conventions; the linked analytical proofs establish the uniform and asymptotic results.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
