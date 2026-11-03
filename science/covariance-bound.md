# Covariance of local Pauli measurements

[Project overview](../README.md) · [Model and main result](model.md)

The tester combines many local observables from each copy. Its sample bound therefore depends on the covariance of the whole measurement vector, rather than on the variance of each coordinate separately. This page proves a bound that is independent of the number of Hamiltonian terms.

## Setting and the high-temperature input

Let
```math
H_h=\sum_{i=1}^{M}h_iP_i,\qquad
\rho_h=\frac{e^{-\beta H_h}}{Z_h},
\qquad |h_i|\le1,
```
where the $`P_i`$ are distinct nonidentity Pauli strings of weight at most $`k`$. Join two menu terms when their supports overlap. Write $`\Delta`$ for the maximum degree of this graph and
```math
d=\Delta+1.
```
Thus every closed overlap neighborhood $`N_i`$ contains at most $`d`$ terms.

The high-temperature input is the uniform bound
**(1)**

```math
\frac{\beta^2}{2}I_M
\preceq\nabla_h^2\log Z_h
\preceq\frac{3\beta^2}{2}I_M.
```
We use the explicit sufficient temperature regime established by Haah, Kothari, and Tang, Corollary 4.4 of [arXiv:2108.04842v3](https://arxiv.org/abs/2108.04842v3). The [model](model.md) fixes the temperature promise used throughout the project. Equation (1) is an inherited equilibrium result. The covariance argument below needs only its upper bound.

For an operator $`A`$, write
```math
\langle A\rangle_h=\mathrm{Tr}(\rho_h A),
\qquad \bar A=A-\langle A\rangle_h I.
```
The centered Bogoliubov–Kubo–Mori, or Duhamel, covariance is
**(2)**

```math
b_h(A,A)
=\int_0^1
\mathrm{Tr}\!\left(
\rho_h^{1-s}\bar A\rho_h^s\bar A
\right)\,ds.
```
Differentiating the matrix exponential gives
**(3)**

```math
a^\mathsf{T}\nabla_h^2\log Z_h\,a
=\beta^2 b_h(A,A),
\qquad A=\sum_i a_iP_i,\quad a\in\mathbb R^M.
```
Consequently, (1) implies
**(4)**

```math
b_h(A,A)\le\frac32\|a\|_2^2.
```

## From Duhamel covariance to ordinary variance

For a Hermitian $`A`$, the Brooks Harris inequality states
**(5)**

```math
b_h(A,A)
\le\mathrm{Var}_{\rho_h}(A)
\le b_h(A,A)
+\frac{\beta}{12}
\left\langle[A,[H_h,A]]\right\rangle_h.
```
We use the normalization in Brankov and Tonchev, [Eq. (2.30)](https://icmp.lviv.ua/journal/zbirnyk.65/003/art03.pdf), which credits Harris, *Journal of Mathematical Physics* **8**, 1044 (1967). Their paper is *Generalized inequalities for the Bogoliubov–Duhamel inner product with applications in the Approximating Hamiltonian Method*, *Condensed Matter Physics* **14**, 13003 (2011), [doi:10.5488/CMP.14.13003](https://doi.org/10.5488/CMP.14.13003).

For completeness, (5) has a short finite-dimensional spectral proof. In an eigenbasis of $`H_h`$, let $`E_r`$ be the energies, $`p_r=e^{-\beta E_r}/Z_h`$, and
```math
L(p_r,p_s)=
\begin{cases}
\displaystyle\frac{p_r-p_s}{\log p_r-\log p_s},&p_r\ne p_s,\\[6pt]
p_r,&p_r=p_s.
\end{cases}
```
The coefficient of $`|\bar A_{rs}|^2`$ in the symmetrized variance is $`(p_r+p_s)/2`$, while its coefficient in (2) is $`L(p_r,p_s)`$. With $`x=\beta(E_s-E_r)/2`$,
```math
\frac{p_r+p_s}{2}=L(p_r,p_s)\,x\coth x.
```
Using $`1\le x\coth x\le1+x^2/3`$, with the continuous value at zero, gives
```math
0\le\frac{p_r+p_s}{2}-L(p_r,p_s)
\le\frac{\beta}{12}(p_r-p_s)(E_s-E_r).
```
Summing over $`r,s`$ proves (5), including degeneracies. It also shows
**(6)**

```math
\left\langle[A,[H_h,A]]\right\rangle_h\ge0.
```

### Locality bounds the double commutator

Expanding $`A=\sum_i a_iP_i`$,
**(7)**

```math
[A,[H_h,A]]
=\sum_{i,j,\ell}a_i a_j h_\ell
[P_i,[P_\ell,P_j]].
```
A nonzero summand must satisfy
**(8)**

```math
\ell\in N_j,\qquad i\in N_\ell\cup N_j.
```
Indeed, the inner commutator vanishes on disjoint supports, and its support is contained in
$`\mathrm{supp}(P_\ell)\cup\mathrm{supp}(P_j)`$.

For each fixed $`j`$, there are at most $`2d^2`$ admissible pairs $`(i,\ell)`$. The same bound holds for the number of pairs $`(j,\ell)`$ at fixed $`i`$: the alternatives $`i\in N_\ell`$ and $`i\in N_j`$ each contribute at most $`d^2`$. These are upper bounds; overcounting zero commutators is harmless.

Each nested commutator has operator norm at most four. Since $`|h_\ell|\le1`$ and $`2|a_i a_j|\le a_i^2+a_j^2`$,
**(9)**

```math
\begin{aligned}
\left|
\left\langle[A,[H_h,A]]\right\rangle_h
\right|
&\le4\sum_{\text{triples satisfying (8)}}|a_i a_j|\\
&\le8d^2\|a\|_2^2. 
\end{aligned}
```
Combining (4), (5), and (9),
**(10)**

```math
\mathrm{Var}_{\rho_h}\!\left(\sum_i a_iP_i\right)
\le C_{\mathrm{th}}\|a\|_2^2,
\qquad
C_{\mathrm{th}}=\frac32+\frac23\beta d^2.
```

Define the real symmetric thermal covariance matrix
```math
G_{ij}=\frac12\langle P_iP_j+P_jP_i\rangle_h
-\langle P_i\rangle_h\langle P_j\rangle_h .
```
Its quadratic form is the variance in (10), so
**(11)**

```math
0\preceq G\preceq C_{\mathrm{th}}I_M.
```
This step accounts for noncommutativity. An upper bound on Duhamel covariance alone does not automatically bound ordinary variance.

## The measurement vector

On each copy, choose the measurement axis independently and uniformly from $`X,Y,Z`$ at every active qubit. Record the axis $`B_u`$ and outcome $`s_u\in\{-1,1\}`$. For a menu string $`P_i`$, let $`w_i`$ be its weight and set
**(12)**

```math
X_i=
3^{w_i}
\mathbf 1\{B_u=(P_i)_u\text{ for every }u\in\mathrm{supp}(P_i)\}
\prod_{u\in\mathrm{supp}(P_i)}s_u.
```
Then
**(13)**

```math
\mathbb E_h X_i=\langle P_i\rangle_h.
```
These are the usual local Pauli classical-shadow estimates; see Huang, Kueng, and Preskill, [*Nature Physics* **16**, 1050–1057 (2020)](https://doi.org/10.1038/s41567-020-0932-7). A single-copy measurement record supplies every coordinate in (12).

To compare their covariance with $`G`$, consider two menu terms.

**Disjoint support.** Their basis-matching events involve different sites, and

```math
\mathbb E_h X_iX_j=\langle P_iP_j\rangle_h
=\frac12\langle P_iP_j+P_jP_i\rangle_h.
```

**Compatible overlap.** If the nonidentity local axes agree on the $`r`$ shared sites, then

```math
\mathbb E_h X_iX_j=3^r\langle P_iP_j\rangle_h.
```

**Incompatible overlap.** If the axes disagree at a shared site, the two coordinates cannot both be nonzero, and

```math
\mathbb E_h X_iX_j=0.
```

The third case also includes globally commuting strings such as $`XX`$ and $`YY`$. Their global commutation does not make them jointly measurable in one product Pauli basis.

Let $`R=\mathrm{Cov}_h(X)-G`$. By (13), the mean-product terms cancel. Thus $`R_{ij}=0`$ on disjoint pairs. On overlapping pairs, including the diagonal,
**(14)**

```math
|R_{ij}|\le3^k.
```
For compatible overlap this follows from $`|3^r-1|\le3^k`$ and $`|\langle P_iP_j\rangle_h|\le1`$. For incompatible overlap the symmetrized product has operator norm at most one.

Each row has at most $`d`$ potentially nonzero entries. Since $`R`$ is real symmetric,
**(15)**

```math
\|R\|_{\mathrm{op}}
\le \max_i\sum_j|R_{ij}|
\le d3^k.
```

## Covariance bound

**Proposition.** Under the model above and the high-temperature Hessian upper bound (1),
**(16)**

```math
\boxed{
0\preceq\mathrm{Cov}_h(X)\preceq C_\beta I_M,
\qquad
C_\beta=\frac32+\frac23\beta(\Delta+1)^2+(\Delta+1)3^k.
}
```
The bound holds uniformly over $`h\in[-1,1]^M`$.

For independent snapshots $`X`$ and $`Y`$ from two admissible sources,
**(17)**

```math
\mathrm{Cov}(X-Y)
=\mathrm{Cov}(X)+\mathrm{Cov}(Y)
\preceq2C_\beta I_M.
```
These are the covariance estimates used by the [equality tester](testing-algorithm.md). The explicit temperature regime of the model implies $`(2/3)\beta d^2\le1/2`$, so the simpler upper bound $`C_0=2+d3^k`$ may be used for the implemented sample-size rule. The constants are conservative; no optimal prefactor is claimed.

The argument uses bounded interaction overlap and uniform high-temperature curvature. It does not require a spatial lattice, translation invariance, a correlation-length estimate, or a separate comparison between correlation decay and graph-volume growth.

[Deterministic numerical checks](../verification/README.md) examine the spectral, commutator, and measurement identities on small noncommuting systems. They check the implementation and selected examples; the proof above supplies the uniform statement.
