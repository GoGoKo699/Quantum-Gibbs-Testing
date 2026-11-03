# Interpretation and limits

The [main theorem](model.md) determines the worst-case number of independent preparations needed to compare two unknown Gibbs sources in a known, bounded-overlap interaction family at sufficiently high temperature. Independent local measurements attain the same order of copy complexity as arbitrary collective measurements. This is a statement about the promised comparison task and its information cost.

## Global comparison from local data

The measured quantities are local Pauli expectations, but the decision guarantee is in global trace norm. The connection uses the Gibbs exponential-family promise. The full state is determined by its interaction coefficients, and uniform curvature makes the interaction expectations quantitatively informative about separation between members of this family.

The test compares sources without outputting their coefficients. Learning an entire Hamiltonian imposes a different loss function and a different output obligation. The square-root dependence on the number of interactions arises because a quadratic statistic detects the aggregate discrepancy while cancelling its self-noise. It is not obtained by estimating each coordinate to a uniformly small error and taking a union bound.

Noncommutativity is present in the model and in the upper-bound proof. The Hessian of the log partition function is a Duhamel covariance, while a measured observable has ordinary variance. [The covariance proof](covariance-bound.md) bridges these objects with Harris's inequality and a local double-commutator estimate. Treating the two covariance matrices as identical would leave a gap for noncommuting Hamiltonians.

The matching converse is deliberately commuting. A hard commuting subfamily is sufficient to lower-bound the entire quantum model. It establishes that entangling measurements cannot improve the worst-case order of the copy rate; it does not rule out better constants or easier particular pairs.

## Why both thermal promises matter

For $`n>k`$, consider

```math
\tau=2^{-n}I,
\qquad
\omega=2^{-n}\bigl(I+\varepsilon Z^{\otimes n}\bigr),
\qquad 0<\varepsilon\leq1.
```

These are valid states and $`\lVert\omega-\tau\rVert_1=\varepsilon`$. Every nonidentity Pauli string of weight at most $`k`$ has zero expectation in both states. Therefore their interaction-moment vectors agree for any menu of that weight, despite their global separation. For $`\varepsilon<1`$, the logarithm of $`\omega`$ contains the full-weight parity operator and cannot be represented using only such a bounded-weight menu; $`\varepsilon=1`$ is additionally not full rank.

This example defeats the moment-to-trace-norm implication outside the promised family. It does not assert that the complete local measurement record contains no parity information: measuring all qubits in the Z basis does expose that information. The point is precise: the theorem's interaction-moment statistic and its soundness proof rely on **both** sources satisfying the family promise. They are not a generic detector of an arbitrary malfunctioning source.

## Why the known menu matters

The supplied list identifies which $`M`$ moment coordinates to estimate and bounds the support-overlap degree of that list. It is stronger than the statement that an unknown Hamiltonian happens to be sparse. A candidate list containing every possible edge can have a large overlap degree even when each realized Hamiltonian has bounded degree. Replacing the known menu with an unknown graph changes both the measurement problem and its converse; the current theorem does not make that replacement.

The coefficient cube also fixes an energy scale. Rescaling the Hamiltonian without rescaling $`\beta`$ changes the promise. Zero inverse temperature makes every state maximally mixed and the testing problem trivial, which is why the theorem and the nonvacuous lower-bound range require $`\beta>0`$.

## Temperature, finite examples and useful scope

The sufficient threshold $`\beta_*=[100e^6(\Delta+1)^8]^{-1}`$ is small, even at modest overlap degree. It comes from an existing uniform high-temperature theorem rather than a claim of a physically sharp transition. The result is a sharp asymptotic copy law within that window. It does not by itself establish experimentally economical sample constants or applicability near a critical point.

The proof separates the roles of its ingredients. Uniform log-partition curvature converts trace separation to a moment signal; controlled ordinary and snapshot covariance controls noise. A broader thermal regime would require justified versions of these properties. Checking a few endpoints or a finite numerical grid cannot certify uniform curvature for every unknown pair in a family. The [finite examples](../verification/README.md) are consequently labelled by their tested temperature and by whether they fall inside the stated sufficient window.

The lower bound imposes a further relation between $`\varepsilon`$, $`\beta`$ and $`M`$. Its weakly biased product states must fit inside the coefficient cube and still be trace-norm separated. This condition is displayed in the main theorem instead of being hidden in asymptotic notation.

## Copy cost and physical workload

Each statistical sample is an independently prepared state. The test requires no coherent preparation inverse, Hamiltonian simulation or retained quantum memory, and its detector consists of single-qubit Pauli readout. It still consumes a full source preparation per copy. A laboratory's thermalization time, imperfect mixing, drift between copies and correlated preparation errors are not specified by the copy-access model.

With $`M=\Theta(n)`$ and fixed $`k,\Delta`$, the theorem gives order $`\sqrt n/\varepsilon^2`$ copies, while reading and processing all interaction data has order $`n^{3/2}/\varepsilon^2`$ elementary workload at fixed success probability. The result should not be described as sublinear total laboratory or classical work in the system size. Unused spectator qubits need not be measured, and all constants associated with the known interaction list remain explicit in the algorithm.

## Attribution and open boundaries

The high-temperature Hessian theorem, Harris inequality, local-Pauli estimators, quadratic mean-testing statistic and random-sign product-testing lower-bound mechanism are inherited tools. Their combination here supports the stated optimal comparison theorem for interacting, potentially noncommuting thermal sources. [Related work](../references/RELATED_WORK.md) compares that operational claim with broader Gibbs certification and with classical product testing, including its rare-marginal regimes.

Natural questions beyond the theorem include a better justified temperature range, unknown interaction menus and tolerant global comparison. They are separate mathematical problems, not additional claims of this account. The source promise, exact null hypothesis and explicit nonvacuous separation range are part of the result itself.
