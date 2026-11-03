# Watrous bridge: from quantum states to thermal comparison

[Thirty-milestone map](MILESTONES.md) · [Project overview](../README.md) · [Model and theorem](../science/model.md)

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018** ([publisher record](https://doi.org/10.1017/9781316848142)). Section and theorem numbers on this page refer to the [author's prepublication manuscript][W], available for personal reading. The published book and that manuscript are distinguished in the [bibliography](../references/references.bib).

This bridge supports the settled map of **12 background milestones and 18 narrative milestones**. It supplies a compact reading route, fixes conventions, and works through one complete example. The [map](MILESTONES.md) gives the individual understanding targets; the science pages contain the full proofs.

## 1. The foundation supplied by Watrous

| Connection in the milestone map | Anchor reading | Role in this project |
|---|---|---|
| [M01–M02: states and Pauli coordinates](MILESTONES.md#m01-states-observables-and-outcome-probabilities), and [M05: copy access](MILESTONES.md#m05-copy-sources-and-measurement-access) | Sections 1.1.3 and 2.1–2.3 | Matrix norms, composite states, channels and measurements make the input resources and recorded probabilities precise. |
| [M06: operational distance](MILESTONES.md#m06-trace-norm-as-distinguishability) | Section 3.1.1, especially Theorem 3.4 | Binary discrimination explains the meaning of a global state-distance promise and later bounds all final decisions in the converse. |
| [M07: relative entropy](MILESTONES.md#m07-relative-entropy-and-data-processing) | Section 5.2, especially 5.2.3 and Theorem 5.38 | Data processing and Pinsker connect an entropy comparison to global trace separation. |
| [M08–M09: fluctuations and response](MILESTONES.md#m08-covariance-and-directions-of-fluctuation) | Sections 1.1.3 and 1.2 | Norm, probability and convexity foundations support the covariance and thermal-response calculations developed in the project. |

The Gibbs family, high-temperature estimates and finite-sample testing machinery enter through the research sources identified in Section 4 below. In particular, the book's discrimination theorem concerns specified hypotheses; it does not by itself construct an equality tester for two unknown members of a thermal family.

## 2. Conventions and their translations

### Trace norm and the alternative half-trace convention

Define

```math
q(\rho,\sigma)=\|\rho-\sigma\|_1,
\qquad
d_{\mathrm{tr}}(\rho,\sigma)=\frac12q(\rho,\sigma).
```

Watrous calls **the unhalved quantity** $`q`$ the trace distance in Section 1.1.3, following Eq. (1.181). The project's theorem uses that same quantity. The symbol $`d_{\mathrm{tr}}`$ above represents the other common convention, whose range is $`[0,1]`$. Thus the project's alternative $`q\ge\varepsilon`$ is equivalent to $`d_{\mathrm{tr}}\ge\varepsilon/2`$.

Theorem 3.4 gives the optimal success probability for distinguishing a specified pair of states with equal priors:

```math
p_{\mathrm{succ}}^{\mathrm{opt}}
=\frac12+\frac14q
=\frac{1+d_{\mathrm{tr}}}{2}.
```

The optimal measurement may depend on the specified states. The testing algorithm instead works uniformly when both states are unknown and only their family is given. This distinction connects [M06](MILESTONES.md#m06-trace-norm-as-distinguishability) to [M12](MILESTONES.md#m12-synthesis-of-the-promised-comparison-problem).

### Base-two entropy and natural logarithms

Watrous uses $`\log`$ for base-two logarithms and $`\ln`$ for natural logarithms; Section 5.1.1 states the convention explicitly. Write

```math
\begin{aligned}
D_2(\rho\|\sigma)
&=\mathrm{Tr}\rho(\log_2\rho-\log_2\sigma),\\
D_{\ln}(\rho\|\sigma)
&=\mathrm{Tr}\rho(\ln\rho-\ln\sigma)
=(\ln2)D_2(\rho\|\sigma).
\end{aligned}
```

Theorem 5.38 therefore translates as

```math
D_2(\rho\|\sigma)\ge\frac{q^2}{2\ln2}
\quad\Longrightarrow\quad
D_{\ln}(\rho\|\sigma)\ge\frac{q^2}{2}
=2d_{\mathrm{tr}}^2.
```

Applying the inequality in both orders gives

```math
D_{\ln}(\rho\|\sigma)+D_{\ln}(\sigma\|\rho)
\ge q^2=4d_{\mathrm{tr}}^2.
```

These are the constants used in [the thermal geometry proof](../science/thermal-geometry.md#relative-entropy-converts-moments-to-global-trace-norm). Its log partition function is $`L(h)=\ln Z_h`$. If a base-two function $`L_2(h)=\log_2Z_h`$ is used instead, then $`L_2=L/\ln2`$, and both its gradient and its Hessian are divided by $`\ln2`$. The imported curvature constants must be converted accordingly.

Two further notation points prevent ambiguity. Watrous's matrix operator norm $`\Vert A\Vert _\infty`$ is written $`\Vert A\Vert _{\mathrm{op}}`$ in the project. His measurement notation $`\mu(s)`$ denotes an effect operator; the project's $`\mu(h)`$ instead denotes the real vector of Pauli expectation values. A measurement can be written as effects $`E_s`$ with probabilities $`\mathrm{Tr}(\rho E_s)`$ to keep these roles distinct.

## 3. A complete one-qubit example

This example connects [M12](MILESTONES.md#m12-synthesis-of-the-promised-comparison-problem), [M18](MILESTONES.md#m18-simultaneous-pauli-score-construction), and [M20–M23](MILESTONES.md#m20-independent-pairs-and-the-unbiased-statistic).

### The family and its state separation

Take one qubit and the known menu $`\{Z\}`$. Thus $`n=M=k=d=1`$ and $`\Delta=0`$. Fix any inverse temperature in the theorem's range,

```math
0<\beta\le\frac1{100e^6}.
```

For the example pair, let

```math
H_A=-\frac1{16}Z,\qquad H_B=0,
\qquad r=\tanh(\beta/16),\qquad\varepsilon=r.
```

Both coefficients lie in $`[-1,1]`$. Expanding the exponential using $`Z^2=I`$ gives

```math
\rho_A=
\frac{e^{\beta Z/16}}{2\cosh(\beta/16)}
=\frac{I+rZ}{2},
\qquad
\rho_B=\tau=\frac I2.
```

The eigenvalues of $`\rho_A-\tau`$ are $`r/2`$ and $`-r/2`$, so

```math
\|\rho_A-\tau\|_1=r=\varepsilon,
\qquad d_{\mathrm{tr}}(\rho_A,\tau)=r/2,
\qquad
\mathrm{Tr}(\rho_AZ)-\mathrm{Tr}(\tau Z)=r.
```

This pair satisfies the alternative promise. It also lies in the matching lower-bound range because $`r<\beta/16<\beta/8`$ and $`r<1/16`$. The specified coefficients allow the example to be calculated exactly; the protocol itself receives independent copies, the menu, $`\beta`$ and $`\varepsilon`$.

### From measurement outcomes to unbiased scores

For each copy, choose an axis uniformly from $`\{X,Y,Z\}`$ and record the outcome sign $`s\in\{-1,+1\}`$. Give the copy score $`3s`$ if the chosen axis is $`Z`$, and score zero otherwise. The factor three compensates for the probability $`1/3`$ of choosing the relevant axis.

For a first-source score $`x`$,

```math
\Pr(x=3)=\frac{1+r}{6},\qquad
\Pr(x=-3)=\frac{1-r}{6},\qquad
\Pr(x=0)=\frac23.
```

Consequently $`\mathbb Ex=r`$ and $`\mathbb Ex^2=3`$. A second-source score $`y`$ has the same distribution with $`r=0`$, giving $`\mathbb Ey=0`$ and $`\mathbb Ey^2=3`$. Independent copies and independent axis choices between the sources give the paired score $`z=x-y`$ with

```math
\mathbb Ez=r,\qquad
\Gamma:=\mathrm{Var}(z)=6-r^2.
```

Ordinary measurement of $`Z`$ on the first state would have variance $`1-r^2`$. The randomized score has variance $`3-r^2`$: basis selection adds a known sampling cost. In a many-coordinate, noncommuting model, the [covariance proof](../science/covariance-bound.md) controls the entire covariance matrix, including correlations between coordinates recorded from the same copy.

### Removing the bias from a squared sample mean

For $`N`$ independent paired scores, a squared empirical mean obeys

```math
\mathbb E\left(\frac1N\sum_i z_i\right)^2
=r^2+\frac{6-r^2}{N}.
```

The unwanted term is present even under equality. Removing the diagonal self-products gives the statistic

```math
T=\frac{(\sum_i z_i)^2-\sum_i z_i^2}{N(N-1)},
\qquad \mathbb ET=r^2.
```

For example, these three observed pairs give a complete arithmetic calculation:

| Pair | First axis, sign | $`x_i`$ | Second axis, sign | $`y_i`$ | $`z_i`$ |
|---|---|---:|---|---:|---:|
| 1 | $`Z,+1`$ | $`3`$ | $`X,+1`$ | $`0`$ | $`3`$ |
| 2 | $`X,-1`$ | $`0`$ | $`Z,-1`$ | $`-3`$ | $`3`$ |
| 3 | $`Y,+1`$ | $`0`$ | $`Y,-1`$ | $`0`$ | $`0`$ |

Here $`\sum_i z_i=6`$ and $`\sum_i z_i^2=18`$, so $`T=(36-18)/(3\cdot2)=3`$. Comparing this value with $`\varepsilon^2/4`$ gives the decision **different**. These three pairs illustrate the calculation. The proved confidence guarantee uses the [prescribed schedule](../science/testing-algorithm.md#explicit-protocol), which here is

```math
C_0=5,\qquad
N=\left\lceil\frac{2560}{r^2}\right\rceil
\quad\text{pairs, hence }2N\text{ state copies}.
```

The exact variance for any $`N\ge2`$ is

```math
\mathrm{Var}(T)
=\frac{4r^2(6-r^2)}N
+\frac{2(6-r^2)^2}{N(N-1)}.
```

For the null pair $`(\tau,\tau)`$, the mean is zero and the variance is $`72/[N(N-1)]`$. This explains why the behavior of a single short record is not the uniform error guarantee. The explicit numerical schedule is conservative, as in the main theorem.

### Why the source promise matters

Consider instead $`\sigma=(I+rX)/2`$. Its trace-norm distance from $`\tau`$ is still $`r`$, but its $`Z`$ expectation and its entire $`Z`$-coordinate score distribution agree with those of $`\tau`$. It is thermal at the same $`\beta`$ for Hamiltonian $`-X/16`$, which is outside the supplied menu $`\{Z\}`$.

Thus these scores establish the promised comparison only when both sources obey the stated menu. This is already visible in one qubit; [the interpretation page](../science/interpretation.md#why-both-thermal-promises-matter) gives the corresponding many-qubit limitation. The full raw measurement record and the particular score retained by the protocol are different statistical objects.

## 4. From the foundation to the research proof

The one-qubit calculation displays the components separately. The full proof must make them work uniformly over an interacting, potentially noncommuting family.

| Milestone block | Additional research input and its job |
|---|---|
| [M13–M15: thermal signal](MILESTONES.md#m13-uniform-high-temperature-curvature) | Haah–Kothari–Tang's current high-temperature Hessian theorem controls the parameter-to-moment map. The Gibbs logarithm identity and Watrous's Pinsker foundation then give $`\Vert \rho_h-\rho_g\Vert _1^2\le2\Vert \mu(h)-\mu(g)\Vert _2^2`$. The [geometry proof](../science/thermal-geometry.md) verifies the constants and coefficient segment. |
| [M16–M19: measured noise](MILESTONES.md#m16-duhamel-covariance-and-noncommutativity) | The Hessian controls Duhamel covariance. Harris's comparison, in Brankov–Tonchev's normalization, converts this to ordinary thermal variance with a local commutator correction. The standard Huang–Kueng–Preskill Pauli score and a sparse overlap correction give the [snapshot covariance bound](../science/covariance-bound.md). |
| [M20–M23: decision and implementation](MILESTONES.md#m20-independent-pairs-and-the-unbiased-statistic) | The quadratic statistic uses established U-statistic and high-dimensional mean-testing methods, credited to Hoeffding and Chen–Qin. The project gives its exact finite-sample variance, threshold, copy schedule and streaming implementation in [the algorithm proof](../science/testing-algorithm.md). |
| [M24–M28: collective converse](MILESTONES.md#m24-disjoint-supports-inside-every-allowed-menu) | Disjoint allowed supports embed the classical product-testing obstruction studied by Canonne–Diakonikolas–Kane–Stewart. Bonami's inequality verifies separation of every alternative; a mixture second moment bounds distinguishability. The [lower-bound proof](../science/collective-lower-bound.md) then applies the channel and discrimination foundations to unrestricted collective and adaptive protocols. |

The square-root rate is visible in the general statistic's variance. With $`\delta=\mu(h)-\mu(g)`$ and paired-score covariance $`\Gamma`$, the exact identity is

```math
\mathrm{Var}(T)
=\frac4N\delta^{\mathsf T}\Gamma\delta
+\frac{2}{N(N-1)}\mathrm{Tr}(\Gamma^2).
```

A uniform operator-norm bound on $`\Gamma`$ makes the second term $`O(M/N^2)`$. Under equality the first term vanishes; under the alternative the thermal geometry forces $`\Vert \delta\Vert _2^2\ge\varepsilon^2/2`$. This is how vector covariance, quantum distance and a classical decision statistic combine to produce the $`\sqrt M/\varepsilon^2`$ copy scale.

For the converse, the hidden sign vector is chosen **once per source**. The relevant repeated-copy mixture is $`\mathbb E_s\rho_s^{\otimes S}`$, not $`(\mathbb E_s\rho_s)^{\otimes S}`$. Common diagonalization converts its distance from the null to classical total variation. The discrimination and channel foundations then explain why quantum memory and a final collective measurement cannot reveal information absent from that input. This is the connection between [M11](MILESTONES.md#m11-commuting-models-and-hidden-parameter-mixtures) and [M28](MILESTONES.md#m28-collective-and-adaptive-protocol-reduction).

[M29](MILESTONES.md#m29-matching-bounds-in-the-supported-accuracy-range) combines the bounds only in their shared parameter range. [M30](MILESTONES.md#m30-synthesis-of-operational-meaning-attribution-and-limits) interprets the result with its known-menu and two-source thermal promises, its distinction between copy count and physical workload, and its attribution to the separate ingredients. The [related-work record](../references/RELATED_WORK.md) documents those sources and the broader Gibbs-testing results. Watrous supplies the quantum-information foundation for these connections; the project pages and primary research supply the thermal and statistical arguments.

[W]: https://jhwatrous.github.io/TQI.pdf
