# A lower bound for collective and adaptive protocols

This proof supplies the lower bound for the testing problem in [the model](model.md). Throughout, distance means the **unhalved trace norm**. The lower bound is valid for every positive inverse temperature in the error range stated below; the high-temperature assumption enters the matching upper bound, not this construction.

The statistical ingredients are inherited. Random signs and a chi-square second moment give the classical product-uniformity lower bound; see Canonne, Diakonikolas, Kane and Stewart, [*Testing Bayesian Networks*, Theorem 9 and Section 2.2](https://proceedings.mlr.press/v65/canonne17a/canonne17a.pdf). The separation argument uses [Bonami's hypercontractive inequality](https://doi.org/10.5802/aif.357). We give the details needed to embed that construction into every permitted Pauli menu and to cover unrestricted collective processing of the copies.

## Statement

Let $`P_1,\ldots,P_M`$ be distinct nonidentity Pauli strings. Their support-overlap graph has maximum degree $`\Delta`$, and $`d=\Delta+1`$. Fix $`\beta>0`$ and consider the family

```math
H_h=\sum_{a=1}^M h_aP_a,\qquad
\rho_h=\frac{e^{-\beta H_h}}{\mathrm{Tr}e^{-\beta H_h}},
\qquad h\in[-1,1]^M.
```

Assume $`M\ge1`$ and

```math
0\lt \varepsilon\le
\min\left\{\frac1{16},\frac{\beta\sqrt{M/d}}8\right\}.
```

Any protocol that distinguishes $`\rho_h=\rho_g`$ from $`\|\rho_h-\rho_g\|_1\ge\varepsilon`$ with success probability at least $`2/3`$ on every promised pair must have deterministic total copy cap

```math
S>\frac{\sqrt{M/d}}{64\varepsilon^2}.
```

Here a protocol may choose which source to sample adaptively, keep all its quantum systems in memory, use arbitrary ancillas and intermediate quantum operations, and perform a collective final measurement. The bound counts copies from both sources together. More precisely, the proof excludes every integer cap $`S\le\sqrt L/(64\varepsilon^2)`$, where $`L`$ is the size of the disjoint-support subfamily chosen below.

This is a worst-case lower bound for each fixed known menu. It does not assume that the menu contains one-qubit Pauli strings.

## 1. An admissible product subfamily

A greedy independent-set construction gives indices $`a_1,\ldots,a_L`$ whose supports are pairwise disjoint, with

```math
L\ge\left\lceil\frac{M}{d}\right\rceil.
```

Indeed, choosing a vertex and deleting its closed neighborhood removes at most $`d`$ vertices per choice. Write $`Q_i=P_{a_i}`$ and set

```math
r=\frac{4\varepsilon}{\sqrt L},\qquad t=Lr^2=16\varepsilon^2.
```

For each sign vector $`s\in\{-1,+1\}^L`$, define coefficients

```math
h_{a_i}(s)=-\frac{s_i\mathrm{arctanh}(r)}{\beta},
\qquad h_a(s)=0\quad\text{for }a\notin\{a_1,\ldots,a_L\}.
```

The error assumptions imply $`r\le1/4`$, $`t\le1/16`$, and

```math
\mathrm{arctanh}(r)\le2r
=\frac{8\varepsilon}{\sqrt L}\le\beta.
```

Thus all coefficients lie in the required cube. Since the $`Q_i`$ act on disjoint supports,

```math
\rho_s:=\rho_{h(s)}=2^{-n}\prod_{i=1}^L(I+rs_iQ_i).
```

The maximally mixed state $`\tau=I/2^n`$ is also in the family, with coefficient vector zero.

Each nonidentity Pauli string supported on $`w_i`$ qubits has eigenvalues $`+1`$ and $`-1`$, each with multiplicity $`2^{w_i-1}`$. Consequently, the simultaneous eigenspace for every vector of signs $`x\in\{-1,+1\}^L`$ has the same dimension $`2^{n-L}`$. This includes all qubits outside the selected supports. In a fixed common eigenbasis, the informative outcome distribution of $`\rho_s`$ is therefore exactly

```math
p_s(x)=2^{-L}\prod_{i=1}^L(1+rs_ix_i).
```

All other basis labels have a uniform conditional distribution, common to every state in the construction. The state $`\tau`$ gives the uniform distribution $`u(x)=2^{-L}`$. These equal degeneracies are why disjoint strings of different weights cause no change to the lower bound.

## 2. Every alternative has the required trace separation

Expectations and $`L^p`$ norms in this section are with respect to $`u`$. The likelihood-ratio displacement is

```math
f_r(x)=\frac{p_s(x)}{u(x)}-1
=\prod_{i=1}^L(1+rs_ix_i)-1.
```

Its nonconstant Fourier coefficients are $`r^{|A|}\prod_{i\in A}s_i`$, so Parseval gives

```math
\|f_r\|_2^2=(1+r^2)^L-1\ge Lr^2=t.
```

Let $`T_\eta`$ be the Boolean noise operator, multiplying a Fourier coefficient of degree $`j`$ by $`\eta^j`$. The Bonami inequality in the needed normalization is

```math
\|T_{1/\sqrt3}f\|_4\le\|f\|_2.
```

Because $`f_r=T_{1/\sqrt3}f_{\sqrt3r}`$, it follows that

```math
\|f_r\|_4^2
\le\|f_{\sqrt3r}\|_2^2
=(1+3r^2)^L-1
\le e^{3t}-1
\le4t.
```

The last inequality holds for $`0\le t\le1/16`$: the derivative of $`4t-(e^{3t}-1)`$ is at least $`4-3e^{3/16}>0`$ on this interval. Hölder interpolation gives

```math
\|f_r\|_2\le\|f_r\|_1^{1/3}\|f_r\|_4^{2/3},
```

and hence

```math
\|\rho_s-\tau\|_1
=\|p_s-u\|_1
=\|f_r\|_1
\ge\frac{\|f_r\|_2^3}{\|f_r\|_4^2}
\ge\frac{\sqrt t}{4}
=\varepsilon.
```

The first equality uses the equal common eigenspace multiplicities from Section 1. Thus **every fixed sign vector** gives a promised alternative; no conditioning on a likely event or asymptotic normal approximation is needed.

## 3. Exact chi-square calculation for repeated copies

Compare the null pair $`(\tau,\tau)`$ with the alternative pairs $`(\rho_s,\tau)`$. Draw $`s`$ uniformly once and keep it fixed for the entire first source. On $`S`$ copies from that source, the informative classical mixture is

```math
\overline p_S=2^{-L}\sum_s p_s^{\otimes S}.
```

This is a mixture of repeated-copy distributions. Averaging the state separately for each copy would instead erase the statistical problem and is not the experiment used here.

Writing $`u_S=u^{\otimes S}`$ and introducing an independent uniform sign vector $`v`$, the likelihood-ratio second moment is

```math
\begin{aligned}
1+\chi^2(\overline p_S\|u_S)
&=\mathbb E_{s,v}
  \left[\mathbb E_{x\sim u}
  \prod_{i=1}^L(1+rs_ix_i)(1+rv_ix_i)\right]^S\\
&=\mathbb E_{s,v}\prod_{i=1}^L(1+r^2s_iv_i)^S\\
&=\left[\frac{(1+r^2)^S+(1-r^2)^S}{2}\right]^L.
\end{aligned}
```

Using $`\log(1+z)\le z`$, $`\log(1-z)\le-z`$, and $`\cosh z\le e^{z^2/2}`$,

```math
\chi^2(\overline p_S\|u_S)
\le\cosh(Sr^2)^L-1
\le\exp\left(\frac{LS^2r^4}{2}\right)-1.
```

If $`S\le\sqrt L/(64\varepsilon^2)`$, then

```math
\frac{LS^2r^4}{2}\le\frac1{32},\qquad
\mathrm{TV}(\overline p_S,u_S)
\le\frac12\sqrt{e^{1/32}-1}
\lt 0.09\lt \frac13.
```

The optimal success probability for distinguishing the null from this mixture with equal prior probabilities is $`(1+\mathrm{TV})/2\lt 2/3`$.

## 4. Why adaptivity and collective measurements cannot evade the bound

The second source is $`\tau`$ under both hypotheses. Grant a tester its exact description and unlimited free preparations of it. This can only make the task easier. Any protocol with deterministic total copy cap $`S`$ can then be simulated from $`S`$ pre-supplied copies of the first source: provide the next stored copy whenever the protocol requests that source, generate $`\tau`$ whenever it requests the other source, and discard any unused copies when the protocol stops. All adaptive measurements, classical records, quantum memories and final decisions form a quantum channel applied to these inputs.

The inputs $`\tau^{\otimes S}`$ and

```math
\overline\rho_S=2^{-L}\sum_s\rho_s^{\otimes S}
```

are diagonal in the same known basis. Their uninformative degeneracy labels have the same conditional distribution, so

```math
\frac12\|\overline\rho_S-\tau^{\otimes S}\|_1
=\mathrm{TV}(\overline p_S,u_S).
```

Trace-norm contractivity therefore bounds every protocol's output distinguishability by the value in Section 3. Equivalently, a POVM on common diagonal states is a stochastic processing of their basis labels, even when its operators are not diagonal. Neither argument restricts the physical measurement used by the tester.

A protocol succeeding with probability at least $`2/3`$ on the null and on each fixed $`s`$ would also succeed with probability at least $`2/3`$ against the uniform mixture. Section 3 excludes this for every integer $`S\le\sqrt L/(64\varepsilon^2)`$. Since $`L\ge M/d`$, the stated lower bound follows.

## 5. Range and meaning of optimality

For fixed $`\Delta`$, the bound is $`\Omega(\sqrt M/\varepsilon^2)`$. Together with [the local-measurement upper bound](testing-algorithm.md), it gives matching scaling at the prescribed high temperature whenever

```math
0\lt \varepsilon\le\min\left\{\frac1{16},\frac{\beta\sqrt{M/d}}8\right\}.
```

At any fixed positive allowed $`\beta`$ and fixed $`0\lt \varepsilon\le1/16`$, the second restriction holds as soon as

```math
M\ge\frac{64d\varepsilon^2}{\beta^2}.
```

No further large-$`M`$ assumption is used. Outside this error range the upper bound remains available, but this construction does not establish matching optimality. In particular, one should not extrapolate a nonzero lower bound to an error threshold for which the alternative promise is empty. The theorem concerns a deterministic cap on copies, not a separate expected-stopping-time model.
