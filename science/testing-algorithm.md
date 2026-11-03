# Equality tester, finite-sample proof, and resources

[Project overview](../README.md) · [Model and main result](model.md) · [Thermal geometry](thermal-geometry.md) · [Measurement covariance](covariance-bound.md)

This page gives an explicit test for equality of two unknown Gibbs states in the promised family. A single run consumes $N$ copies of each source, so its total copy cost is $2N$. Every quantum measurement acts on one qubit of one copy. The remaining computation is a classical quadratic mean test.

## Assumptions and two inputs from the thermal analysis

Use the [model](model.md) with a known menu of $M\ge1$ distinct nonidentity Pauli strings, weight bound $k\ge1$, overlap degree $\Delta$, and $d=\Delta+1$. The two independent sources supply independent and identically distributed copies of $\rho_h$ and $\rho_g$, where $h,g\in[-1,1]^M$ and

$$
0<\beta\le\frac{1}{100e^6d^8}.
\tag{1}
$$

For $0<\epsilon\le2$, the promise problem is

$$
H_0:\rho_h=\rho_g,
\qquad
H_1:\|\rho_h-\rho_g\|_1\ge\epsilon.
\tag{2}
$$

The norm is unhalved. No guarantee is required when neither hypothesis holds.

For one measured copy of $\rho_h$, choose the Pauli axis independently and uniformly at each active site. If term $P_a$ has weight $w_a$, form the real score

$$
X_a=3^{w_a}
\mathbf1\{\text{the selected axes match }P_a\text{ on its support}\}
\prod_{u\in\operatorname{supp}(P_a)}s_u,
\tag{3}
$$

where $s_u\in\{-1,1\}$ is the measured sign. The [covariance proof](covariance-bound.md) establishes

$$
\mathbb E_h X=\mu(h),
\qquad
0\preceq\operatorname{Cov}_h(X)\preceq C_\beta I_M,
\qquad
C_\beta=\frac32+\frac23\beta d^2+d3^k.
\tag{4}
$$

Define the convenient integer majorant

$$
C_0=2+d3^k.
\tag{5}
$$

Condition (1) implies $\beta d^2\le1/(100e^6d^6)<3/4$, so $C_\beta<C_0$. The implemented test can therefore use $C_0$ without evaluating a Gibbs state, partition function, or covariance matrix.

Independently form a score vector $Y$ from a copy of $\rho_g$. The measurement axes are independent between the two sources as well as between different copies. Then

$$
Z=X-Y,
\qquad
\mathbb EZ=\delta:=\mu(h)-\mu(g),
\qquad
\Gamma:=\operatorname{Cov}(Z)\preceq2C_0I_M.
\tag{6}
$$

Sharing the same random axes between the sources would require a different covariance calculation; the protocol uses independent axes.

The second thermal input is the [moment separation inequality](thermal-geometry.md):

$$
\|\rho_h-\rho_g\|_1^2\le2\|\delta\|_2^2.
\tag{7}
$$

Writing $s=\|\delta\|_2^2$, hypotheses (2) therefore imply $s=0$ and $s\ge\epsilon^2/2$, respectively.

## Explicit protocol

Let

$$
q=\lceil\sqrt M\rceil,
\qquad
N=\max\left\{2,\left\lceil\frac{512C_0q}{\epsilon^2}\right\rceil\right\}.
\tag{8}
$$

1. Obtain $N$ independent scores $X_1,\ldots,X_N$ from the first source and $N$ independent scores $Y_1,\ldots,Y_N$ from the second, using (3).
2. Set $Z_i=X_i-Y_i$ and compute

$$
T=\frac{1}{N(N-1)}\sum_{i\ne j}Z_i^{\mathsf T}Z_j
=\frac{\left\|\sum_{i=1}^N Z_i\right\|_2^2-\sum_{i=1}^N\|Z_i\|_2^2}{N(N-1)}.
\tag{9}
$$

3. Output **different** if $T>\epsilon^2/4$, and **equal** otherwise.

The statistic can be negative on a finite sample. It is used as written, without truncating it before the threshold comparison.

