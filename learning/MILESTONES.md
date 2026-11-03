# Thirty milestones for Quantum Gibbs Testing

[Project overview](../README.md) · [Model and main result](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md)

This map follows the scientific structure of the project: how local measurements can compare two unknown thermal sources in global trace norm, and why collective measurements cannot improve the worst-case copy rate in the stated matching regime. Its thirty understanding targets are common to every reader. Detailed calculations remain in the linked proof pages.

## Allocation and educational anchor

| Phase | Milestones | Role in the scientific story |
|---|---|---|
| Background/preliminaries | M01–M12 | Build from individual states, observables, and fluctuations to the full quantum statistical comparison problem. |
| Narrative/innovation | M13–M30 | Assemble the signal and noise bounds, the implemented test, and the converse into the operational theorem and its limits. |

The twelve background milestones connect quantum information, equilibrium states, and finite-sample statistics. The eighteen narrative milestones follow the two substantial proof directions and their resource accounting. Each phase ends with a synthesis of its components. The second phase attributes imported results and identifies the contribution in their precise operational combination.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's manuscript][W] supplies the section numbering used below; the [publisher record](https://doi.org/10.1017/9781316848142) identifies the published book. The relevant route is Sections 1.1.3 and 1.2, Sections 2.1–2.3, Section 3.1.1, and Section 5.2, especially 5.2.3. These sections provide matrix, probability, state, measurement, discrimination, and entropy foundations; they are not a requirement to read the entire book.

Watrous's manuscript calls the unhalved matrix trace norm between states their trace distance. This project uses that same unhalved quantity and explicitly distinguishes the alternative convention with a factor of one half. Watrous uses base-two logarithms for entropy; the project uses natural logarithms. The [bridge](WATROUS_BRIDGE.md) translates these conventions and connects the anchor to the proof.

The high-temperature curvature theorem, Harris variance comparison, Pauli snapshot covariance argument, quadratic testing calculation, and product-mixture converse require the project pages and their cited primary research. A source pointer to Watrous supplies foundations, not a claim that the book contains these research ingredients.

## Phase I: Background/preliminaries

### M01: States, observables, and outcome probabilities

**Central question.** How does a quantum state determine the statistics of a measurable quantity?

**Understanding target.** Distinguish a density operator, a Hermitian observable, an individual measurement outcome, and an expectation value. Explain why a probability model for repeated experiments is needed even when the state is fixed.

**Dependencies and story role.** No earlier milestone. This establishes the individual objects from which both the thermal model and the data analysis are built.

**Conceptual connection.** The operator expression for an expectation becomes the mean of a classical record after a measurement has been specified.

