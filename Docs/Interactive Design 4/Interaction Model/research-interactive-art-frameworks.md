# Research Notes — Interactive Art Frameworks and Interaction Taxonomies

> Reference document collecting relevant academic work on how interaction is modeled, classified, and evaluated in interactive art and interaction design.
> Compiled during the development of the ID4 transformation model, March 2026.

---

## 1. Lim & Stolterman — Interactivity Attributes

**Papers:**
- Lim, Y., Stolterman, E., & Tenenberg, J. (2008). "The Anatomy of Prototypes." *ACM Transactions on Computer-Human Interaction.*
- Lim, Y., Lee, S., & Kim, D. (2011). "Interactivity Attributes: A New Way of Thinking and Describing Interactivity." *Proc. CHI 2011.*
- Lim, Y., Stolterman, E., Jung, H., & Donaldson, J. (2007). "Interaction Gestalt and the Design of Aesthetic Interactions." *Proc. DPPI 2007.*
- Lim, Y. (2012). "Interactivity Attributes for Expression-Oriented Interaction Design." *International Journal of Design, 6(1).*

**Core contribution:** Seven attributes that describe the *felt quality* of interactivity — the invisible shape of how an interaction feels, independent of what it looks like or what technology powers it.

### The Seven Attributes

| Attribute | Describes | Poles |
|-----------|-----------|-------|
| **Concurrency** | Can input and output happen at the same time? | Concurrent ↔ Sequential |
| **Continuity** | Is the interaction a sustained flow or discrete episodes? | Continuous ↔ Discrete |
| **Predictability** | Can the participant anticipate what will happen? | Predictable ↔ Unpredictable |
| **Movement range** | How wide is the space of possible action? | Wide ↔ Narrow |
| **Movement speed** | How fast must the participant act? | Fast ↔ Slow |
| **Approximativity** | How forgiving is the system of imprecise input? | Approximate ↔ Precise |
| **Response speed** | How fast does the system respond? | Prompt ↔ Delayed |

### Key finding: Two perceptual clusters

The research found that these attributes cluster into two felt qualities:

- **Natural / sympathetic:** sequential, continuous, unpredictable, wide range, slow, approximate, delayed response
- **Hard / artificial:** concurrent, discrete, predictable, narrow range, fast, precise, prompt response

This suggests that the "feel" of an interaction is not determined by any single attribute but by the *gestalt* — the overall pattern across all seven dimensions.

### Relevance to the transformation model

The transformation model's three map types (continuous, on/off, one-shot) primarily capture **continuity** and **response speed**. The other five attributes (concurrency, predictability, movement range, movement speed, approximativity) are not directly encoded in the model — they describe properties of the *dialogue* between participant and system that emerge from the full interaction design, not just the transformation.

The coupling quality vocabulary in the transformation model is an attempt to recover some of this territory through reflective prompts rather than formal parameters: "Is the space forgiving or precise?" (approximativity), "Is the space eager or reluctant?" (response speed + predictability).

**What the model captures that Lim doesn't:** The specific mathematical/parametric structure of the mapping — curve shapes, ADSR envelopes, smoothing rates. Lim's framework is descriptive (what does it feel like?), not constructive (how do I build it?).

**What Lim captures that the model doesn't:** Movement range, movement speed, and approximativity — properties of the participant's action space that are not about the system's response. These matter for interaction design but are input-side concerns, not transformation concerns.

---

## 2. Edmonds & Cornock — Interactive Art Systems Taxonomy

**Papers:**
- Cornock, S. & Edmonds, E. (1973). "The Creative Process Where the Artist Is Amplified or Superseded by the Computer." *Leonardo, 6(1).*
- Edmonds, E. (2004). "Approaches to Interactive Art Systems." *Proc. GRAPHITE 2004.*
- Edmonds, E. (2010). "Art, Interaction and Engagement." *Proc. OzCHI 2010.*
- Edmonds, E. (2011). "Revisiting Interactive Art Systems." *Proc. C&C 2011.*

**Core contribution:** The foundational taxonomy for classifying art systems by their relationship between artwork and audience. Proposed in 1973 and refined over four decades.

### The Four Categories

