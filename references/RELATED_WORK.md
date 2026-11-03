# Related work and attribution

This comparison concerns the precise problem in [the model](../science/model.md): two unknown Gibbs states on the same **known bounded-degree Pauli menu**, a known sufficiently small positive inverse temperature, and exact equality versus a global trace-norm gap. [The upper bound](../science/testing-algorithm.md) and [the collective lower bound](../science/collective-lower-bound.md) match at $`\Theta_{k,\Delta}(\sqrt M/\varepsilon^2)`$ in the stated error range. Bibliographic metadata and relevant versions were checked on 3 November 2026; reusable entries are in [references.bib](references.bib).

## The closest quantum Gibbs testing result

Bluhm, Caro, Escudero Gutiérrez, Lee, Oufkir, Rouzé and Shin, [*Certifying and learning local quantum Hamiltonians*, arXiv:2603.29809v1, Theorem 17](https://arxiv.org/html/2603.29809v1), already give a Gibbs-state comparison test when **both states are unknown**. For arbitrary-degree $`k`$-local Hamiltonians with bounded Pauli coefficients, their theorem uses

```math
O\!\left(\frac{\beta^2n^{2k}3^k k\log(n/\delta)}{\eta^4}\right)
```

copies and Pauli measurements. In their unhalved trace norm, it distinguishes distance at most $`\eta^2/(400\beta n^k)`$ from distance at least $`2\eta`$, with error probability at most $`\delta`$. It applies at all temperatures and has polynomial classical processing time. Section 1.3 asks for optimal Gibbs certification complexity.

The present result addresses a restricted high-temperature, known-menu regime and supplies matching upper and lower copy bounds there. It does not resolve their broader all-temperature question. Their Lemma 4 also uses the Gibbs relative-entropy/moment identity underlying the geometry argument here; that identity is an inherited ingredient.

## Ingredients used in the proof

| Ingredient | Primary source and precise use here |
|---|---|
| High-temperature log-partition geometry | Haah, Kothari and Tang, [arXiv:2108.04842v3, Corollary 4.4](https://arxiv.org/pdf/2108.04842v3). We use its uniform Hessian control, including its explicit temperature restriction. The journal version is [*Learning quantum Hamiltonians from high-temperature Gibbs states and real-time evolutions*](https://doi.org/10.1038/s41567-023-02376-x), *Nature Physics* **20**, 1027–1031 (2024). |
| Ordinary variance versus Duhamel variance | Harris, *Bounds for Certain Thermodynamic Averages*, *Journal of Mathematical Physics* **8**, 1044–1045 (1967). The normalization used here is stated in Brankov and Tonchev, [Eq. (2.30)](https://icmp.lviv.ua/journal/zbirnyk.65/003/art03.pdf), *Condensed Matter Physics* **14**, 13003 (2011). |
| Independent local Pauli snapshots | Huang, Kueng and Preskill, [*Predicting many properties of a quantum system from very few measurements*](https://doi.org/10.1038/s41567-020-0932-7), *Nature Physics* **16**, 1050–1057 (2020). The unbiased Pauli estimators are standard classical-shadow estimators. |
| Quadratic mean comparison | Unbiased quadratic statistics for high-dimensional mean testing are established tools; see Chen and Qin, [*A two-sample test for high-dimensional data with applications to gene-set testing*](https://doi.org/10.1214/09-AOS716), *Annals of Statistics* **38**, 808–835 (2010). We derive the finite-sample variance of the paired-difference statistic directly. |
| Product lower-bound mechanism | Canonne, Diakonikolas, Kane and Stewart, [*Testing Bayesian Networks*, Theorem 9 and Section 2.2](https://proceedings.mlr.press/v65/canonne17a/canonne17a.pdf). Random signs and a likelihood-ratio second moment give the square-root product-uniformity obstruction. |
| Fourier norm comparison | Bonami, [*Étude des coefficients de Fourier des fonctions de Lᵖ(G)*](https://doi.org/10.5802/aif.357), *Annales de l'Institut Fourier* **20**(2), 335–402 (1970). The $`L^2`$-to-$`L^4`$ noise inequality and interpolation establish separation of each fixed alternative. |

The current HKT preprint is version 3, revised 15 March 2023; it reports a correction to Lemma 3.9. The cited corollary and constants are taken from that version. HKT's learning accuracy is coordinatewise Hamiltonian-coefficient accuracy, so its error parameter cannot be equated directly with a global state trace-norm threshold. The present proof uses its geometric theorem without reconstructing the Hamiltonian.

The Harris comparison in [the covariance proof](../science/covariance-bound.md), together with bounded-overlap commutator counting, bounds the ordinary thermal covariance. A sparse correction then bounds the full snapshot covariance. This argument requires neither an additional correlation-decay theorem nor a graph-volume summability assumption.

## Classical testing and the known-menu restriction

The $`\sqrt M/\varepsilon^2`$ dependence has classical antecedents. Daskalakis and Pan, [*Square Hellinger Subadditivity for Bayesian Networks and its Applications to Identity Testing*](https://proceedings.mlr.press/v65/daskalakis17a.html), give optimal $`O(\sqrt n/\varepsilon^2)`$ testing for a product distribution against a known product reference. Their graphical-model results compare structured distributions through local marginals. Noncommuting Gibbs states and their Pauli snapshot distributions do not acquire the bounded-indegree Bayesian factorization used in those results.

There is a relevant qualification for **two unknown** product distributions: Canonne et al., Theorems 31 and 40, establish the unrestricted rate

```math
\Theta\!\left(\max\left\{
\frac{\sqrt n}{\varepsilon^2},\frac{n^{3/4}}{\varepsilon}
\right\}\right)
```

for small errors. The extra term involves rare-marginal instances. The bounded-coefficient high-temperature product family here has marginals uniformly separated from zero and one, so this unrestricted lower bound does not conflict with the present theorem. We inherit the product-uniformity lower-bound mechanism, rather than claiming a new general product-distribution testing law.

Daskalakis, Dikkala and Kamath, [*Testing Ising Models*](https://doi.org/10.1109/TIT.2019.2932255), *IEEE Transactions on Information Theory* **65**, 6829–6852 (2019), study identity and independence testing for Ising models, including regimes with unknown interaction graphs. Their [primary preprint](https://arxiv.org/abs/1612.03147) uses symmetrized relative-entropy separation for several results. Its unknown-graph lower bounds cannot be transferred without preserving both the metric and the structural promise.

Here the menu itself is known and has bounded overlap, even when many coefficients vanish. Knowing only that each realized Hamiltonian is sparse is a weaker promise. For example, the union of all possible matchings contains all pair interactions and has growing overlap degree. The present theorem therefore does not assert optimal testing for arbitrary unknown sparse Ising graphs.

## Other recent thermal results and access models

Chen, Anshu and Nguyen, [*Learning quantum Gibbs states locally and efficiently*, arXiv:2504.02706v1](https://arxiv.org/abs/2504.02706), give efficient local Hamiltonian-learning results beyond the high-temperature regime, with temperature-dependent costs. Their objective is estimating Hamiltonian coefficients; it is different from the equality decision and global trace-norm promise considered here.

Chen and Gilyén, [*Efficiently estimating quantum thermal properties from exponentially fewer samples*, arXiv:2603.16845v2](https://arxiv.org/abs/2603.16845v2), estimate $`M`$ observables to precision $`\varepsilon`$ using $`O(\log M/\varepsilon^2)`$ Gibbs copies **given access to the Hamiltonian and controlled Hamiltonian simulation**. The September 2026 revision retains this access assumption. Those operations are not supplied by the unknown-copy-source model here, so that sample bound is not an alternative algorithm for this testing problem.

## The contribution established by these notes

The claim is the combined operational theorem: under the specified thermal and menu promises, global trace-norm equality testing of two unknown interacting quantum states has an optimal square-root dependence on the number of allowed interaction parameters. Independent single-qubit Pauli measurements and efficient classical processing attain the upper bound; allowing arbitrary collective processing does not improve the worst-case scaling in the matching regime.

The estimator, high-temperature Hessian theorem, Harris inequality, shadow measurement rule, Boolean hypercontractivity and classical random-sign lower-bound mechanism are credited above. The proof provides the moment-to-trace conversion in this regime, a uniform covariance bound for the actual measured data, and the complete menu-specific lower-bound embedding. It establishes neither arbitrary-state thermal certification nor a fixed nonzero completeness tolerance, and it makes no claim of optimality outside the lower bound's explicit error range.
