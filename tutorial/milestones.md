# A 30-milestone map of Quantum Gibbs Testing

[Learning route](README.md) · [Watrous bridge](watrous-bridge.md) · [Exact model and theorem](../science/model.md)

This common map follows the scientific problem rather than a reader's previous study. It has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The background phase moves from one state and one measurement to the complete promised comparison problem. The narrative phase develops the geometry, noise control, and statistic, then builds the converse and joins the result. This allocation gives space to both proof mechanisms without turning each technical lemma into a separate milestone.

Every source pointer below refers either to the single anchor, **Watrous, *The Theory of Quantum Information* (2018)**, or to the authoritative project account. Anchor section numbers refer to the author's 2018 manuscript linked and translated in the [bridge](watrous-bridge.md). The map covers the contribution as a connected story; the science pages retain the detailed derivations and research attribution.

## Background and preliminaries: M01–M12

### M01: A source state and one preparation

**Central question.** What does a laboratory supply when it supplies one copy of an unknown state?

**Understanding target.** Distinguish the density operator describing a preparation from a particular measurement outcome, and distinguish independent copies from several subsystems of one copy.

**Dependencies and story role.** No earlier milestone. This is the local physical object from which the whole testing experiment is built.

**Conceptual connection.** Positivity and unit trace make Born probabilities valid; independence determines how repeated input states combine.

**Source pointers.** Watrous Sections 2.1.1–2.1.2; [model: source access](../science/model.md); [single-spin introduction](README.md).

### M02: Pauli operators as interaction coordinates

**Central question.** Why can a known list of Pauli strings label unknown Hamiltonian parameters?

**Understanding target.** Explain a tensor-product Pauli string, its support and weight, and why excluding the identity and duplicate strings removes scalar and coordinate ambiguities.

**Dependencies and story role.** M01. The state is now connected to the elementary operators that specify its thermal family.

**Conceptual connection.** Hermitian observables have measurable expectations; normalized Pauli orthogonality makes the coefficient representation identifiable.

**Source pointers.** Watrous Sections 1.1.2–1.1.3; [model: known interaction menu](../science/model.md); [thermal geometry: conventions](../science/thermal-geometry.md).

### M03: A Born record and an unbiased score

**Central question.** How does a physical measurement become a numerical estimate of an expectation?

**Understanding target.** Separate a measured sign, a measurement probability, a score computed from a record, and the score's ensemble mean.

**Dependencies and story role.** M01–M02. This introduces the observation mechanism before many-coordinate statistics.

**Conceptual connection.** A classical function of a measurement record can correct randomized basis selection while preserving the desired expectation.

**Source pointers.** Watrous Sections 2.3.1–2.3.2; [single-spin score](README.md); [algorithm: score definition](../science/testing-algorithm.md).

### M04: Locality and support overlap

**Central question.** Which features of the interaction list control local counting?

**Understanding target.** Distinguish bounded weight from bounded overlap degree, and distinguish intersecting supports from noncommuting operators.

**Dependencies and story role.** M02. The individual operators now form the graph needed by both upper and lower bounds.

**Conceptual connection.** Each interaction touches few qubits, while each interaction also has few graph neighbors. These restrictions control different costs and estimates.

**Source pointers.** Watrous Section 1.1.2 for tensor operators; [model: overlap graph](../science/model.md); [bridge: Hamiltonian menu](watrous-bridge.md).

### M05: The Gibbs family and its normalization

**Central question.** How do bounded unknown couplings produce a well-defined unknown state?

**Understanding target.** Explain the Hamiltonian sum, positive matrix exponential, partition function, and role of the coefficient cube. Identify which data the tester actually receives.

**Dependencies and story role.** M01–M02, M04. This combines operators into the statistical source family.

**Conceptual connection.** Normalization turns an energy model into a density operator without giving the tester a partition-function oracle or a state description.

**Source pointers.** Watrous Sections 1.1.3 and 2.1.2; [model: Gibbs states and input access](../science/model.md); [thermal geometry: family](../science/thermal-geometry.md).

### M06: Temperature and the energy scale

**Central question.** Why is known positive inverse temperature part of the promise?

**Understanding target.** Explain how beta scales bounded couplings, why beta equal to zero makes the family trivial, and why a sufficient high-temperature condition differs from a sharp physical threshold.