| Category | Description |
|----------|-------------|
| **Static** | The work does not change. Painting, sculpture. |
| **Dynamic-Passive** | The work changes on its own but is not influenced by the audience. Kinetic sculpture, generative video. |
| **Dynamic-Interactive** | The work changes in response to audience actions. The core category for interactive art. |
| **Dynamic-Interactive (Varying)** | The work's response itself changes over time — the mapping evolves, the system adapts or learns. |

### Key insight: From reactive to adaptive

The most important distinction for the ID4 course is between the third and fourth categories. A **reactive** system always responds the same way to the same input. An **adaptive** system changes its response based on history — it learns, evolves, remembers.

In the transformation model's terms: reactive = stateless mapping. Adaptive = stateful mapping (the map itself changes based on accumulated state). This maps directly to the course's separation of transformation (stateless, handled by the map types) and statefulness (handled separately through Variables and Conditions, introduced in P4).

### Edmonds' broader framework

Edmonds later proposed thinking in terms of "art systems" rather than "artworks" — the system includes the artist, the artifact, AND the audience. The role of the artist is not to construct the artifact but to "specify and modify the constraints and rules used to govern the relationship between audience and artwork as it takes place in the world."

This resonates strongly with Nguyen's framework (the designer sculpts the possibility space, the participant navigates it) and with the course's thesis (agency as art — the interaction IS the creative material).

---

## 3. Löwgren — Interaction Aesthetics and Pliability

**Papers:**
- Löwgren, J. (2007). "Pliability as an Experiential Quality." *Artifact, 1(2).*
- Löwgren, J. (2009). "Toward an Articulation of Interaction Esthetics." *New Media & Society, 11(2).*

**Core contribution:** Identified **pliability** as a key aesthetic quality of interaction — the felt sense of tight, responsive coupling between the participant's action and the system's response.

### Pliability

A pliable interaction feels "alive" — small inputs produce proportional, immediate responses. The participant feels that the system is listening, tracking, following. Pliability is the positive experience of tight coupling.

Pliability emerges from the combination of:
- Continuous mapping (not threshold or binary)
- Low latency (fast response)
- Proportional response (small input → small output, large input → large output)
- Smooth interpolation (no jitter, no quantization)

In the transformation model: a **continuous** map type with a **linear or eased curve** and **fast smoothing** produces maximum pliability. A **threshold** or **on/off** map type reduces pliability because the response is discontinuous.

### Pliability is not always the goal

This is an important nuance. Löwgren identifies pliability as an aesthetic quality, not as an optimization target. A *lack* of pliability — resistance, delay, discontinuity — can be equally expressive. A space that refuses to respond until you commit (threshold) or that responds only after a delay creates a different quality of agency. The question is always: what does the designer intend?

### Rhythm as aesthetic quality

Löwgren also identifies **rhythm** as a designable quality of interaction — the temporal pattern of action and response. Not just "how fast" but "what pattern over time." A rhythmic interaction creates a sense of partnership between participant and system. This connects to the transformation model's note that pulse/rhythm can be achieved by using time as a continuous input driving any map type.

---

## 4. Usman Haque — Responsive Environments and Cybernetics

**Papers / Sources:**
- Haque, U. (2006). "Architecture, Interaction, Systems." *AU: Arquitetura & Urbanismo.*
- Haque, U. — various writings on Pachube (now Xively), responsive architecture, and the Open Source Architecture manifesto.
- Background: Gordon Pask's *Conversation Theory* as applied to architectural systems.

**Core contribution:** Distinguished between **reactive** and **conversational** systems in responsive architecture. Drew on cybernetics (Gordon Pask) to argue that meaningful interaction requires circular causality — the system and participant co-evolve, not just stimulus→response.

### Linear causal response vs. circular mutual reaction

**Linear:** Participant does X → system responds Y. One direction. The system is a mirror or a tool.

**Circular:** Participant does X → system responds Y → participant perceives Y and adjusts → system adjusts in turn → and so on. The system and participant are in dialogue. Neither fully controls the other.

Haque argues that most "interactive" installations are actually **reactive** (linear) — they respond but do not converse. True interactivity requires the second model: circular, mutual, evolving.

### Relevance to the transformation model