**Source pointers.** [Watrous, Sections 2.1 and 2.3][W]; [model: known interaction menu and unknown sources](../science/model.md#known-interaction-menu-and-unknown-sources).

### M02: Tensor products, Pauli strings, and support

**Central question.** What makes an interaction local in a register of many qubits?

**Understanding target.** Explain tensor-product Pauli strings, their nonidentity support and weight, and their orthogonality as operator coordinates. Distinguish support overlap from commutation: overlapping strings can commute, and locality is a statement about support.

**Dependencies and story role.** M01. Extend individual observables to the structured many-qubit coordinates used by the entire project.

**Conceptual connection.** Tensor-product structure supports both the Hamiltonian description and single-qubit implementation of its measurement scores.

**Source pointers.** [Watrous, Sections 1.1.3 and 2.1][W] for operator and register foundations; [model: known interaction menu](../science/model.md#known-interaction-menu-and-unknown-sources) for the project's Pauli convention.

### M03: Gibbs states and the coefficient energy scale

**Central question.** How do an interaction Hamiltonian and temperature specify a thermal state?

**Understanding target.** Explain the normalized matrix exponential, partition function, inverse temperature, and coefficient cube. Recognize why adding an identity term leaves the state unchanged and why changing the coefficient bound changes the energy scale of the promise.

**Dependencies and story role.** M01–M02. Introduce the physical family whose unknown members will be compared.

**Conceptual connection.** A many-body equilibrium model becomes a finite-dimensional family of probability-generating density operators.

**Source pointers.** [Thermal geometry: family and conventions](../science/thermal-geometry.md#family-and-conventions); [model](../science/model.md). [Watrous, Sections 1.1.3 and 2.1][W] supply matrix and state foundations; the Gibbs-family specification is supplied locally.

### M04: Menus, overlap graphs, and locality

**Central question.** What information does a known bounded-overlap interaction menu provide?

**Understanding target.** Distinguish the allowed menu from the set of nonzero realized couplings. Interpret the overlap graph and its closed-neighborhood bound, and explain why an unknown sparse Hamiltonian does not automatically satisfy a known sparse-menu promise.

**Dependencies and story role.** M02–M03. Make the structural assumptions precise before using them to control measurement noise or construct hard instances.

**Conceptual connection.** One combinatorial description will control local commutator counting in the upper bound and disjoint interaction selection in the converse.

**Source pointers.** [Model: known interaction menu](../science/model.md#known-interaction-menu-and-unknown-sources); [interpretation: why the known menu matters](../science/interpretation.md#why-the-known-menu-matters). This project-specific graph structure is not an imported Watrous theorem.

### M05: Copy sources and measurement access

**Central question.** What operations and resources does the comparison experiment actually supply?

**Understanding target.** Distinguish an independently prepared copy from a classical description, a purification, or dynamics access. Explain the difference between independent local measurements and unrestricted collective or adaptive protocols, and count copies from both sources.

**Dependencies and story role.** M01–M02. Establish the operational model within which the upper and lower bounds can be compared fairly.

**Conceptual connection.** Quantum channels and measurements describe permitted processing, while the source model specifies which input resources must be paid for.

**Source pointers.** [Watrous, Sections 2.2–2.3][W]; [model: access assumptions](../science/model.md#known-interaction-menu-and-unknown-sources); [interpretation: copy cost and physical workload](../science/interpretation.md#copy-cost-and-physical-workload).

### M06: Trace norm as distinguishability

**Central question.** Why is trace norm an operational measure of global state separation?

**Understanding target.** Connect the trace norm of a state difference to optimal binary discrimination with known hypotheses. Keep its normalization distinct from half the trace norm, and distinguish this binary discrimination formula from testing equality of two unknown sources.

**Dependencies and story role.** M01 and M05. Give the eventual testing guarantee a physical meaning that includes every possible measurement.

**Conceptual connection.** A matrix norm becomes a limit on decision success; the same connection will turn a mixture-distance bound into a converse.

**Source pointers.** [Watrous, Sections 1.1.3 and 3.1.1][W]; [model: equality versus trace-norm separation](../science/model.md#equality-versus-trace-norm-separation).

### M07: Relative entropy and data processing

**Central question.** How can an entropy comparison constrain an experiment's distinguishability?

**Understanding target.** Explain the order dependence of relative entropy, its monotonicity under quantum channels, and its Pinsker lower bound in trace norm. Translate the base-two entropy convention to the natural-log convention used by the thermal identities.

**Dependencies and story role.** M06. Add the information-theoretic tool that will connect the thermal parameter family to the global testing metric.

**Conceptual connection.** Data processing relates the quantum problem to ordinary measurement probabilities without assuming that its Hamiltonians commute.

**Source pointers.** [Watrous, Section 5.2, especially 5.2.3 and Theorem 5.38][W]; [thermal geometry: relative entropy and global trace norm](../science/thermal-geometry.md#relative-entropy-converts-moments-to-global-trace-norm).

### M08: Covariance and directions of fluctuation

**Central question.** Why is a list of coordinate variances insufficient to describe the noise in many simultaneous estimates?

**Understanding target.** Interpret a covariance matrix through the variance of every real linear combination of coordinates. Explain an operator-norm covariance bound, correlations within one measurement record, and independence between different source copies.

**Dependencies and story role.** M01, M02, and M05. Move from individual observables to the joint fluctuations that determine a high-dimensional test's performance.

**Conceptual connection.** Matrix-norm reasoning controls the noise of the full moment vector, including directions assembled from many interaction terms.

**Source pointers.** [Watrous, Sections 1.1.3 and 1.2][W] for norms and probability foundations; [covariance proof](../science/covariance-bound.md) for the thermal and measured covariance matrices.

### M09: Convexity, log partition functions, and response

**Central question.** What information do derivatives of the log partition function contain?

**Understanding target.** Interpret its gradient as interaction expectations and its Hessian as thermal response. Explain the significance of a uniform positive curvature bound and why a convex coefficient domain permits comparisons along an entire segment.

**Dependencies and story role.** M03 and M08. Organize the equilibrium family into a geometric framework without yet assuming the needed high-temperature theorem.

**Conceptual connection.** Thermodynamic response, covariance, and stability of the parameter-to-moment map become aspects of one derivative calculation.

**Source pointers.** [Watrous, Section 1.2][W] for convexity; [thermal geometry: curvature and the coefficient segment](../science/thermal-geometry.md). The thermal derivative identities and uniform research bound are supplied by the project and HKT.

### M10: Quadratic mean testing and finite-sample inference

**Central question.** How can a decision about equality require less information than estimating every unknown parameter?

**Understanding target.** Explain why a squared aggregate mean displacement is a useful signal, why squaring a noisy sample mean introduces a bias, and how independence can remove that bias. Relate expectation and variance bounds to finite-sample decision errors.

**Dependencies and story role.** M06 and M08. Introduce the statistical mechanism needed to use a whole vector of noisy local data efficiently.

**Conceptual connection.** An unbiased cross-sample product turns a comparison problem into estimation of one scalar, while retaining covariance information about the vector.

**Source pointers.** [Watrous, Section 1.2][W] for probability foundations; [testing algorithm: expectation, variance, and finite-sample guarantee](../science/testing-algorithm.md). The quadratic mean-testing method is an attributed statistical ingredient, not a result supplied by the anchor.

### M11: Commuting models and hidden-parameter mixtures

**Central question.** How can classical distributions provide a rigorous obstruction to a quantum testing task?

**Understanding target.** Explain the distribution represented by a jointly diagonal family, including uninformative degeneracy labels. Distinguish drawing one hidden parameter for all copies from redrawing it independently on each copy, and explain why a mixture can conceal the direction of a discrepancy.

**Dependencies and story role.** M02, M03, M06, and M10. Introduce the form of hard instances needed for a converse against general quantum processing.

**Conceptual connection.** A restricted commuting subfamily can bound the worst-case performance of a larger noncommuting model.

**Source pointers.** [Watrous, Sections 2.1–2.3 and 3.1.1][W] for classical states and discrimination; [collective lower bound, Sections 1 and 3](../science/collective-lower-bound.md). The product-mixture method is supplied by the cited research and local proof.

### M12: Synthesis of the promised comparison problem

**Central question.** What exactly must a successful comparison theorem guarantee?

**Understanding target.** Assemble the common known menu, unknown coefficients in both sources, common temperature, independent-copy access, exact-equality null, global trace-norm alternative, and total copy budget into one promise problem. Separate a uniform minimax statement from performance on a selected pair.

**Dependencies and story role.** M04, M05, M07, M09, M10, and M11. Close the background phase by combining the physical, statistical, and operational objects into the full research question.

**Conceptual connection.** The promised family links local measurements to global state comparison; the resource model gives upper and lower bounds a common meaning.

**Source pointers.** [Model and main result](../science/model.md); [interpretation and limits](../science/interpretation.md). Watrous supplies the foundations identified above; the full problem is defined by this project.

## Phase II: Narrative/innovation

### M13: Uniform high-temperature curvature

**Central question.** Which equilibrium theorem makes every allowed parameter direction observable?

**Understanding target.** Explain the HKT Hessian bounds, their uniformity over the coefficient cube, and the explicit sufficient temperature restriction. Track the source's degree notation and distinguish a conservative sufficient threshold from a sharp physical transition.

**Dependencies and story role.** M04, M09, and M12. Begin the proof with the local response control on which the later signal and noise estimates depend.

**Conceptual connection.** A theorem originally used for Hamiltonian learning supplies geometric information without requiring Hamiltonian reconstruction.

**Source pointers.** [Thermal geometry: the inherited Hessian bound](../science/thermal-geometry.md#the-inherited-hessian-bound), citing HKT v3, Lemma 4.3 and Corollary 4.4; [related work](../references/RELATED_WORK.md). This uniform Gibbs theorem is absent from the Watrous anchor.

### M14: Geometry along the coefficient segment

**Central question.** How does a pointwise curvature bound compare two unknown members of the family?

**Understanding target.** Explain why the straight segment between two allowed coefficient vectors remains admissible. Use the integrated Hessian as one positive matrix relating the coefficient difference to the moment difference, rather than treating unrelated coordinatewise mean-value points as one point.

**Dependencies and story role.** M13. Convert the local derivative theorem into a uniform comparison of arbitrary source pairs.

**Conceptual connection.** Convexity of the parameter domain is the step that extends local thermal response to a global relation inside the promised family.

**Source pointers.** [Thermal geometry: a uniform bound along the coefficient segment](../science/thermal-geometry.md#a-uniform-bound-along-the-coefficient-segment); [Watrous, Section 1.2][W] for the underlying convexity language.

### M15: Global trace separation from local moments

**Central question.** Why must globally separated promised Gibbs states differ in their interaction moments?

**Understanding target.** Combine the exact symmetric-relative-entropy identity with the integrated curvature bound and Pinsker's inequality. Explain the direction of the resulting implication and why it requires both states to belong to the family.

**Dependencies and story role.** M07 and M14. Establish the signal needed by the measured-data test: a global state gap forces an aggregate local-moment gap.

**Conceptual connection.** The Gibbs logarithm converts a global information divergence into interaction expectations, making local data sufficient for this promised decision.

**Source pointers.** [Thermal geometry: relative entropy and global trace norm](../science/thermal-geometry.md#relative-entropy-converts-moments-to-global-trace-norm); [Watrous, Section 5.2.3 and Theorem 5.38][W]; [interpretation: both thermal promises](../science/interpretation.md#why-both-thermal-promises-matter).

### M16: Duhamel covariance and noncommutativity

**Central question.** Why does thermal curvature not directly equal the variance of a measured observable?

**Understanding target.** Distinguish Duhamel covariance, symmetrized thermal covariance, and classical covariance of measurement scores. Explain where noncommutativity enters the differentiated matrix exponential and why identifying these quantities would leave a proof gap.

**Dependencies and story role.** M08, M09, and M13. Begin the noise analysis by identifying the exact covariance controlled by the inherited theorem.

**Conceptual connection.** The same thermal response that controls the signal must be translated carefully before it can control measurement fluctuations.

**Source pointers.** [Thermal geometry: curvature is Duhamel covariance](../science/thermal-geometry.md#curvature-is-duhamel-covariance); [covariance proof: thermal input](../science/covariance-bound.md#setting-and-the-high-temperature-input). This comparison is supplied locally beyond the anchor's operator foundations.

### M17: Harris comparison and local commutators

**Central question.** How can ordinary thermal variance remain bounded when the interactions do not commute?

**Understanding target.** Explain Harris's variance comparison and the role of its double-commutator correction. Show conceptually why only overlapping term triples contribute and why counting them bounds every real combination of the menu observables independently of menu size.

**Dependencies and story role.** M04 and M16. Obtain the ordinary thermal covariance bound needed before analyzing the detector's additional randomness.

**Conceptual connection.** Bounded overlap converts a noncommutative correction into a controlled local combinatorial cost.

**Source pointers.** [Covariance proof: ordinary variance and the local double commutator](../science/covariance-bound.md#from-duhamel-covariance-to-ordinary-variance), including Harris's inequality as normalized by Brankov and Tonchev. This research-level variance comparison is absent from Watrous.

### M18: Simultaneous Pauli score construction

**Central question.** How does one product measurement provide unbiased estimates for every listed interaction?

**Understanding target.** Explain independent random Pauli axes, basis-matching events, products of recorded signs, and the inverse-probability score factor. Distinguish simultaneous estimation from a joint projective measurement of all menu operators.

**Dependencies and story role.** M02, M05, and M08. Specify the actual experimental data whose covariance and sample cost will be analyzed.

**Conceptual connection.** Local measurement records and classical postprocessing provide all moment coordinates without coherent access to the unknown source.

**Source pointers.** [Covariance proof: the measurement vector](../science/covariance-bound.md#the-measurement-vector), citing the standard local Pauli shadow estimator; [Watrous, Section 2.3][W] for measurement foundations.

### M19: Snapshot covariance and sparse overlap

**Central question.** Why does estimating many local observables from the same copy not create uncontrolled collective noise?

**Understanding target.** Compare disjoint, compatibly overlapping, and incompatibly overlapping Pauli pairs. Explain why the difference between snapshot covariance and thermal covariance is confined to the overlap graph, and how an absolute row-sum bound yields the explicit uniform covariance constant.

**Dependencies and story role.** M17–M18. Finish the noise bound for the measured vector, including both state correlations and randomized-basis effects.

**Conceptual connection.** Thermodynamic variance control and sparse detector corrections together bound the fluctuation in every direction of the full observable space.

**Source pointers.** [Covariance proof: measurement vector and final covariance bound](../science/covariance-bound.md#covariance-bound); [Watrous, Section 1.1.3][W] for matrix-norm foundations. The combined snapshot bound is established by the project proof.

### M20: Independent pairs and the unbiased statistic

**Central question.** How can two unknown sources be compared without learning either mean vector?

**Understanding target.** Form independent differences of source score vectors and explain why cross-products from distinct pairs estimate their squared mean displacement without self-noise bias. Account for independent measurement randomness between the two sources and the factor of two in the copy count.

**Dependencies and story role.** M10, M15, and M19. Turn the thermal signal and noise statements into an explicit comparison statistic.

**Conceptual connection.** A standard classical mean test becomes a quantum source-comparison protocol because its required geometric and covariance conditions have now been justified.

**Source pointers.** [Testing algorithm: explicit protocol](../science/testing-algorithm.md#explicit-protocol) and [exact expectation and variance](../science/testing-algorithm.md#exact-expectation-and-variance), with attribution to established quadratic-statistic methods.

### M21: Exact variance and the square-root dimension law

**Central question.** Which variance terms determine the required number of source copies?

**Understanding target.** Separate the statistic's linear fluctuation from its centered pair-product fluctuation and explain why the relevant cross terms vanish. Interpret the covariance-squared trace term and the null variance scaling that leads to the square root of the number of interaction coordinates.

**Dependencies and story role.** M08 and M20. Derive the dimensional sample scale instead of inferring it from separate estimates of individual means.

**Conceptual connection.** Independence between copies removes cross terms, while the within-copy covariance bound controls the surviving aggregate noise.

**Source pointers.** [Testing algorithm: exact expectation and variance](../science/testing-algorithm.md#exact-expectation-and-variance); [Watrous, Section 1.2][W] for probability foundations. The complete finite-sample calculation is supplied in the project.

### M22: Decision threshold and confidence

**Central question.** How do the signal and variance bounds become a uniformly reliable decision rule?

**Understanding target.** Relate the exact-equality null, forced alternative signal, and chosen threshold to the two error probabilities. Explain the explicit conservative sample schedule, the total copies from both sources, and confidence amplification by independent repetitions.

**Dependencies and story role.** M15 and M21. Complete the statistical upper bound for every promised pair, including an unknown common null state.

**Conceptual connection.** Thermal geometry sets the separation threshold; classical concentration converts the measurement-noise bound into a finite-sample guarantee.

**Source pointers.** [Testing algorithm: finite-sample guarantee](../science/testing-algorithm.md#finite-sample-guarantee-with-the-stated-constants) and [confidence amplification](../science/testing-algorithm.md#confidence-amplification); [Watrous, Section 1.2][W] for the underlying probability inequalities.

### M23: Streaming, precision, and total workload

**Central question.** What resources are required to implement the copy-efficient test?

**Understanding target.** Explain the vector and scalar streaming accumulators, exact integer scores, rational threshold comparison, and storage bit lengths. Separate copy count, one-qubit readout, classical work, and source-preparation time; include the explicit menu and its preprocessing.

**Dependencies and story role.** M05, M18, M20, and M22. Close the upper-bound construction with a realizable data-processing account and its physical limits.

**Conceptual connection.** The unbiased statistic has an efficient algebraic form, but a small number of full-register preparations still entails extensive readout and processing.

**Source pointers.** [Testing algorithm: measurement and classical resources](../science/testing-algorithm.md#measurement-and-classical-resources); [interpretation: copy cost and physical workload](../science/interpretation.md#copy-cost-and-physical-workload). These implementation costs are established locally.

### M24: Disjoint supports inside every allowed menu

**Central question.** Where does a hard classical subproblem come from if the menu contains no single-qubit terms?

**Understanding target.** Explain the greedy independent-set selection in the overlap graph and its guaranteed size. Translate disjoint allowed Pauli strings into independent informative eigenvalue labels, including their equal degeneracies and any spectator qubits.

**Dependencies and story role.** M04, M11, and M12. Begin the converse within each fixed allowed menu, rather than replacing it with a specially chosen different menu.

**Conceptual connection.** The same bounded overlap that limits the upper-bound noise guarantees enough independent directions for a worst-case obstruction.

**Source pointers.** [Collective lower bound, Section 1: an admissible product subfamily](../science/collective-lower-bound.md#1-an-admissible-product-subfamily); [Watrous, Section 2.1][W] for state and register foundations.

### M25: Product alternatives inside the coefficient cube

**Central question.** How can many weak discrepancies remain valid thermal instances of the promised model?

**Understanding target.** Explain the random signs, common bias magnitude, inverse-hyperbolic-tangent coefficients, and zero values of unselected terms. Connect the bias scale to the coefficient constraint and identify the resulting relation among accuracy, temperature, and menu size.

**Dependencies and story role.** M03 and M24. Establish admissibility of the hard alternatives before claiming they are separated or statistically difficult.

**Conceptual connection.** The physical energy-scale promise constrains the statistical construction and ultimately restricts the theorem's matching range.

**Source pointers.** [Collective lower bound, Section 1](../science/collective-lower-bound.md#1-an-admissible-product-subfamily); [model: lower-bound range](../science/model.md#theorem-optimal-copy-complexity-with-local-readout). This construction is supplied by the project and its cited product-testing research.

### M26: Fourier norms and trace separation

**Central question.** Why is every fixed sign alternative globally far from the maximally mixed state?

**Understanding target.** Relate the product likelihood displacement to its Boolean Fourier coefficients. Explain how its second moment, Bonami's fourth-moment control, and interpolation produce a lower bound on its first absolute moment and hence on trace separation.

**Dependencies and story role.** M06, M11, and M25. Verify the alternative promise for every member of the hard family, independently of the later mixture calculation.

**Conceptual connection.** A norm comparison prevents the likelihood discrepancy from being concentrated on too little probability mass to yield the claimed global distance.

**Source pointers.** [Collective lower bound, Section 2: trace separation](../science/collective-lower-bound.md#2-every-alternative-has-the-required-trace-separation); [related work: Fourier norm comparison](../references/RELATED_WORK.md#ingredients-used-in-the-proof). Bonami hypercontractivity is a research dependency beyond the Watrous anchor.

### M27: Fixed-sign mixtures and the information bound

**Central question.** How can a collection of individually separated alternatives remain difficult to detect from few copies?

**Understanding target.** Form the mixture by choosing its sign vector once for the entire source. Explain the exact likelihood-ratio second moment across repeated copies, its chi-square bound, and the conversion to small total variation between the mixture and the null.

**Dependencies and story role.** M10, M11, M25, and M26. Establish the quantitative information obstruction at the same sample scale as the upper bound.

**Conceptual connection.** Hidden discrepancy directions suppress the low-order evidence available to a test, even though each underlying state satisfies the alternative promise.

**Source pointers.** [Collective lower bound, Section 3: exact chi-square calculation](../science/collective-lower-bound.md#3-exact-chi-square-calculation-for-repeated-copies); [related work: product lower-bound mechanism](../references/RELATED_WORK.md#ingredients-used-in-the-proof). The mixture technique comes from the cited classical testing literature.

### M28: Collective and adaptive protocol reduction

**Central question.** Why can quantum memory, adaptive source choices, and a joint measurement not evade this converse?

**Understanding target.** Explain the reduction from a deterministic total copy cap to pre-supplied copies of the informative source, while granting the common null source freely. Use common diagonalization and channel contractivity to bound all final decisions, and distinguish a hard mixture from a new per-copy source promise.

**Dependencies and story role.** M05, M06, and M27. Extend the classical information bound to the full class of quantum protocols allowed by the theorem.

**Conceptual connection.** The operational channel description shows that a commuting subfamily can obstruct even processing that is not restricted to classical measurements.

**Source pointers.** [Collective lower bound, Section 4: adaptive and collective measurements](../science/collective-lower-bound.md#4-why-adaptivity-and-collective-measurements-cannot-evade-the-bound); [Watrous, Sections 2.2–2.3 and 3.1.1][W].

### M29: Matching bounds in the supported accuracy range

**Central question.** In which precise sense is the source-comparison rate optimal?

**Understanding target.** Combine the local-measurement upper bound and unrestricted lower bound with their quantifiers and constants. Separate the upper bound's temperature condition from the converse's additional accuracy condition, and state matching minimax scaling only where both apply.

**Dependencies and story role.** M22, M23, and M28. Integrate both proof directions into the project's central theorem.

**Conceptual connection.** An attainable procedure and an information obstruction together identify the resource scale; the nonvacuous parameter range is part of that conclusion.

**Source pointers.** [Model: optimal copy complexity](../science/model.md#theorem-optimal-copy-complexity-with-local-readout); [collective lower bound, Section 5: range and meaning of optimality](../science/collective-lower-bound.md#5-range-and-meaning-of-optimality); [testing algorithm](../science/testing-algorithm.md).

### M30: Synthesis of operational meaning, attribution, and limits

**Central question.** What scientific conclusion survives after accounting for the promises, resources, and inherited ingredients?

**Understanding target.** Explain the optimal global comparison law for two unknown, potentially noncommuting thermal sources on a known bounded-overlap menu. Locate the contribution in the supported combination of established tools and compare its scope with broader Gibbs testing. Use the parity example to explain the arbitrary-state certification boundary, while distinguishing the separate absence of a constant-gap tolerant guarantee.

**Dependencies and story role.** M12, M15, M19, M23, and M29. Close the narrative phase by connecting proof mechanisms to the theorem's physical meaning, limitations, and relation to prior work.

**Conceptual connection.** Local readout, thermal structure, high-dimensional statistics, and a collective converse form one operational account whose copy complexity is distinct from total laboratory workload.

**Source pointers.** [Interpretation and limits](../science/interpretation.md); [related work and attribution](../references/RELATED_WORK.md); [model and main result](../science/model.md); [verification scope](../verification/README.md).

[W]: https://jhwatrous.github.io/TQI.pdf