**Dependencies and story role.** M05. This makes the regime of the later uniform estimates intelligible.

**Conceptual connection.** At high temperature individual interaction responses are weak, yet many such signals can combine into a global separation.

**Source pointers.** [Model: temperature and theorem range](../science/model.md); [interpretation: temperature and finite examples](../science/interpretation.md); [single-spin bridge](watrous-bridge.md).

### M07: A promised decision about two unknown sources

**Central question.** What must the tester decide, and on which pairs must it succeed?

**Understanding target.** State exact equality versus unhalved trace-norm separation, the two source promises, the common known temperature, and the total-copy success requirement. Explain the unspecified intermediate cases.

**Dependencies and story role.** M01, M05–M06. This is the operational task to which every later bound refers.

**Conceptual connection.** Composite testing differs from discriminating two fully described states and from reconstructing either source.

**Source pointers.** Watrous Section 3.1.1; [model: equality versus separation](../science/model.md); [bridge: convention translation](watrous-bridge.md).

### M08: Observable moments as a smaller description

**Central question.** What information does the interaction-moment vector retain?

**Understanding target.** Identify one expectation per supplied menu term and distinguish this M-component vector from the full exponentially large density matrix or the list of unknown couplings.

**Dependencies and story role.** M02–M03, M05. This introduces the data representation on which the test operates.

**Conceptual connection.** The Gibbs promise can make a selected collection of local moments globally informative, although the same claim fails for unrestricted states.

**Source pointers.** Watrous Sections 2.1.2 and 2.3.1; [thermal geometry: observable vector](../science/thermal-geometry.md); [interpretation: global comparison](../science/interpretation.md).

### M09: Vector noise and covariance

**Central question.** Why is controlling each score separately insufficient?

**Understanding target.** Explain covariance between score coordinates, covariance in an arbitrary real direction, and the difference between an operator bound and a bound on the sum of coordinate variances.

**Dependencies and story role.** M03, M08. This supplies the noise language needed by the quadratic test.

**Conceptual connection.** Uniform directional control can keep the noise constant independent of M even though total variance grows with M.

**Source pointers.** Watrous Sections 1.1.3 and 1.2.2; [measurement covariance](../science/covariance-bound.md); [algorithm: paired-score covariance](../science/testing-algorithm.md).

### M10: Trace norm as operational distinguishability

**Central question.** Why is a global trace-norm promise meaningful to an experiment?

**Understanding target.** Relate the unhalved trace norm to optimal equal-prior binary discrimination, and translate the factor of one half used in classical total variation.

**Dependencies and story role.** M01, M03, M07. This connects the task's mathematical separation to a decision advantage.

**Conceptual connection.** A distance on input states bounds every possible measurement's output distinguishability, providing the language for a collective converse.

**Source pointers.** Watrous Sections 1.1.3 and 3.1.1, Theorem 3.4; [bridge: conventions](watrous-bridge.md); [lower bound: collective processing](../science/collective-lower-bound.md).

### M11: Relative entropy and information loss

**Central question.** How can relative entropy help control a trace-norm gap?

**Understanding target.** Distinguish directed relative entropy from its symmetric sum, translate bits to natural-log units, and explain the roles of data processing and Pinsker's inequality.

**Dependencies and story role.** M05, M10. This prepares the information-theoretic link between thermal parameters and observable signal.

**Conceptual connection.** Gibbs logarithms make relative entropy explicitly calculable in terms of parameters and moments; Pinsker turns that identity into operational separation control.

**Source pointers.** Watrous Sections 5.1.1–5.1.2 and 5.2.1–5.2.3, Theorems 5.35 and 5.38; [thermal geometry: relative entropy](../science/thermal-geometry.md); [bridge](watrous-bridge.md).

### M12: The complete framework and its resources

**Central question.** What must be combined to compare two unknown thermal sources efficiently?

**Understanding target.** Assemble the family promise, global decision gap, local moment records, noise, and resource model. Explain why a copy advantage is distinct from a preparation-time or total-work advantage.

**Dependencies and story role.** M01–M11. This integrates the background phase into one operational problem.

**Conceptual connection.** The upcoming proof must show a sufficient local signal, manageable measurement noise, a sound statistic, and an unrestricted lower bound for the same promised task.

