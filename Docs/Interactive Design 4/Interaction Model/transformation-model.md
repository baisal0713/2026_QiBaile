# The Transformation Model — How Input Becomes Output

> Design document for the ID4 interaction framework.
> Defines how values travel from input to output in any interactive atom.
> Last updated: March 2026.

---

## What This Document Is

Every interaction in the course follows the same atomic pattern:

**Input → Map → Time → Output**

The **input** is what the system knows about the participant (proximity, gaze, contact, a button press). The **output** is what changes in the world (light, sound, material, particles, fog). This document defines what happens in the middle — the **transformation** — which is where the design lives.

The transformation has two stages: **Map** (how the input value relates to the output value) and **Time** (how the response unfolds temporally). Together they determine the character of the interaction — whether the space feels eager or reluctant, snappy or languid, attentive or indifferent.

A third layer — **Coupling Quality** — sits alongside the technical model as a reflective prompt. It asks: "what does this feel like?" This layer is not implemented in code; it is the critical vocabulary students use to evaluate and discuss their design choices.

---

## How We Got Here

This model evolved through several iterations. Documenting the evolution preserves the reasoning behind each simplification.

### Iteration 1: Shape × Temporality (two independent axes)

The first attempt separated the transformation into two parallel dimensions:

**Mapping shape** (the static curve): linear, inverse, curved/eased, threshold/step, deadzone, quantized/stepped, asymmetric.

**Temporal behavior** (what happens over time): instantaneous, smoothed/damped, one-shot, sustained, accumulated, decaying, rhythmic/oscillating, delayed/latent.

The idea was that every interaction is a point in the matrix of shape × time. This produced ~56 theoretical combinations.

**Problem:** The two axes are not truly independent. In signal processing, the mapping shape and temporal behavior are two views of the same transfer function — they interact, and many combinations are either redundant or incoherent. The matrix was too large to be useful and implied a false orthogonality.

### Iteration 2: Synth analogy — Mapping + ADSR Envelope

Inspired by sound synthesis, the second attempt reframed the transformation as a signal chain:

**Input → Mapping (static curve) → Envelope (ADSR temporal shape) → Output**

The mapping is a pure mathematical function: given input X, what is output Y? No time involved. The envelope (Attack, Decay, Sustain, Release) shapes how that output unfolds temporally — how fast it onsets, whether it overshoots, what happens while sustained, how it releases.

This was cleaner: two sequential stages rather than two parallel axes. The synth analogy provided intuitive grounding — every musical instrument has a mapping (how hard you press → how loud) and an envelope (how the sound attacks, sustains, and releases).

**Advance:** Correctly identified that mapping and time are sequential stages in a chain, not independent dimensions. ADSR is parametric rather than categorical — a small number of continuous parameters generate all temporal behaviors.

**Problem:** ADSR is synthesizer jargon. The four-phase model (Attack, Decay, Sustain, Release) is more detail than students need for designing interactions. The In/During/Out simplification was attempted but still required students to think in terms of phases they wouldn't consciously design at that granularity.

### Iteration 3: Response Curve as central concept

Attempted to collapse the entire transformation into a single concept: the **response curve** — a drawable curve in Unity's AnimationCurve editor. Input on X, output on Y. All mapping types (linear, eased, threshold, inverse) are just different curve shapes.

**Advance:** Visually intuitive. Students can literally draw the relationship. Maps directly to Unity's AnimationCurve inspector.

**Problem:** Only works for continuous mappings. A button press or collision event doesn't have a "curve" — it's a discrete event that triggers a response. Forcing everything into a curve metaphor obscures the fundamental difference between continuous signals and discrete events.

### Iteration 4: Continuous vs. Discrete distinction

Recognized that the mapping stage contains two fundamentally different operations:

- **Continuous input → continuous output:** A flowing value drives another flowing value. The curve is the design.
- **Discrete input → triggered output:** An event fires, a response plays. The curve is irrelevant; the response timing and character are the design.

This distinction is not about the mapping shape — it's about the nature of the signal itself.

### Iteration 5: Three map types (final student-facing model)

Collapsed everything to three perceptually distinct modes that capture the fundamental ways an interaction can feel:

**Continuous, On/Off, One-shot.**

Everything else is a parameter within these three modes. This is the model described below.

---

## The Student-Facing Model

### Input → Map → Output

