# The Transformation Model v2 — How Input Becomes Output

> Design document for the ID4 interaction framework.
> Defines how values travel from input to output in any interactive atom.
> Supersedes transformation-model.md (v1).
> Last updated: March 2026.

---

## Core Statement

Every interaction is a relationship between an input and an output.

The atomic pattern is:

**Input (Signal) → Relationship → Output**

The input is what the system knows about the participant. The output is what changes in the world. The relationship is where the design lives — it determines whether the space feels eager or reluctant, attentive or indifferent, alive or still.

---

## Signal

The input provides a signal — a value arriving from a sensor, a UI element, time, or another system.

There are two signal types:

**Continuous** — a flowing value that changes over time. Distance to an object, angle of gaze, position of a slider, elapsed seconds. The signal has magnitude and variation.

**Binary** — a state with two values. Inside or outside a zone, pressing or not pressing a button, looking or not looking at an object. The signal has no in-between — it is one or the other.

Every sensor in the framework already produces one of these two signal types. The signal type is a property of the input, not of the relationship — it is determined by the sensor before the relationship ever sees it. It is presented here, between input and relationship, because this is where the design decision becomes visible: the relationship responds differently depending on which kind of signal arrives.

---

## Relationship

The relationship defines how the input affects the output over time. There are two fundamental types.

### Bound (dependent)

The output is bound to the input — it depends on it continuously. As the input changes, the output changes with it. If the input stops changing, the output holds where it is. If the input disappears, the output returns to rest. The relationship is alive for as long as the input is present.

A bound relationship works with both signal types:

- **Continuous signal + Bound** — the output tracks a flowing value. Walk closer, the light brightens. Walk away, it dims. The classic proportional response.
- **Binary signal + Bound** — the output switches between two states. Enter a zone, the light turns on. Leave, it turns off. The transition between states can be instant or gradual — that's a question of envelope, not of relationship type.

Bound is the most common relationship in spatial interaction. Presence drives response. The participant moves, the world follows.

*The system follows you.*

### Unbound (independent)

The output is unbound from the input — it runs independently. The input starts a response, but once triggered, the output evolves on its own. It no longer depends on whether the input continues, changes, or disappears. The response plays through its shape and finishes.

- A button press triggers a light that swells up and fades over three seconds.
- A collision fires a particle burst that dissipates.
- Crossing a threshold launches a sound sting that plays to completion.

The input sets the output in motion; the connection is then severed. The participant acts; the world takes over.

*The system continues on its own.*

### Why Two and Not Three

The previous model (v1) used three categories: Continuous, On/Off, and One-shot. This was mixing two independent dimensions. "Continuous" and "On/Off" are both bound — the output depends on the input — but they differ in signal type (continuous vs. binary). "One-shot" is genuinely different because the output becomes independent of the input. The revised model separates signal type from relationship type, making the structure visible:

|  | Bound | Unbound |
|---|---|---|
| **Continuous signal** | proximity → light intensity | threshold crossing → particle swell |
| **Binary signal** | inside zone → light ON | button press → burst |

Two dimensions, two values each. Everything the three-type model could express, with fewer categories and clearer reasoning about why interactions feel different from each other.

Note: "bound" and "unbound" can also be thought of as "continuous" and "discrete" relationships — the output is either continuously coupled to the input or discretely triggered and then free. The dependent/independent framing is preferred because it describes the felt quality of the relationship, not just its technical behavior.

---

## Condition

A relationship may be gated by conditions — rules that determine when it is active.

**Unconditional** — the relationship is always active. Proximity always drives the light. This is the default.

**Conditional** — the relationship only activates when specific rules are satisfied. The light only responds to proximity when a variable is true, or when the participant is also looking at the object, or after a delay.

Conditions modify *when* a relationship applies. They do not change *what type* it is. A binding gated by a condition is still a binding — it simply has a narrower window of activation.

Conditions connect directly to the framework's Variable and Condition systems. They are the bridge between the stateless transformation model and the stateful world.

---

## Curve, Range, Envelope

Every relationship has a shape — the specific character of how input becomes output. This shape is defined by three things.

### Curve

The curve defines the *form* of the transformation. It is the core design surface.