**Source pointers.** [Model: theorem and resource table](../science/model.md); [interpretation: costs and limits](../science/interpretation.md); [bridge: whole argument](watrous-bridge.md).

## Narrative and innovation: M13–M30

### M13: Curvature of the thermal family

**Central question.** What does the log partition function reveal about the moment map?

**Understanding target.** Explain its gradient and Hessian, the Duhamel-covariance identity, and what uniform upper and lower Hessian bounds say about the family's response to coupling changes.

**Dependencies and story role.** M05–M06, M08–M09. This begins the proof with the local response of the thermal model.

**Conceptual connection.** The imported Haah–Kothari–Tang theorem supplies a quantitative curvature window; the project uses its two sides for separation and noise control.

**Source pointers.** Watrous Section 1.2.1 for differentiation and convexity; [thermal geometry: inherited Hessian bound](../science/thermal-geometry.md); [Related work](../references/RELATED_WORK.md).

### M14: From local curvature to a pairwise comparison

**Central question.** How does a derivative estimate compare two arbitrary admissible sources?

**Understanding target.** Explain integration along the coefficient segment and why one symmetric positive matrix relates the coefficient and moment differences.

**Dependencies and story role.** M13. This joins the local response into a statement uniform over the whole coefficient cube.

**Conceptual connection.** Convexity keeps every point on the segment admissible; matrix integration avoids assuming that coordinatewise mean-value points coincide.

**Source pointers.** Watrous Section 1.2.1; [thermal geometry: segment argument](../science/thermal-geometry.md).

### M15: Global trace separation becomes moment signal

**Central question.** Why must globally different promised states have separated local moment vectors?

**Understanding target.** Follow cancellation of partition functions in symmetric relative entropy, combine curvature with Pinsker, and identify the squared moment gap that the test must detect.

**Dependencies and story role.** M10–M11, M14. This completes the upper bound's signal argument.

**Conceptual connection.** The Gibbs logarithm relates an operational state distance to the measured coordinate vector, using both source promises.

**Source pointers.** Watrous Section 5.2.3, Theorem 5.38 with the log conversion in the [bridge](watrous-bridge.md); [thermal geometry: separation inequality](../science/thermal-geometry.md).

### M16: Duhamel fluctuations versus ordinary variance

**Central question.** Why does the Hessian bound not immediately control measured noise?

**Understanding target.** Distinguish the matrix-exponential derivative's Duhamel covariance from the ordinary variance of a Hermitian observable. Explain when commuting operators make them agree.

**Dependencies and story role.** M09, M13. This identifies the noncommuting step that the noise proof must supply.

**Conceptual connection.** Thermal sensitivity and measurement fluctuations are related objects, yet their equivalence needs an argument in the interacting quantum case.

**Source pointers.** [Thermal geometry: Duhamel covariance](../science/thermal-geometry.md); [covariance proof: Harris comparison](../science/covariance-bound.md); [interpretation](../science/interpretation.md).

### M17: A local correction controls ordinary fluctuations

**Central question.** How does bounded support overlap control the noncommuting correction?

**Understanding target.** Explain the Harris inequality's double-commutator term, why only overlapping triples contribute, and how graph counting bounds that term in a real coefficient direction.

**Dependencies and story role.** M04, M13, M16. This converts thermal curvature into the ordinary variance estimate required for measurement analysis.

**Conceptual connection.** Local operator algebra and sparse overlap replace a bound depending on the full register dimension.

**Source pointers.** Watrous Section 1.1.3 for operator norm inequalities; [covariance proof: double commutator and counting](../science/covariance-bound.md); [verification](../verification/README.md).

### M18: One local readout estimates every menu term

**Central question.** How can independent one-qubit measurements supply a whole moment vector?

**Understanding target.** Derive the randomized Pauli score from its axis-match probability and Born sign expectation, and explain why only the known supports need to be processed.

**Dependencies and story role.** M02–M04, M08. This supplies the explicit physical detector for the sufficient statistic.

**Conceptual connection.** One record contributes to many compatible coordinates, with inverse-probability weighting rather than separate experiments for every term.

**Source pointers.** Watrous Sections 2.3.1–2.3.2; [covariance proof: local scores](../science/covariance-bound.md); [algorithm: score definition](../science/testing-algorithm.md).

