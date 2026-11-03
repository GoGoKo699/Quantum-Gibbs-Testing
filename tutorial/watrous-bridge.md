# From Watrous to Quantum Gibbs Testing

[Learning route](README.md) · [30 milestones](milestones.md) · [Exact model](../science/model.md)

The selected educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. The section numbers below refer to the author's **2018 prepublication manuscript**, whose front matter is dated January 2018. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the April 2018 publication and links the [manuscript contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) and chapters. The manuscript is linked rather than reproduced here.

Watrous supplies states, measurements, distinguishability, channels, and relative entropy. This project supplies the thermal-family geometry and statistical constructions that connect those foundations to equality testing. Its primary research citations identify the inherited high-temperature theorem, covariance inequality, local estimators, and classical testing mechanisms. Those references support the proofs; the educational route uses one anchor.

## Targeted readings

Use these sections as focused lookups alongside the milestones. Reading the whole book is unnecessary for this project.

| Project use | Watrous manuscript sections | Connection to develop |
|---|---|---|
| Operators, Pauli strings, and norm conventions, M01–M04 | [1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), linear operators and operator decompositions/norms; [2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), quantum states of registers | A state is a positive trace-one operator; an interaction is a Hermitian operator, and its expectation is linear in the state. |
| Independent copies and Born probabilities, M01–M03 | [2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), measurements | One preparation is one input copy. A measured sign is a random variable, distinct from its exact expectation. |
| Convexity, probability, and statistical noise, M08–M09 | [1.2.1–1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), analysis/convexity and probability theory | Coefficient segments, expectation, and covariance support the project derivations. The U-statistic calculation is supplied in the project. |
| Operational distance and binary decisions, M07, M10, M28 | [3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), discriminating pairs of states | The Holevo–Helstrom theorem (Theorem 3.4) gives the optimal decision probability for two specified states; a composite testing problem additionally has unknown parameters. |
| Relative entropy and the thermal moment signal, M11, M15 | [5.1.1–5.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), classical entropy; [5.2.1–5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), quantum entropy and joint convexity | Quantum Pinsker (Theorem 5.38) converts relative entropy into a trace-norm bound after translating logarithms. |
| Arbitrary processing in the lower bound, M28 | [2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), quantum channels; [3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | A protocol, including its classical records and final decision, is a channel applied to its supplied copies. Processing cannot improve optimal discrimination of the inputs. |
| Entropy data processing, M11, M15 | [5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), Theorem 5.35 | Applying the same channel to both states cannot increase their relative entropy; this supports the standard measurement-based Pinsker argument. |

## Translate the conventions

| Anchor convention or object | Project convention or object | What matters |
|---|---|---|
| A quantum register with state in D(X) | An n-qubit density operator rho | The state space has dimension two to the n; the number M of interaction terms can be much smaller than that dimension. |
| An operator and its adjoint, written with a star | A Pauli string P and Hermitian matrix operations | Every menu string is phase free, Hermitian, traceless, and squares to the identity. The identity and duplicate coordinates are excluded. |
| Trace norm, Hilbert–Schmidt norm, operator norm | Trace norm for states; Euclidean norm for moment vectors; operator norm for covariance matrices | A norm on the M-component vector is different from a Schatten norm on the full quantum register. |
| Measurement outcome probabilities | Random score vectors X and Y | Scores are numerical functions of physical measurement records. They may be zero or have magnitude larger than one. |
| Base-two relative entropy | Natural-log relative entropy | Multiply the anchor's relative entropy by ln(2) before importing numerical constants. |
| Pair discrimination with equal priors | Equality versus a separated unknown pair | The project must succeed on every promised source pair, rather than on two supplied state descriptions. |

The project's separation is the **unhalved** trace norm. For classical probability distributions, total variation is half their L1 difference. With equal prior probabilities, the optimal success probability for distinguishing states rho and sigma is one half plus one quarter of their unhalved trace-norm difference. In the commuting construction this is one half plus one half of the classical total variation.

Watrous specifies base-two logarithms at the start of Section 5.1.1. If D_W denotes the anchor's quantum relative entropy and D the project's natural-log quantity, then

```math
D(\rho\Vert\sigma)=(\ln2)D_W(\rho\Vert\sigma),
\qquad
D(\rho\Vert\sigma)\ge\frac12\|\rho-\sigma\|_1^2.
```

The second formula is Theorem 5.38 in the project's convention. Its coefficient applies to the unhalved trace norm.

## From a Hamiltonian menu to a statistical family

A Pauli menu specifies which interactions can occur. Unknown coefficients select one Hamiltonian from that list, and normalization turns its matrix exponential into a state:

```math
H_h=\sum_{a=1}^M h_aP_a,
\qquad
\rho_h=\frac{e^{-\beta H_h}}{\mathrm{Tr}e^{-\beta H_h}}.
```

Both laboratories have unknown coefficients, bounded between minus one and one. They share the known menu and the same known inverse temperature beta. The menu's support-overlap graph joins terms that touch a common qubit. Its maximum degree is at most Delta, and the project writes d = Delta + 1. Intersecting supports and noncommuting operators are different notions: two Z interactions can overlap while commuting. The theorem controls overlap, which is enough for its local counting arguments.

For the single-spin menu Z, normalization gives the state and moment in the [learning introduction](README.md). When the coupling changes, the population bias changes. At small positive beta the change is weak, but predictable. At beta equal to zero all couplings give the same maximally mixed state. This explains both the need for positive beta and the lower bound's joint dependence on beta, separation, and family size.

A known menu is stronger than an unknown Hamiltonian being sparse. For example, a list of all possible two-qubit edges can have large overlap degree even when a realized Hamiltonian uses only a few edges. The supplied family, rather than the realized support alone, is part of the theorem.

## The missing geometry: global separation produces a local signal

Define the vector mu(h) of expectations of the menu terms. Estimating this vector is physically simple; connecting it to the global state requires the Gibbs promise.

The derivative of the log partition function is minus beta times mu. Its second derivative is a **Duhamel covariance**, obtained by differentiating a matrix exponential. In a commuting model it agrees with the familiar covariance of the interactions. For noncommuting terms it generally differs from ordinary variance. The [thermal geometry](../science/thermal-geometry.md) imports a uniform Hessian bound from Haah–Kothari–Tang in the explicit sufficient high-temperature window. Integrating that bound along the coefficient segment joins its local curvature information into a comparison valid for every pair in the cube.

The logarithm of a Gibbs state is its negative scaled Hamiltonian minus a scalar normalization. In the sum of the two relative entropies those scalar terms cancel. Combining this identity with curvature and Pinsker gives

```math
\|\rho_h-\rho_g\|_1^2
\le D(\rho_h\Vert\rho_g)+D(\rho_g\Vert\rho_h)
\le 2\|\mu(h)-\mu(g)\|_2^2.
```

Thus a global unhalved trace-norm gap epsilon forces a squared moment signal of at least epsilon squared divided by two. Exact equality produces zero signal. This is the direction needed by the tester. It supplies no constant-gap tolerant completeness theorem, and it assumes both states are in the family.

## The missing noise control: from a Born record to a mean test

Select one of X, Y, Z independently at each active qubit. For an interaction of weight w, its axes are all matched with probability three to the power minus w. Multiply the product of observed signs by three to the power w when they match, and use zero otherwise. The Born rule makes this score an unbiased estimator of that Pauli expectation.

Unbiasedness alone does not bound collective noise across M coordinates. The [covariance proof](../science/covariance-bound.md) first compares Duhamel and ordinary fluctuations using Harris's inequality and a bounded-overlap double commutator. It then controls the extra noise from the local measurement scores. The covariance operator is bounded by a constant depending on locality and overlap, uniformly in M.

Acquire independent score vectors from the two sources and subtract them. Use independent measurement axes between sources as well as between copies. Write the resulting differences as Z_i. Their mean is the desired moment difference. The statistic averages inner products between different preparations:

```math
T=\frac{1}{N(N-1)}\sum_{i\ne j}Z_i^{\mathsf T}Z_j.
```

Independence removes each preparation's self-noise in expectation. Under equality its variance is of order M divided by N squared. The far case has squared moment signal at least epsilon squared divided by two. Requiring the standard deviation to be smaller than this signal gives N of order square root M divided by epsilon squared. The [algorithm](../science/testing-algorithm.md) proves this with finite-sample constants, including the signal-dependent variance term. It also gives the threshold, confidence amplification, and streaming implementation. No Gaussian approximation or tomography step is required.

## The missing converse: a classical obstruction covers quantum protocols

The upper bound works for noncommuting sources. The lower bound can use a commuting subfamily because a uniformly valid tester must also succeed on that subfamily.

A greedy selection finds at least M/d menu strings with disjoint supports. Turning on only these couplings produces independent weakly biased signs in a known joint eigenbasis, with uniform extra degeneracy labels. A source's hidden sign vector is chosen once and kept fixed over every preparation. The alternative for S copies is consequently a mixture of repeated-copy states; replacing it by independent fresh signs on every copy would describe another experiment.

The [lower-bound proof](../science/collective-lower-bound.md) shows that every fixed alternative has the promised separation, then bounds the chi-square distinguishability of the repeated-copy mixture. A tester with adaptive source requests can be supplied with its entire capped allotment of first-source copies in advance. The second source is the known maximally mixed state under both hypotheses and can be supplied for free in this easier problem. All later operations are processing of the supplied copies.

Because the hard input states share a common eigenbasis, reading that basis already supplies their complete informative record. A collective quantum measurement is a processing of that record. Trace-norm contractivity, or the equivalent operational discrimination argument from Watrous, transfers the classical obstruction to arbitrary quantum memories, measurements, and adaptive decisions. The converse concerns a deterministic total-copy cap.

## Join the bounds and keep the resources distinct

The matched copy rate is of order square root M divided by epsilon squared in the explicit range stated on the [model page](../science/model.md). The upper bound's temperature window and the lower bound's separation range have different proof roles. The elementary product converse itself works at positive temperature outside the upper-bound window, while matching optimality needs both bounds.

For a linear-size menu and fixed locality/overlap, the copy count grows as square root n. Each copy still requires preparation, local readout, and classical processing. The stated implementation has O(M) working words and a readout/processing workload that can exceed linear order in n. Preparation time and imperfect or drifting sources are not supplied by the copy-access model.

Finally, equal bounded-weight moments need not imply equal arbitrary states: the parity example in [interpretation](../science/interpretation.md) makes this distinction concrete. Use the [Related work](../references/RELATED_WORK.md) for attribution and the precise operational comparisons. Use the [verification guide](../verification/README.md) to reproduce finite checks of the identities; those checks support the proof account without extending its domain.