In a **bound** relationship, the curve maps input to output. The X axis is the input value; the Y axis is the output value. A linear curve means proportional response. An eased curve means slow start and fast finish (or the reverse). An inverse curve means more input produces less output. A stepped curve means the output jumps at thresholds. The student draws the relationship.

In an **unbound** relationship, the curve maps time to output. The X axis is elapsed time; the Y axis is the output value over the duration of the response. A spike is a burst. A slow rise and fall is a swell. A sharp onset with a long tail is lightning and afterglow. The student draws the temporal shape.

This is the same tool in Unity — an AnimationCurve in the inspector — but it means something different depending on the relationship type. In a bound relationship, the curve answers "given this input, what should the output be?" In an unbound relationship, the curve answers "as time passes, what should the output do?"

This distinction is a teaching moment, not a technical complication. One tool, two meanings: *where* vs. *when*.

### Range

Range defines the boundaries of the transformation — how much of the input matters and how far the output reaches.

**Input range** — the portion of the input signal that the curve operates on. A proximity sensor might report 0 to 20 meters, but the interaction only cares about 0 to 5 meters. Everything outside this window is ignored or clamped.

**Output range** — the minimum and maximum values the output can reach. The light might only go from 0.2 to 0.8 intensity, never fully off and never fully bright.

Range is where students control scale and sensitivity. A narrow input range with a wide output range makes the interaction feel amplified — small movements, big responses. A wide input range with a narrow output range makes it feel subtle — you have to commit before anything happens.

Clamping and deadzone are not separate concepts — they are range settings. A deadzone is a gap at the bottom of the input range. Clamping is the natural consequence of defined boundaries.

### Envelope

The envelope defines *how the output reaches its target over time*. The curve says where the output should be; the envelope says how it gets there.

This is borrowed from sound synthesis, where every sound has an ADSR envelope: Attack, Decay, Sustain, Release. The same four parameters describe the temporal character of any interaction response.

**Attack** — how fast the output reaches its target when activated. A fast attack feels snappy, mechanical, eager. A slow attack feels gradual, organic, reluctant. In a bound relationship, this is how quickly the output catches up when the input changes. In an unbound relationship, this is the onset of the response.

**Decay** — whether the output overshoots its target and settles back. A light that flashes brighter than its sustained level and then dims back is showing decay. Most interactions have zero decay — they arrive at their target cleanly. But overshoot is one of the most visceral ways to make a response feel alive.

**Sustain** — what happens while the input is held. In a bound relationship with a continuous signal, sustain is trivial — the output simply tracks the mapped value. In a bound relationship with a binary signal, sustain defines what happens while the condition is true — hold steady at the target, drift slowly upward, oscillate. In an unbound relationship, sustain does not apply — there is no held phase.

**Release** — how the output returns to rest when the input stops or the condition ends. A fast release feels crisp, clinical, clean. A slow release feels lingering, warm — the space holds onto your presence after you've gone. Release can differ from attack, and this asymmetry — fast in, slow out, or slow in, fast out — is one of the most expressive parameters in the entire model.

**Not all four parameters are always active.** This is important. The envelope is universal in principle but selective in practice:

| | Attack | Decay | Sustain | Release |
|---|---|---|---|---|
| **Bound + continuous** | how fast output tracks input | overshoot on fast changes | holds at mapped value (trivial) | how fast output returns to rest |
| **Bound + binary** | speed of turning on | overshoot when activating | behavior while active | speed of turning off |
| **Unbound** | onset speed | settling after peak | not applicable | tail/fade |

For day-to-day design, **attack and release are the essential pair**. They are what the previous model called "speed-in and speed-out," and they cover the vast majority of expressive variation. Decay and sustain are the advanced extension — available when a student wants overshoot or drift, but not required for every interaction.

---

## Curve, Range, Envelope — Summary

These three are not alternatives. They are sequential stages that every signal passes through:

**Curve** (what value?) → **Range** (how much?) → **Envelope** (how fast?)

Or in a sentence: the curve determines the target, the range scales and clamps it, and the envelope shapes how the output arrives there over time.

A student designing an interaction makes three decisions: what is the shape of the relationship (curve), what are the boundaries (range), and what is the temporal feel (envelope). Change any one and the interaction feels different. That is the design space.

---

## State

State introduces memory into the system. Without state, every interaction is stateless — the same input always produces the same output, with no history. State changes that.