### M19: Snapshot covariance remains bounded

**Central question.** Why does estimating all moments together not introduce uncontrolled directional noise?

**Understanding target.** Distinguish the state's ordinary covariance from the extra randomized measurement covariance, and explain how bounded locality and overlap give an M-independent operator bound.

**Dependencies and story role.** M09, M17–M18. This completes the upper bound's noise input.

**Conceptual connection.** The thermal fluctuation estimate and the local measurement correction combine into a covariance guarantee for actual score vectors.

**Source pointers.** [Covariance proof: snapshot correction and final bound](../science/covariance-bound.md); [algorithm: conservative covariance majorant](../science/testing-algorithm.md).

### M20: Pairing the two sources

**Central question.** How can an unknown-versus-unknown test be expressed as one mean problem?

**Understanding target.** Form the difference of independent scores, identify its mean and covariance, and explain why the protocol uses independent axes between the two sources.

**Dependencies and story role.** M07, M15, M19. This aligns the physical records with a standard statistical object.

**Conceptual connection.** Equality becomes zero mean; the far promise becomes a lower bound on the squared mean, with controlled covariance for the paired sample.

**Source pointers.** Watrous Section 1.2.2; [algorithm: paired scores and hypotheses](../science/testing-algorithm.md).

### M21: Removing self-noise with cross-products

**Central question.** Why use a quadratic statistic between different preparations?

**Understanding target.** Explain the bias in squaring a noisy empirical vector and why cross-products from distinct independent paired samples estimate the squared mean without that self-noise.

**Dependencies and story role.** M09, M20. This introduces the detector's decisive statistic.

**Conceptual connection.** Detecting an aggregate squared discrepancy can require fewer samples than reconstructing every parameter accurately.

**Source pointers.** [Algorithm: U-statistic protocol and expectation](../science/testing-algorithm.md); [bridge: mean-testing mechanism](watrous-bridge.md); [Related work: statistical ingredients](../references/RELATED_WORK.md).

### M22: Null noise and signal-dependent variance

**Central question.** Which terms determine the statistic's finite-sample uncertainty?

**Understanding target.** Follow the centered decomposition, identify the linear signal-dependent term and degenerate quadratic term, and explain why different unordered pairs are uncorrelated even if one sample index is shared.

**Dependencies and story role.** M09, M21. This turns unbiasedness into a controlled testing error.

**Conceptual connection.** Under the null only the quadratic noise survives, giving variance proportional to M divided by the sample count squared.

**Source pointers.** Watrous Section 1.2.2; [algorithm: exact variance proof](../science/testing-algorithm.md); [verification: finite U-statistic checks](../verification/README.md).

### M23: The square-root copy rate

**Central question.** How do the signal and variance yield a valid equality test?

**Understanding target.** Explain the threshold between zero and the forced far-case signal, the finite-sample probability bound, and the resulting order square root M over epsilon squared for total copies.

**Dependencies and story role.** M15, M19–M22. This integrates the sufficient signal, detector, and noise proof into the upper theorem.

**Conceptual connection.** The null standard deviation scales as square root M over N, while the relevant squared signal scales as epsilon squared.

**Source pointers.** [Algorithm: explicit sample choice and error bounds](../science/testing-algorithm.md); [model: upper bound](../science/model.md).

### M24: Confidence and implementation costs

**Central question.** What does the proven test require beyond its leading copy rate?

**Understanding target.** Explain independent-run confidence amplification, streaming vector/scalar accumulation, per-copy readout, processing workload, and O(M) working-word storage, including the growth of integer bit lengths.

**Dependencies and story role.** M18, M21, M23. This finishes the constructive side as a physical and classical procedure.

**Conceptual connection.** A local detector with no retained quantum memory still incurs state preparation and classical work; confidence and implementation are separate from minimax scaling.

**Source pointers.** [Algorithm: resources and confidence](../science/testing-algorithm.md); [model: resource table](../science/model.md); [interpretation: physical workload](../science/interpretation.md).

### M25: A hard product family inside every menu

**Central question.** How can a lower bound apply to each fixed permitted interaction list?

**Understanding target.** Explain the greedy disjoint-support selection, construct its weakly biased Gibbs states, and account for uniform eigenvalue degeneracy even when strings have different weights.

