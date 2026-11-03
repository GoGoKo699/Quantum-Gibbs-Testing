# Thermal geometry and the observable separation

[Project overview](../README.md) · [Model and main result](model.md) · [Measurement covariance](covariance-bound.md)

The equality tester measures only the specified Hamiltonian terms. This page shows why those observables detect a global trace-norm separation between two states in the promised high-temperature Gibbs family. The equilibrium curvature theorem is inherited from Haah, Kothari, and Tang; the argument below records its assumptions, constants, and the resulting testing implication.

## Family and conventions

Let $`P_1,\ldots,P_M\in\{I,X,Y,Z\}^{\otimes n}`$ be distinct nonidentity Pauli strings, with $`M\ge1`$ and weight at most $`k\ge1`$. For $`h\in[-1,1]^M`$, define

**(1)**

```math
H_h=\sum_{a=1}^M h_aP_a,
\qquad Z_h=\mathrm{Tr}e^{-\beta H_h},
\qquad \rho_h=\frac{e^{-\beta H_h}}{Z_h},
\qquad L(h)=\log Z_h.
```

All logarithms in this page are natural. The norm $`\|\rho-\sigma\|_1`$ is the **unhalved** trace norm. The convention sometimes called trace distance is half this quantity.

Join distinct menu terms when their supports intersect. Let $`\Delta`$ be a supplied upper bound on the maximum degree of this graph and write $`d=\Delta+1`$. Throughout, assume

**(2)**

```math
0\lt \beta\le\beta_0,
\qquad
\beta_0=\frac{1}{100e^6(\Delta+1)^8}.
```

The observable vector is

**(3)**

```math
\mu(h)_a=\mathrm{Tr}(\rho_hP_a).
```

Neither the coefficients nor the partition function need to be computed by the tester. They specify the statistical promise used in the proof.

## The inherited Hessian bound