- **Accumulation** — values build over time. Each visit adds to a counter. The light is brighter the tenth time you approach than the first.
- **Toggle** — state persists after input ends. Press once, the light stays on. Press again, it turns off. The input is momentary; the effect is lasting.
- **Counters, progress, thresholds** — the system remembers what has happened and gates future behavior on that history.

State is not part of the relationship itself. It modifies what surrounds the relationship:

- It can transform the **input signal** before it reaches the curve (accumulated proximity instead of raw proximity).
- It can change the **conditions** that gate when a relationship is active.
- It can alter the **parameters** of the relationship itself (the curve shifts, the range widens, the envelope slows).

This separation — transformation is stateless, state wraps around it — aligns with how the course introduces these concepts. The transformation model (P1–P3) is learned first. State (P4) is layered on top.

---

## Feedback and Composition

The model describes one atom: one input, one relationship, one output. But interesting interactions are built from multiple atoms composed together.

- The output of one relationship can feed the input of another.
- Multiple relationships can drive the same output simultaneously (layering).
- A relationship's output can loop back to influence its own input (feedback).

This is where interactions become layered, dynamic, and conversational. The basic model remains valid at each node — it simply repeats and connects. Composition is not a new mechanism; it is the atom applied recursively.

---

## The Coupling Quality Vocabulary

Alongside the technical model, every interaction invites a phenomenological question: *what does this feel like?*

This is not a parameter. It is a vocabulary for critique and discussion — the bridge between technical choices and lived experience.

- **Eager** or **reluctant** — fast attack and tight tracking vs. slow onset and heavy smoothing.
- **Attentive** or **indifferent** — continuous proportional response vs. threshold that ignores you until you commit.
- **Precise** or **forgiving** — narrow range, steep curve vs. wide range, gentle curve.
- **Sticky** or **crisp** — slow release (lingers after you leave) vs. fast release (snaps back to neutral).
- **Alive** or **still** — oscillating sustain, overshoot, breathing vs. steady hold, clean tracking.

These qualities emerge from curve, range, and envelope choices, but they are experienced as a whole. The technical model gives students the tools to build. The coupling quality vocabulary gives them the language to evaluate.

---

## How We Got Here

This model evolved through six iterations. The history is preserved because the reasoning behind each simplification matters.

**Iteration 1: Shape × Temporality matrix.** Two independent axes (mapping shape × temporal behavior) producing ~56 theoretical combinations. Failed because the axes are not truly independent — they interact, and most combinations are redundant or incoherent.

**Iteration 2: Synth analogy (Mapping + ADSR).** Reframed as a signal chain: input → static curve → ADSR envelope → output. Correctly identified that mapping and time are sequential stages, not parallel axes. Failed because ADSR jargon was too technical and four phases were more detail than students needed.

**Iteration 3: Response Curve as single concept.** Attempted to collapse everything into one drawable AnimationCurve. Worked for continuous mappings but broke for discrete events — a button press doesn't have a "curve."

**Iteration 4: Continuous vs. Discrete distinction.** Recognized that the signal type (flowing value vs. discrete event) is a fundamental divide, not just a parameter.

**Iteration 5: Three map types (Continuous, On/Off, One-shot).** Collapsed everything to three perceptually distinct modes. Clean and teachable, but was secretly mixing signal type with relationship type in one axis.

**Iteration 6: Bound and Unbound × two signal types (this document).** Separated signal (continuous/binary) from relationship (bound/unbound). Resolved the ambiguity of On/Off (which was bound + binary signal, not a third category). Organized shape into three sequential stages: curve, range, envelope. ADSR preserved as the envelope model but positioned so that attack and release are the essential pair, with decay and sustain as advanced extensions.

---

## One-Line Teaching Version

The system is either bound to you — following your input — or unbound, continuing on its own. The shape of every response is defined by a curve, a range, and an envelope.

---

## Open Questions

- [ ] Should the Interactive Palette be reorganized around bound/unbound clusters instead of the old three-type clusters?
- [ ] Is "envelope" too technical a term for students, or does the synth analogy provide enough intuitive grounding?
- [ ] Should decay and sustain be hidden from the basic inspector and exposed only in an "advanced" foldout?
- [ ] Does the curve distinction (input→output vs. time→output) need a visual teaching aid, or is experiencing both in the palette sufficient?