The three map types (continuous, on/off, one-shot) are all **reactive** — they describe the system's response to input. Circular/conversational interaction emerges when:
- The output feeds back as input (the system's response changes the participant's behavior, which changes the input, which changes the response)
- The mapping itself changes over time (adaptive behavior — Edmonds' fourth category)

Both of these are handled outside the transformation model: feedback through the composition of multiple interaction atoms, adaptivity through the statefulness system. But Haque's insight is worth preserving: **the transformation model describes atoms of reaction. Conversation emerges from the composition of atoms.**

---

## 5. Kwastek — Aesthetics of Interaction in Interactive Art

**Source:**
- Kwastek, K. (2006). "Research Project: A Taxonomy of Interactive Art." Working paper.
- Kwastek, K. (2013). *Aesthetics of Interaction in Digital Art.* MIT Press.

**Core contribution:** Proposed a taxonomy specifically for interactive art that foregrounds the *aesthetic experience* of interaction rather than the technical mechanism. Argues that interactive art should be analyzed through the lens of what the participant experiences, not what the technology does.

### Key distinction: Interaction as aesthetic process

Kwastek distinguishes between:
- **Instrumental interaction** — the participant uses the system as a tool to achieve a goal (UI design, productivity software)
- **Aesthetic interaction** — the interaction itself is the experience; there is no goal beyond the doing

This distinction maps directly to the ID4 course philosophy. The course teaches aesthetic interaction — the Irreducibility Principle ("could this experience be replaced by a video?") is Kwastek's distinction in operational form.

---

## 6. The "Inflation of Interactivity" Paper (2024)

**Paper:**
- Chen et al. (2024). "Inflation of Interactivity? Analyzing and Understanding Embodied Interaction in Interactive Art through a New Three-dimensional Model." *arXiv:2409.00047.*

**Core contribution:** Proposes a three-dimensional model for analyzing embodied interaction in interactive art:
1. **Sensory dimension** — what sensory channels are engaged (visual, auditory, haptic, proprioceptive)
2. **Motor dimension** — what physical actions are required (gesture, locomotion, manipulation, gaze)
3. **Cognitive dimension** — what mental engagement is required (perception, decision, memory, imagination)

### Relevance

This model operates at a higher level than the transformation model — it describes the full interaction experience, not just the input→output transformation. But it highlights a gap: the transformation model is **agnostic about sensory modality**. The same continuous map driving light intensity versus driving sound pitch will feel very different, because the sensory channel shapes the experience. The model doesn't encode this — it treats output as a generic "component" without distinguishing perceptual weight.

For the course, this gap is addressed through the Interactive Palette: students experience the same map type across different output components and *feel* the difference. The palette teaches sensory modality through the body, not through parameters.

---

## 7. Nguyen — Games: Agency as Art (2020)

Already documented in `why-agency-art.md`. Key points relevant to this research:

- Agency is designed through **goals, abilities, and constraints**
- The transformation model's map types and parameters are **implementations of constraints** — they determine what the participant can and cannot accomplish through their actions
- Constraints are not obstacles to agency; they are the medium through which agency acquires character
- A threshold is not a "worse" interaction than a continuous mapping — it is a different quality of constraint, producing a different experience of agency

---

## Summary: What Each Framework Contributes

| Framework | Level | Contribution | Gap |
|-----------|-------|-------------|-----|
| **Lim & Stolterman** | Perceptual | Vocabulary for felt qualities of interaction | Not constructive — can't build from it |
| **Edmonds & Cornock** | Systemic | Reactive vs. adaptive classification | Too coarse for design decisions |
| **Löwgren** | Aesthetic | Pliability and rhythm as designable qualities | Doesn't formalize the parameters |
| **Haque / Pask** | Cybernetic | Reactive vs. conversational distinction | Philosophical, not implementable directly |
| **Kwastek** | Critical | Aesthetic vs. instrumental interaction | Analytical, not constructive |
| **Chen et al.** | Experiential | Sensory, motor, cognitive dimensions | High-level, doesn't address transformation |
| **Nguyen** | Philosophical | Agency as art, constraints as medium | Doesn't address implementation |
| **ID4 Transformation Model** | Implementation | Constructive: map types, parameters, ADSR | Doesn't capture dialogue-level qualities |

The transformation model fills a gap none of these frameworks address: a **constructive, parametric model** that non-programmers can use to build specific interactions with specific felt qualities. It trades theoretical completeness for practical utility. The other frameworks provide the critical vocabulary to evaluate what the model produces.