We use [Haah, Kothari, and Tang, arXiv:2108.04842v3](https://arxiv.org/pdf/2108.04842v3), specifically Eq. (101), Lemma 4.3, and Corollary 4.4 with Eqs. (112)–(113). Equation numbers refer to the linked v3 PDF. Their symbols $`E_a,\lambda,N`$ correspond to our $`P_a,h,n`$; their degree $`d`$ is bounded by our $`\Delta`$. Thus using a supplied degree upper bound in (2) only makes their temperature condition more restrictive. Their $`d`$ does not denote our closed-neighborhood bound $`\Delta+1`$.

Their assumptions match this family: bounded real coefficients, traceless terms orthonormal in normalized Hilbert–Schmidt inner product, and an overlap graph defined by intersecting supports. Here these conditions hold because

**(4)**

```math
\mathrm{Tr}P_a=0,
\qquad 2^{-n}\mathrm{Tr}(P_aP_b)=\delta_{ab},
\qquad \|P_a\|_{\mathrm{op}}=1.
```

Their exact moment-map Jacobian $`J(h)=\nabla_h\mu(h)`$ satisfies, uniformly on the coefficient cube,

**(5)**

```math
\left\|I_M+\beta^{-1}J(h)\right\|_{\infty\to\infty}\le\frac12.
```

Differentiation of (1) gives

**(6)**

```math
\nabla_h L(h)=-\beta\mu(h),
\qquad \nabla_h^2L(h)=-\beta J(h).
```

Consequently $`J(h)`$ is real symmetric. For a real symmetric matrix, the spectral norm is bounded by its maximum absolute row sum. Thus (5) implies

**(7)**

```math
\boxed{
\frac{\beta^2}{2}I_M
\preceq\nabla_h^2L(h)
\preceq\frac{3\beta^2}{2}I_M
\quad\text{for every }h\in[-1,1]^M.
}
```

Both sides of (7) are present in the cited proof. Equation (2) is a sufficient explicit temperature condition; no claim is made that it is the largest possible regime.

For completeness, an actual overlap degree of zero can be checked directly without invoking a graph-counting formula, regardless of the supplied upper bound. In this case the term supports are disjoint and

```math
Z_h=2^n\prod_{a=1}^M\cosh(\beta h_a).
```

Hence the Hessian is diagonal, with entries $`\beta^2\mathrm{sech}^2(\beta h_a)`$. Condition (2) implies $`|\beta h_a|\lt 1/2`$, so these entries lie between $`\beta^2/2`$ and $`\beta^2`$, which proves (7) in this case as well.

## Curvature is Duhamel covariance

This identification also supplies the thermal input to the [measurement covariance proof](covariance-bound.md). For a real vector $`v`$, let

```math
A_v=\sum_a v_aP_a,
\qquad
\bar A_v=A_v-\mathrm{Tr}(\rho_hA_v)I.
```

The derivative of the matrix exponential in direction $`A_v`$ is

**(8)**

```math
\left.\frac{d}{dt}e^{-\beta(H_h+tA_v)}\right|_{t=0}
=-\beta\int_0^1 e^{-(1-s)\beta H_h}A_v e^{-s\beta H_h}\,ds.
```

Taking its trace yields the first identity in (6). Differentiating once more, including the derivative of the normalizing partition function, yields

**(9)**

```math
v^{\mathsf T}\nabla_h^2L(h)v
=\beta^2\int_0^1
\mathrm{Tr}\!\left(\rho_h^{1-s}\bar A_v\rho_h^s\bar A_v\right)\,ds.
```

The integral is the centered Duhamel covariance. Equation (7) therefore bounds it between $`\|v\|_2^2/2`$ and $`3\|v\|_2^2/2`$. Ordinary quantum variance requires a further comparison; that step is supplied by the Harris inequality in the covariance proof.

## A uniform bound along the coefficient segment

Take any two admissible coefficient vectors $`h,g\in[-1,1]^M`$. Set

**(10)**

```math
v=h-g,
\qquad \delta=\mu(h)-\mu(g),
\qquad
K=\int_0^1\nabla^2L(g+tv)\,dt.
```

The cube is convex, so $`g+tv\in[-1,1]^M`$ at every $`t\in[0,1]`$. The same menu, overlap degree, coefficient bound, and temperature condition therefore apply throughout this integral. The fundamental theorem of calculus and (6) give the exact matrix identity

**(11)**

```math
-\beta\delta=Kv.
```

Integrating (7) preserves the semidefinite bounds:

**(12)**

```math
\frac{\beta^2}{2}I_M\preceq K\preceq\frac{3\beta^2}{2}I_M.
```

In particular, $`K`$ is invertible, and

**(13)**

```math
\frac{\beta}{2}\|h-g\|_2
\le\|\mu(h)-\mu(g)\|_2
\le\frac{3\beta}{2}\|h-g\|_2.
```

The integral in (10) is essential to the statement: all coordinates are controlled by one symmetric positive matrix. No assertion that different coordinatewise mean-value points coincide is required.

## Relative entropy converts moments to global trace norm

For full-rank states define

```math
D(\rho\|\sigma)=\mathrm{Tr}\bigl[\rho(\log\rho-\log\sigma)\bigr],
\qquad
D_{\mathrm{sym}}(\rho,\sigma)=D(\rho\|\sigma)+D(\sigma\|\rho).
```

Finite-temperature Gibbs states are full rank. Substituting $`\log\rho_h=-\beta H_h-L(h)I`$ gives

**(14)**

```math
\begin{aligned}
D(\rho_h\|\rho_g)
&=-\beta(h-g)\cdot\mu(h)+L(g)-L(h),\\
D_{\mathrm{sym}}(\rho_h,\rho_g)
&=-\beta(h-g)\cdot\bigl(\mu(h)-\mu(g)\bigr).
\end{aligned}
```

These are exact exponential-family identities and hold also for noncommuting Hamiltonian terms. Using (11)–(12),

**(15)**

```math
\begin{aligned}
D_{\mathrm{sym}}(\rho_h,\rho_g)
&=v^{\mathsf T}Kv\\
&=\beta^2\delta^{\mathsf T}K^{-1}\delta\\
&\le2\|\delta\|_2^2.
\end{aligned}
```

Quantum Pinsker's inequality with natural logarithms reads

**(16)**

```math
D(\rho\|\sigma)\ge\frac12\|\rho-\sigma\|_1^2.
```

One way to check this normalization is to measure the projector onto the positive part of $`\rho-\sigma`$. The difference of the resulting binary success probabilities is $`\|\rho-\sigma\|_1/2`$. Relative entropy cannot increase under this measurement, by [Lindblad's data-processing theorem](https://doi.org/10.1007/BF01609396). Binary relative entropy satisfies $`D_{\mathrm{bin}}(p\|q)\ge2(p-q)^2`$: its second derivative with respect to $`p`$ is $`1/[p(1-p)]\ge4`$, and its value and first derivative vanish at $`p=q`$. This proves (16); boundary probabilities follow by continuity.

Apply (16) in both orders and then (15):

**(17)**

```math
\boxed{
\|\rho_h-\rho_g\|_1^2
\le D_{\mathrm{sym}}(\rho_h,\rho_g)
\le2\|\mu(h)-\mu(g)\|_2^2.
}
```

Equivalently,

**(18)**

```math
\|\rho_h-\rho_g\|_1\le\sqrt2\,\|\mu(h)-\mu(g)\|_2.
```

Thus a trace-norm separation of at least $`\epsilon`$ forces squared observable separation at least $`\epsilon^2/2`$. Exact equality gives zero observable separation. These are precisely the two implications used by the [testing algorithm](testing-algorithm.md).

## Scope of the implication

Both states in (17) must belong to the stated family. For an arbitrary state outside that family, equality of the selected local moments need not imply equality to a Gibbs state. The result therefore compares two promised Gibbs sources; it does not test the thermal promise itself.

The estimate controls trace norm from observable separation. It does not give a dimension-independent converse of the form $`\|\mu(h)-\mu(g)\|_2\le C\|\rho_h-\rho_g\|_1`$, and the tester does not assert constant-gap tolerant testing in trace norm. The elementary coordinatewise converse only yields $`\|\mu(h)-\mu(g)\|_2\le\sqrt M\|\rho_h-\rho_g\|_1`$.

The identity term has been excluded to remove the scalar ambiguity in the Hamiltonian. Indeed, if $`\rho_h=\rho_g`$, their logarithms show $`H_h-H_g`$ is scalar; tracelessness and Pauli orthogonality force $`h=g`$. The proof does not assume that the Hamiltonians commute, have a spatial lattice, or possess a spectral gap.

## Source attribution

- Jeongwan Haah, Robin Kothari, and Ewin Tang, *Optimal learning of quantum Hamiltonians from high-temperature Gibbs states*, [arXiv:2108.04842v3](https://arxiv.org/pdf/2108.04842v3): the uniform high-temperature Hessian theorem and explicit sufficient threshold.
- Göran Lindblad, *Completely positive maps and entropy inequalities*, *Communications in Mathematical Physics* **40**, 147–151 (1975), [doi:10.1007/BF01609396](https://doi.org/10.1007/BF01609396): quantum relative-entropy data processing, used in the standard Pinsker argument.

The Hessian theorem, Gibbs relative-entropy identities, and Pinsker inequality are inherited tools. The calculation here makes their normalization and role in the stated comparison problem explicit.
