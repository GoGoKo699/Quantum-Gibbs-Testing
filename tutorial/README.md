# Learn Quantum Gibbs Testing

[Project overview](../README.md) · [Exact model and theorem](../science/model.md)

Two laboratories each supply the same unknown state whenever asked for a new preparation. Both sources are promised to be Gibbs states in a specified family. The task is to decide whether they agree, or differ by a prescribed global trace norm. The detector can answer this question from local Pauli measurements without reconstructing either Hamiltonian.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [Watrous bridge](watrous-bridge.md) identifies focused sections in the author's available 2018 manuscript, translates its conventions, and develops the missing connections to thermal geometry and quadratic testing. The [30-milestone map](milestones.md) gives the common understanding route through the project.

The map has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The first phase moves from one state and one measurement to the complete two-source statistical problem. The second builds the local tester, then the hard product subfamily, and finally joins their bounds and physical meaning. Each milestone records a question, an understanding target, its earlier dependencies, the connection it develops, and sources. It is a reader-independent map of the contribution; detailed technical derivations remain in the science pages.

## Start with one spin

Take the known menu to contain only the Pauli operator Z. A source has an unknown coupling h between minus one and one, and a known positive inverse temperature beta. Its two energy eigenstates have relative probabilities fixed by their energies. Normalization gives

```math
\rho_h=\frac{I-\tanh(\beta h)Z}{2},
\qquad \mu(h)=-\tanh(\beta h).
```

A Z measurement returns a sign whose average is the observable moment mu. Here the unhalved trace norm between two source states equals the absolute difference between their moments. A random Pauli readout selects Z with probability one third: assign three times the observed sign when it selects Z, and assign zero otherwise. This score has the same average mu. The full project extends this idea to many overlapping, possibly noncommuting interactions.

With many terms, a small discrepancy can be spread over many moments. Testing each moment separately loses the aggregate signal. The test instead uses products of score differences from **different independent preparations**. Those cross-products estimate the squared mean difference while removing the positive contribution from each preparation's own measurement noise. The [bridge](watrous-bridge.md) explains the mechanism before the [finite-sample proof](../science/testing-algorithm.md).

## Reading routes

| Purpose | Route |
|---|---|
| Understand the physical and statistical question | Milestones M01–M12, alongside the bridge and [model](../science/model.md). |
| Understand why local measurements suffice | M13–M24: [thermal geometry](../science/thermal-geometry.md), [covariance bound](../science/covariance-bound.md), and [testing algorithm](../science/testing-algorithm.md). |
| Understand the unrestricted quantum lower bound | M25–M28 and [collective lower bound](../science/collective-lower-bound.md). |
| Understand optimality, costs, and scope together | M29–M30, [interpretation](../science/interpretation.md), and [Related work](../references/RELATED_WORK.md). |
| Inspect the specialist proofs directly | Start from the exact theorem on the [model page](../science/model.md) and follow its proof links. |
| Reproduce the finite checks | Use [verification](../verification/README.md); its examples check identities and implementations, while the written arguments establish the universal theorem. |

Keep the theorem's promises visible while studying: both sources belong to the same known-menu Gibbs family, the positive temperature is common and known, the uniform upper bound uses an explicit sufficient high-temperature window, and the matching lower bound has a stated separation range. Copies, local readout work, classical storage, and physical preparation time are different resources. The [LLM reading guide](../llms.txt) maps questions to the authoritative files.