The transformation is called **Map**. It describes how an input relates to an output. There are three types:

---

### 1. Continuous

The output follows the input value in real time. As the input changes, the output changes with it. The relationship is alive and flowing.

*Walk closer, the pillar gets brighter. Walk away, it dims. Move your hand, the pitch follows.*

**Parameters:**
- **Curve** — the shape of the relationship between input and output. Linear (straight proportional), eased (slow start or slow end), inverse (more input = less output), or any custom shape drawn in an AnimationCurve.
- **Smoothing** — how fast the output tracks the input. Instant (raw, mechanical) to slow (laggy, heavy, contemplative). This is the "feel" of the coupling.

**Continuous is the default for spatial inputs** (proximity, gaze angle, slider position). The participant moves, the world responds in proportion.

---

### 2. On/Off

The output has two states: active and inactive. Something causes it to switch between them. While active, the output holds steady. When deactivated, it returns to its resting state.

*Enter a zone, the light turns on. Leave, it turns off. Step on a tile, sound plays. Step off, it stops.*

**Parameters:**
- **Trigger condition** — what causes the switch. Entering/exiting a zone (proximity threshold), pressing/releasing a button, looking at/away from an object, stepping on/off a surface.
- **Transition speed** — how fast the output moves between its two states. Instant snap (binary, mechanical) to slow fade (gradual, atmospheric). Can be asymmetric: fast turn-on, slow fade-off (or vice versa).

**On/Off is the default for zone-based and contact-based inputs.** The participant crosses a boundary — in or out — and the world responds with a state change.

*Note: Toggle is a variant of On/Off where each input event flips the state rather than holding it. Press once → on. Press again → off. Same model, different trigger condition.*

---

### 3. One-shot

The input triggers a response that plays out on its own and finishes. The participant fires it; the world takes over. It doesn't matter if the participant stays or leaves — the response completes its arc independently.

*Cross a line, a particle burst fires. Pick up an object, a sound sting plays. Collide with something, the screen shakes for half a second.*

**Parameters:**
- **Duration** — how long the response takes to play out.
- **Shape** — how the response unfolds over its duration. A burst (fast attack, quick decay). A swell (slow rise, peak, fade). A snap (instant peak, long tail).

**One-shot is the default for events and collisions.** The participant does something discrete; the world performs a response.

---

### Summary Table

| Map Type | Output behavior | Input type | Key parameters |
|----------|----------------|------------|----------------|
| **Continuous** | Follows input in real time | Flowing value (proximity, slider, gaze angle) | Curve shape, smoothing speed |
| **On/Off** | Switches between two states | Boundary crossing (zone, contact, button) | Trigger condition, transition speed |
| **One-shot** | Plays once, finishes independently | Discrete event (collision, pickup, button press) | Duration, response shape |

---

### Combinations and Layers

Most interesting interactions are **layers of map types on the same object or space:**

- A pillar that glows **continuously** with proximity AND fires a **one-shot** particle burst when you cross a threshold AND **toggles** (on/off) a sound loop when you touch it — three map types, three layers, one object.

- A room where your proximity **continuously** drives fog density, your gaze **on/off** reveals hidden surfaces, and picking up a crystal fires a **one-shot** atmospheric transformation.

The map types compose. They don't need to be chosen exclusively — they stack.

---

## The Detail Layer: ADSR (For Advanced Students)

Underneath the three map types, all temporal behavior can be described by four parameters borrowed from sound synthesis. This is the **engineering model** — not required for day-to-day design, but available when students want precise control.

**Attack** — how fast the response begins. Instant attack feels mechanical, snappy. Slow attack feels gradual, organic, uncertain.

**Decay** — whether the response overshoots its target and settles back. A light that flashes brighter than its resting intensity and then dims to its sustained level has a fast attack and moderate decay. Most interactions have zero decay (they arrive at their target cleanly).

**Sustain** — what happens while the input is active. Hold steady at the mapped value (the default). Slowly accumulate (grow over time). Slowly drain (decay while active). Oscillate (pulse rhythmically).

**Release** — how the response ends when input stops. Instant release feels clinical. Slow release feels lingering, sticky, warm. Very slow release feels like memory — the space holds onto your presence after you've gone.

Every one of the three student-facing map types is a preset of these four parameters:

| Map type | Attack | Decay | Sustain | Release |
|----------|--------|-------|---------|---------|
| **Continuous** | = smoothing speed | none | = tracks input | = smoothing speed |
| **On/Off** | = transition speed (in) | none | holds at target | = transition speed (out) |
| **One-shot** | = response shape (onset) | = response shape (tail) | none (no sustain) | none (plays out independently) |

Asymmetric on/off (fast in, slow out) = fast attack, slow release. A breathing pulse = continuous with oscillating sustain. Accumulated growth = on/off with rising sustain. Every "preset" name from the brainstorming process maps to an ADSR configuration.

---

## The Reflective Layer: Coupling Quality

Alongside the technical model, every interaction invites a phenomenological question: **what does this feel like?**

This is not a parameter. It is a vocabulary for critique and discussion. When students build an interaction and test it, they should ask:

- Is the space **eager** (fast attack, tight tracking, instant response) or **reluctant** (slow attack, heavy smoothing, delayed onset)?
- Is the space **attentive** (continuous, proportional, follows your every move) or **indifferent** (threshold, ignores you until you commit)?
- Is the space **precise** (quantized, snappy, discrete) or **forgiving** (smoothed, eased, continuous)?
- Is the space **sticky** (slow release, lingers after you leave) or **crisp** (instant release, snaps back to neutral)?
- Is the space **alive** (pulsing, oscillating, breathing) or **still** (holds steady, waits)?

These qualities emerge from the technical choices (map type, curve, smoothing, transition speed) but they are experienced holistically. The technical model gives students the tools to build. The coupling quality vocabulary gives them the language to evaluate.

This connects directly to the course's philosophical foundation: *"What does it feel like to be this agent? What does the doing produce in the one who does it?"* The coupling quality is where the technical atom meets the lived experience.

---

## How This Connects to the Course Framework

### Relationship to the Interaction Toolkit Architecture

The toolkit's three layers (Data → Simulation → Presentation) handle the infrastructure. This transformation model describes **what happens inside the Simulation layer** when an input value drives an output component. The map type determines which kind of controller script is needed:

- **Continuous** controllers read a sensor value every frame and interpolate the output.
- **On/Off** controllers subscribe to enter/exit events and tween between two target values.
- **One-shot** controllers respond to an event by playing a timed sequence and stopping.

### Relationship to Statefulness

Statefulness (memory, accumulation, conditional behavior, adaptive mappings) is handled separately in the course through the Variable and Condition systems. The transformation model assumes **stateless mapping** — the same input always produces the same output. When state is introduced (P4: Interaction + State), it modifies either the input (a variable that changes what the sensor reports) or the mapping itself (a condition that switches which map type is active). State wraps around the transformation; it does not live inside it.

### Relationship to the Six Projects

| Project | Primary map types |
|---------|------------------|
| P1 Ecosystem | Continuous (entity parameters driven by simulation values) |
| P2 Presence Room | Continuous (proximity → everything), On/Off (zone transitions) |
| P3 Active Interaction | On/Off (grab/place triggers responses), One-shot (throw impacts, collisions) |
| P4 Interaction + State | All three + statefulness modifying the mappings |
| P5 Narration & Choices | On/Off with branching conditions, One-shot (irreversible events) |
| P6 Progression | All three, layered and sequenced into temporal arcs |

---

## Key References

- **Lim & Stolterman** — Interactivity Attributes (continuity, predictability, response speed, approximativity) — descriptive vocabulary for the felt qualities this model produces
- **Transfer function approach** — from control theory, the mathematical unity underneath mapping + temporal behavior
- **ADSR envelope** — from sound synthesis, the parametric model underneath the three map types
- **AnimationCurve** — Unity's built-in implementation of the response curve, directly usable in the Inspector
- **Easing functions** — from animation (ease-in, ease-out, ease-in-out), the standard vocabulary for curve shapes

---

## Open Questions

- [ ] Should the Interactive Palette showcase scene demonstrate all three map types on every output component, or focus on the most perceptually distinct combinations?
- [ ] How does the continuous map type handle the crossover point where continuous tracking becomes effectively on/off (very steep curve ≈ threshold)?
- [ ] Does the ADSR detail layer need its own reference card, or is it sufficient as a section in this document?
- [ ] Should "pulse/rhythm" be a fourth map type or remain a parameter (continuous with oscillating input)?