**Dependencies and story role.** M02, M04–M06. This starts the converse from a local subfamily inside the same promised model.

**Conceptual connection.** Bounded overlap guarantees many independent effective signs; a difficult commuting subfamily is enough to constrain the full quantum family.

**Source pointers.** Watrous Sections 1.1.3 and 2.1.2; [lower bound: admissible product subfamily](../science/collective-lower-bound.md).

### M26: Every hard alternative has the required gap

**Central question.** Why are the lower-bound inputs genuinely far from the null?

**Understanding target.** Explain the likelihood-ratio displacement, its moment comparison, and how hypercontractivity and interpolation produce trace separation for every fixed sign vector while keeping the couplings admissible.

**Dependencies and story role.** M06, M10, M25. This validates the alternatives before using an information bound.

**Conceptual connection.** A difficult mixture is useful only when its components are valid promised alternatives; the separation and coefficient-range estimates supply that link.

**Source pointers.** [Lower bound: fixed-alternative separation](../science/collective-lower-bound.md); [Related work: product-testing and Bonami ingredients](../references/RELATED_WORK.md).

### M27: One hidden source over repeated preparations

**Central question.** Why must the unknown sign vector stay fixed over all copies?

**Understanding target.** Distinguish a mixture of repeated-copy distributions from repeated copies of a one-copy mixture, and explain the chi-square second-moment calculation that limits distinguishability.

**Dependencies and story role.** M01, M25–M26. This combines the valid hard alternatives into a statistical obstruction.

**Conceptual connection.** Repeated observations can gradually reveal a persistent hidden parameter; resampling it on every preparation erases the experiment being lower-bounded.

**Source pointers.** Watrous Section 1.2.2 for probability foundations; [lower bound: repeated-copy mixture](../science/collective-lower-bound.md); [verification: mixture algebra](../verification/README.md).

### M28: Why collective measurements and adaptivity do not help

**Central question.** How does a classical mixture obstruction constrain unrestricted quantum testers?

**Understanding target.** Explain pre-supplying the deterministic cap of unknown-source copies, granting the common maximally mixed source for free, and reducing all adaptive processing to a channel. Relate common-basis readout to the input trace norm.

**Dependencies and story role.** M07, M10, M27. This completes the converse for the full quantum access model.

**Conceptual connection.** Giving a protocol more resources makes the lower-bound task easier, yet data processing still bounds its final distinguishability by that of the hard inputs.

**Source pointers.** Watrous Sections 2.2.1–2.2.2 and 3.1.1; [lower bound: collective and adaptive reduction](../science/collective-lower-bound.md); [bridge](watrous-bridge.md).

### M29: The exact domain of matched optimality

**Central question.** Where do the constructive and converse statements match?

**Understanding target.** Combine the high-temperature upper bound with the lower bound's epsilon/beta/M range, distinguish fixed parameters from asymptotic scaling, and explain why empty alternatives or beta equal to zero cannot support an extrapolated converse.

**Dependencies and story role.** M06, M23–M24, M26–M28. This joins both proof directions into the precise theorem.

**Conceptual connection.** The matched law is about copies for a nonvacuous promised decision problem; temperature, separation, and menu size determine when its lower-bound construction fits.

**Source pointers.** [Model: matched theorem and regime](../science/model.md); [lower bound: range of optimality](../science/collective-lower-bound.md); [interpretation](../science/interpretation.md).

### M30: The complete contribution and its boundaries

**Central question.** What does optimal local comparison establish, and which changes create a different problem?

**Understanding target.** Explain the whole signal–noise–statistic–converse chain; distinguish inherited tools from their role in this theorem; use the non-Gibbs parity example, unknown-menu distinction, and resource account to delimit the conclusion. Explain what the finite checks validate.

**Dependencies and story role.** M12–M29. This is the global synthesis of the narrative phase and the project.

**Conceptual connection.** Two promised interacting thermal sources can be compared optimally from local data, while arbitrary-state certification, unknown interaction menus, tolerant global testing, and broader temperature claims require separate arguments.

**Source pointers.** [Model](../science/model.md); [interpretation](../science/interpretation.md); [Related work](../references/RELATED_WORK.md); [verification](../verification/README.md); [Watrous bridge](watrous-bridge.md).