Equation (9) is a degree-two U-statistic. Its decomposition is standard statistical machinery going back to [Hoeffding (1948)](https://doi.org/10.1214/aoms/1177730196); unbiased quadratic tests for high-dimensional means also appear in [Chen and Qin (2010)](https://arxiv.org/abs/1002.4547). The following finite-sample calculation is included in full. No normal approximation, asymptotic dimension condition, or unknown covariance estimation is used.

## Exact expectation and variance

**Lemma.** Let $Z_1,\ldots,Z_N$ be independent and identically distributed real vectors with mean $\delta$, finite covariance $\Gamma$, and $N\ge2$. For (9),

$$
\mathbb ET=\|\delta\|_2^2,
\qquad
\operatorname{Var}T
=\frac4N\delta^{\mathsf T}\Gamma\delta
+\frac{2}{N(N-1)}\operatorname{Tr}(\Gamma^2).
\tag{10}
$$

**Proof.** For $i\ne j$, independence gives $\mathbb E[Z_i^{\mathsf T}Z_j]=\|\delta\|_2^2$. This proves the expectation identity.

Set $\xi_i=Z_i-\delta$. Expanding the statistic gives

$$
T-\|\delta\|_2^2
=\frac2N\sum_i\delta^{\mathsf T}\xi_i
+\frac{2}{N(N-1)}\sum_{i<j}\xi_i^{\mathsf T}\xi_j.
\tag{11}
$$

The two sums are uncorrelated. Every cross expectation contains an independent centered vector that occurs only once, so conditioning on the other vectors makes that expectation zero. For the same reason, different terms $\xi_i^{\mathsf T}\xi_j$ and $\xi_r^{\mathsf T}\xi_t$ with distinct unordered index pairs are uncorrelated, including when they share one index. Finally,

$$
\begin{aligned}
\operatorname{Var}(\delta^{\mathsf T}\xi_i)
&=\delta^{\mathsf T}\Gamma\delta,\\
\mathbb E\bigl[(\xi_i^{\mathsf T}\xi_j)^2\bigr]
&=\sum_{a,b}\mathbb E(\xi_{i,a}\xi_{i,b})\,
\mathbb E(\xi_{j,a}\xi_{j,b})\\
&=\sum_{a,b}\Gamma_{ab}^2
=\operatorname{Tr}(\Gamma^2),\qquad i\ne j.
\end{aligned}
$$

There are $N$ terms in the first sum and $N(N-1)/2$ in the second. Substituting their variances in (11) proves (10). Only second moments of an individual vector are needed; no fourth-moment bound for one snapshot enters this argument. $\square$

For the scores in (6), $\delta^{\mathsf T}\Gamma\delta\le2C_0s$ and $\operatorname{Tr}(\Gamma^2)\le4C_0^2M$. Thus

$$
\operatorname{Var}T
\le\frac{8C_0s}{N}+\frac{8C_0^2M}{N(N-1)}
\le\frac{8C_0s}{N}+\frac{16C_0^2M}{N^2}.
\tag{12}
$$

The last inequality uses $N\ge2$. The trace in (10), rather than a sum of separate coordinatewise confidence bounds, is what gives the $\sqrt M$ sample scale.

## Finite-sample guarantee with the stated constants

Under $H_0$, $s=0$. Chebyshev's inequality, (12), and (8) give

$$
\begin{aligned}
\Pr_{H_0}(\text{different})
&\le\frac{\operatorname{Var}T}{(\epsilon^2/4)^2}\\
&\le\frac{256C_0^2M}{N^2\epsilon^4}\\
&\le\frac{M}{1024q^2}
\le\frac{1}{1024}.
\end{aligned}
\tag{13}
$$

Under $H_1$, $s\ge\epsilon^2/2$, hence $s-\epsilon^2/4\ge s/2$. Therefore

$$
\begin{aligned}
\Pr_{H_1}(\text{equal})
&\le\frac{4\operatorname{Var}T}{s^2}\\
&\le\frac{32C_0}{Ns}+\frac{64C_0^2M}{N^2s^2}\\
&\le\frac{64C_0}{N\epsilon^2}
+\frac{256C_0^2M}{N^2\epsilon^4}\\
&\le\frac{1}{8q}+\frac{M}{1024q^2}\\
&\le\frac18+\frac{1}{1024}<\frac16.
\end{aligned}
\tag{14}
$$

Consequently a single run succeeds with probability at least $5/6$ on either side of (2). Its total copy count is exactly $2N$. Since $q\le2\sqrt M$ for $M\ge1$,

$$
2N=O\!\left(\frac{(2+(\Delta+1)3^k)\sqrt M}{\epsilon^2}\right).
\tag{15}
$$

For fixed $k$ and $\Delta$, this is $O_{k,\Delta}(\sqrt M/\epsilon^2)$. The numerical constant 512 is chosen for a transparent bound and is not optimized.

## Confidence amplification

For a desired failure probability $\alpha\in(0,1/2)$, repeat the whole run independently $R$ times and take the majority decision, where $R$ is the smallest positive odd integer satisfying

$$
R\ge\frac92\log\frac1\alpha.
\tag{16}
$$

Each run's error indicator is independent and has expectation at most $1/6$. Hoeffding's inequality gives

$$
\Pr(\text{majority is wrong})
\le\exp\!\left[-2R\left(\frac12-\frac16\right)^2\right]
=e^{-2R/9}\le\alpha.
\tag{17}
$$

This uses $2NR$ total copies and multiplies the time cost by $R$. Runs can be processed sequentially, retaining only the current run's accumulators and a count of decisions. When an exactly represented confidence rule is preferred, any conservative integer upper bound on the right-hand side of (16) may be used. For example, choosing an odd $R\ge5\lceil\log_2(1/\alpha)\rceil$ suffices and can be implemented by integer comparisons for rational $\alpha$.

## Measurement and classical resources

### Input and physical readout

The menu is supplied as explicit supports and local Pauli labels. Its sparse encoding occupies $O(kM\log(2n))$ bits. The coefficients remain unknown. The degree bound and the temperature promise are specified by the model; the tester does not learn an unknown interaction menu or verify the Gibbs promise. If an overlap-degree bound is not supplied separately, it can be computed once from the given menu as described below.

Let $n_{\mathrm{act}}$ be the number of sites appearing in at least one menu support. Then $n_{\mathrm{act}}\le\min\{n,kM\}$. Sites outside this set are maximally mixed tensor factors for both promised states and may be ignored. Each source copy requires $n_{\mathrm{act}}$ independent axis choices and $n_{\mathrm{act}}$ single-qubit measurements. One run therefore uses $2Nn_{\mathrm{act}}$ single-qubit readouts. Reading all $n$ sites instead gives the valid, less sharp cost $2Nn$.

Random Pauli axes can be sampled exactly from unbiased classical bits by rejection sampling with constant expected work per site. The measurement model assumes ideal local Pauli measurements. Their calibration or physical implementation errors are not included in this noiseless theorem.

Copies are supplied by the two sources. Preparing or thermalizing one copy can have a separate physical time cost, and no bound on that preparation cost is asserted here. If a preparation procedure takes known time $t_h$ or $t_g$ per copy, a sequential implementation adds $N(t_h+t_g)$ time per run. The sublinear dependence on $M$ concerns the number of copies; it does not imply sublinear total readout or processing work.

### Streaming implementation and arithmetic operations

Maintain

$$
S=\sum_iZ_i\in\mathbb Z^M,
\qquad
Q=\sum_i\|Z_i\|_2^2\in\mathbb Z.
\tag{18}
$$

For each pair of source records, form $Z_i$, update $S\leftarrow S+Z_i$ and $Q\leftarrow Q+\|Z_i\|_2^2$, and discard the records. At the end form $W=\|S\|_2^2-Q$, so $T=W/[N(N-1)]$. This avoids storing all samples or evaluating $N(N-1)$ pairwise inner products.

A direct scan through the known menu computes a score vector in $O(kM)$ basic operations after the local measurement record has been obtained. Including axis generation and processing the measured signs, a run has expected cost

$$
O\bigl(N(n_{\mathrm{act}}+kM)+M\bigr)
\tag{19}
$$

arithmetic and record-access operations. Active-site addresses can be compressed once into a table of size $n_{\mathrm{act}}$; a direct sorting-based preprocessing implementation takes $O(kM\log(2kM))$ comparisons of $O(\log(2n))$-bit site labels. If needed, compute the overlap graph by listing pairs of menu terms at each site and removing duplicate edges. At most $d$ terms contain any one site, since those terms form a clique in the overlap graph. There are therefore $O(kMd)$ candidate pairs, with duplicate removal costing $O(kMd\log(2kMd))$ comparisons. For fixed $k,\Delta$, this is a one-time near-linear preprocessing cost. No scan over all weight-$k$ strings is needed.

Live working storage is $O(M)$ arithmetic words for the accumulators and one score vector, plus $O(n_{\mathrm{act}})$ bits for a local measurement record and the read-only menu/address table. For fixed $k$, this is $O(M)$ working words. The first source copy can be measured and discarded before the paired second copy is obtained; only its classical score vector is retained. No quantum memory across copies is required.

### Exact integers and bit complexity

The scores (3) are integers in $\{0,\pm3^{w_a}\}$. Consequently

$$
|Z_{i,a}|\le2\,3^k,
\qquad
|S_a|\le2N3^k,
\qquad
0\le Q\le4NM9^k,
\qquad
|W|\le8MN^2 9^k.
\tag{20}
$$

The final bound is deliberately loose. These bounds permit exact accumulation with $O(k+\log(2M)+\log(2N))$ bits per register. Powers $3^w$, $w\le k$, may be precomputed. Large nearly equal terms in $W$ cause no loss of precision when integer arithmetic is used.

If $\epsilon=a/b$ is a positive rational input, with positive integers $a,b$, the decision in step 3 is exactly the integer comparison

$$
4b^2W>a^2N(N-1).
\tag{21}
$$

The sample schedule is also exact: compute $q=\lceil\sqrt M\rceil$ by integer square comparisons and take the ceiling of $512C_0qb^2/a^2$. Neither the numerical value of $\beta$ nor $e^6$ is needed in these operations; (1) is a promise about the sources.

To make the distinction between word and bit costs explicit, let $B$ be a constant multiple of

$$
k+\log(2M)+\log(2N)+\log(2n)+\operatorname{bits}(a)+\operatorname{bits}(b).
$$

All required integer registers and site labels fit in $O(B)$ bits. In a classical random-access model charging for the bits operated on, schoolbook arithmetic gives the conservative per-run bit bound

$$
O\!\left(\bigl[N(n_{\mathrm{act}}+kM)+M\bigr]B^2\right),
\tag{22}
$$

in addition to the one-time menu preprocessing and polynomial-time integer calculations for (8). For fixed $k,\Delta$ and a rational accuracy input of ordinary polynomial bit length, the overhead relative to (19) is polylogarithmic in the numerical problem parameters and polynomial in the input bit length. The storage bound in bits is $O(MB+n_{\mathrm{act}})$ working bits, plus the explicit menu and address table. Confidence amplification adds a decision counter and multiplies the run costs by $R$.

## What the guarantee does and does not establish

The guarantee applies uniformly to two unknown coefficient vectors in the specified cube, including an unknown common state under the null. It requires both sources to obey the same known-menu thermal promise, independent copies, and the explicit high-temperature condition. Exact equality is the completeness condition. Arbitrary-state thermal certification, unknown-graph testing, and constant-gap tolerant trace-norm testing do not follow from this argument.

All data enter through the counted local measurements and explicit classical menu. The procedure does not require Hamiltonian reconstruction, time-evolution access, a purification, coherent data loading, quantum random-access memory, a partition-function oracle, or entangling measurements. These are properties of the stated protocol, not assumptions about how a laboratory prepares the source states.

The local Pauli estimates, U-statistic calculation, and confidence amplification are established tools. The [thermal geometry](thermal-geometry.md) and [covariance bound](covariance-bound.md) establish that they apply with dimension-independent covariance constants to this noncommuting Gibbs comparison problem. The [model page](model.md) states the separate matching lower bound and its nonvacuous accuracy range.

## Statistical references

- Wassily Hoeffding, *A Class of Statistics with Asymptotically Normal Distribution*, *Annals of Mathematical Statistics* **19**, 293–325 (1948), [doi:10.1214/aoms/1177730196](https://doi.org/10.1214/aoms/1177730196): the general U-statistic framework and decomposition.
- Song Xi Chen and Ying-Li Qin, *A two-sample test for high-dimensional data with applications to gene-set testing*, *Annals of Statistics* **38**, 808–835 (2010), [arXiv:1002.4547](https://arxiv.org/abs/1002.4547), [doi:10.1214/09-AOS716](https://doi.org/10.1214/09-AOS716): established quadratic mean-testing methods. Our finite-sample bound is derived above and does not invoke their asymptotic testing theorem.
