# Research Notes — Engineering Parallels: IPO, ADSR, Signal Processing

> Reference document collecting parallels from engineering, audio synthesis, animation, and reactive programming that informed the ID4 transformation model.
> Compiled during brainstorming, March 2026.

---

## 1. The IPO Model (Input → Process → Output)

The general systems model from computer science and systems engineering: every system receives **input**, applies a **process** (transformation), and produces **output**. Two additional elements complete the picture: **storage** (persistent state) and **feedback** (output routed back as input).

```
              ┌──────────┐
  Input ────► │ Process  │ ────► Output
              └────┬─────┘         │
                   │               │
              ┌────▼─────┐         │
              │ Storage  │         │
              └──────────┘         │
                                   │
              ┌──────────┐         │
              │ Feedback │ ◄───────┘
              └────┬─────┘
                   │
                   ▼
              (back to Input)
```

### How this maps to the ID4 model

| IPO Element | ID4 Equivalent |
|-------------|----------------|
| Input | Input (proximity, gaze, contact, button, etc.) |
| Process | Map (continuous/on-off/one-shot with parameters) |
| Output | Output (light, sound, material, particles, etc.) |
| Storage | State — handled separately via Variables and Conditions (P4+) |
| Feedback | Composition — one atom's output becomes another atom's input |

The ID4 transformation model is essentially the IPO model with the "Process" box opened up and decomposed into map type + temporal parameters. Storage and feedback are explicitly deferred to the course's state and composition systems respectively.

### Key insight from IPO

The IPO model treats "process" as a black box. For a course about designing the *feel* of interaction, the black box is exactly where the design lives. The transformation model's contribution is cracking open "process" and finding structure inside: the map type determines the character, the parameters determine the nuance.

---

## 2. The ADSR Envelope (Audio Synthesis)

The most directly useful parallel. ADSR (Attack, Decay, Sustain, Release) is the standard model for how a sound evolves over time in a synthesizer. Every synth patch, every sampled instrument, every sound effect has an ADSR envelope shaping its amplitude, filter, pitch, or any other parameter.

### The Four Phases

```
Level
  │
  │    /\
  │   /  \___________
  │  /    D    S      \
  │ / A              R \
  │/                    \___
  └─────────────────────────── Time
       ↑     ↑    ↑      ↑
    Key On           Key Off
```

**Attack (A):** How fast the sound reaches its peak after the key is pressed. Fast attack = percussive (piano, drum). Slow attack = swelling (strings, pads).

**Decay (D):** How fast the sound drops from its peak to its sustain level. Determines whether there's an initial transient "punch." Zero decay = the peak IS the sustain level.

**Sustain (S):** The level the sound holds at while the key is held. Not a time value — a level. The sound stays here indefinitely as long as the input is active.

**Release (R):** How fast the sound fades to silence after the key is released. Fast release = crisp cutoff. Slow release = lingering tail.

### Mapping to interaction design

| ADSR Phase | Interaction Equivalent | Example |
|------------|----------------------|---------|
| Attack | Onset speed of the response | How fast does the pillar glow when you enter the zone? |
| Decay | Overshoot and settling | Does the light flash brighter than its sustained level, then settle? |
| Sustain | Behavior while input is active | Does the glow hold steady? Slowly brighten? Pulse? |
| Release | Offset speed of the response | How fast does the glow fade when you leave? |

### How the three map types are ADSR presets

| Map Type | Attack | Decay | Sustain | Release |
|----------|--------|-------|---------|---------|
| **Continuous** | = smoothing speed | none | = tracks input value continuously | = smoothing speed |
| **On/Off** | = in-transition speed | none | holds at target | = out-transition speed |
| **One-shot** | = onset shape | = tail shape | none (no sustain phase) | none (plays independently) |

### Why ADSR is the right depth layer

ADSR is parametric rather than categorical. Instead of naming eight temporal behaviors (instantaneous, smoothed, one-shot, sustained, accumulated, decaying, rhythmic, delayed), four continuous parameters generate all of them:

| Named behavior | ADSR configuration |
|----------------|-------------------|
| Instantaneous | A=0, D=0, S=full, R=0 |
| Smoothed | A=moderate, D=0, S=full, R=moderate |
| One-shot (burst) | A=0, D=fast, S=0, R=0 |
| One-shot (swell) | A=slow, D=slow, S=0, R=0 |
| Sustained | A=moderate, D=0, S=full, R=moderate |
| Asymmetric (fast in, slow out) | A=fast, D=0, S=full, R=slow |
| Asymmetric (slow in, fast out) | A=slow, D=0, S=full, R=fast |
| Lingering | A=any, D=0, S=full, R=very slow |
| Snappy | A=0, D=0, S=full, R=0 |

Accumulated and decaying behaviors involve the sustain level changing over time, which extends the basic ADSR model — sustain becomes a slope rather than a flat line.

Rhythmic/pulsing behavior is not part of ADSR itself — it requires an additional modulation source (LFO, see below).

---

## 3. The Synthesizer Signal Chain

In a synthesizer, sound is shaped through a chain of processing stages:

```
[Oscillator] → [Filter] → [Amplifier] → [Effects] → Output
     ↑              ↑           ↑
     │              │           │
  [LFO/Env]    [LFO/Env]   [LFO/Env]
  (modulation) (modulation) (modulation)
```

**Oscillator** — generates the raw signal (waveform). This is the source.

**Filter** — shapes the frequency content (low-pass, high-pass, bandpass). Removes or emphasizes parts of the signal. Controlled by its own envelope — the filter opens and closes over time.

**Amplifier** — controls the volume over time. Shaped by the main ADSR envelope.

**LFO (Low Frequency Oscillator)** — a slow periodic signal (sine, triangle, square wave) that modulates any other parameter. An LFO on the amplifier creates tremolo (volume pulsing). An LFO on the filter creates wah-wah. An LFO on pitch creates vibrato.

**Effects** — delay, reverb, chorus, distortion. Post-processing applied to the final signal.

### How this maps to interaction design

| Synth Stage | Interaction Equivalent |
|-------------|----------------------|
| Oscillator (source) | The input signal (proximity value, gaze angle, etc.) |
| Filter (frequency shaping) | The response curve / map (which values pass through, how they're shaped) |
| Amplifier (volume shaping) | The ADSR envelope (how the output unfolds over time) |
| LFO (modulation) | Rhythm/pulse — a periodic signal modulating any parameter |
| Effects (post-processing) | Post-processing stack in Unity (bloom, vignette, color grading) |

### The key insight: Modulation is separate from mapping

In the synth model, the LFO is a separate signal source that can be routed to any destination. It doesn't change the mapping or the envelope — it modulates the output of either.

For interaction design, this means **pulse/rhythm is not a map type or an envelope setting**. It's a separate modulation layer. A pulsing pillar is: proximity (input) → continuous map → ADSR envelope → **multiplied by a sine wave LFO** → emission intensity (output). The pulse lives outside the transformation chain.

For the student-facing model this is probably too much detail. But it explains why "pulse" didn't fit neatly into either the map types or the temporal behavior list — it's a modulation source, not a transformation.

---

## 4. Easing Functions (Animation and Motion Design)

The animation world's vocabulary for curve shapes. Standardized across CSS, After Effects, Unity's DOTween, and every motion design tool.

### The standard easing types

| Easing | Curve Shape | Feel |
|--------|-------------|------|
| **Linear** | Straight line | Mechanical, constant, robotic |
| **Ease-In** | Slow start, fast end | Gathering momentum, hesitant beginning |
| **Ease-Out** | Fast start, slow end | Responsive, natural deceleration |
| **Ease-In-Out** | Slow start, fast middle, slow end | Smooth, organic, the most "natural" |
| **Ease-Out-In** | Fast start, slow middle, fast end | Rare, unusual, slightly uncanny |

### Power curves and named variations

Beyond the basic four, easing functions have named mathematical shapes:

| Name | Curve | Character |
|------|-------|-----------|
| **Quad** | x² | Gentle curve |
| **Cubic** | x³ | Moderate curve |
| **Quart** | x⁴ | Strong curve |
| **Quint** | x⁵ | Very strong curve |
| **Expo** | 2^x | Dramatic, explosive |
| **Sine** | sin(x) | Gentle, organic |
| **Circ** | circular arc | Sudden near the ends |
| **Back** | Overshoots then returns | Springy, playful |
| **Elastic** | Oscillates around target | Bouncy, wobbly |
| **Bounce** | Multiple diminishing bounces | Physical, cartoonish |

Reference: [easings.net](https://easings.net/) — visual catalog of all standard easing functions.

### Relevance to the transformation model

Easing functions are the vocabulary for the **curve shape** parameter in the continuous map type AND the **transition speed** parameter in the on/off type. When a student says "I want the light to ease in slowly," they're asking for an Ease-In curve on the continuous map's smoothing, or on the on/off transition.

In Unity, this maps directly to:
- **AnimationCurve** — drawable in the Inspector, evaluatable in code
- **DOTween easing** — `Ease.InOutCubic`, `Ease.OutElastic`, etc.
- **Mathf.Lerp / SmoothDamp** — for runtime smoothing

### Material Design's easing principles

Google's Material Design guidelines codify easing for UI motion:
- **Standard curve** (ease-in-out): for elements moving between positions on screen
- **Deceleration curve** (ease-out): for elements entering the screen — fast start, natural slowdown
- **Acceleration curve** (ease-in): for elements leaving the screen — slow departure, fast exit

The principle: **easing out is best for responses** because it feels responsive (immediate onset) while still natural (gradual settling). This applies directly to interaction design — an ease-out response to proximity feels more alive than linear tracking.

---

## 5. Reactive Programming Operators

Reactive programming (RxJS, Project Reactor, UniRx for Unity) provides a vocabulary for transforming **streams of values or events over time**. The operator categories are:

### Transformation operators

| Operator | What it does | Interaction parallel |
|----------|-------------|---------------------|
| **map** | Transform each value: x → f(x) | The response curve / continuous mapping |
| **filter** | Pass only values that meet a condition | Threshold / deadzone |
| **reduce / scan** | Collapse a stream into a running total | Accumulated state |
| **debounce** | Suppress rapid repeated events | Cooldown on a trigger |
| **throttle** | Limit rate of events | Rate limiting interaction |
| **delay** | Shift events forward in time | Delayed response |
| **buffer** | Collect events into groups | Batch processing of inputs |

### Combining operators

| Operator | What it does | Interaction parallel |
|----------|-------------|---------------------|
| **merge** | Combine multiple streams | Multiple inputs driving one output |
| **zip** | Pair events from two streams | Compound conditions (gaze AND proximity) |
| **combineLatest** | Output when any input changes | Cross-referencing variables |
| **switchMap** | Switch to a new stream on each event | State-dependent mapping changes |

### Relevance

The reactive programming vocabulary is useful for thinking about **composition** — how multiple interaction atoms combine. The transformation model describes a single atom (one input → one map → one output). Reactive operators describe how atoms wire together: merging inputs, filtering conditions, accumulating state, sequencing events.

For the course, this is too technical to teach directly. But the concepts appear implicitly in the toolkit architecture: `VariableTrigger` is a reactive `filter`. `ModifyVariable` is a `scan/reduce`. `SequenceAction` is a `concatMap`. `BranchAction` is a `switchMap`. The toolkit components ARE reactive operators with friendly names.

---

## 6. Control Theory: Transfer Functions

The most mathematically rigorous parallel. In control theory, a **transfer function** H(s) describes the complete input→output relationship of a system in the frequency domain, including both the mapping shape and the temporal dynamics.

A first-order low-pass filter: `H(s) = ωc / (s + ωc)`

This single mathematical object simultaneously encodes:
- The mapping: how strongly the system responds to different rates of change
- The temporal behavior: how fast the output tracks the input, the smoothing characteristic

### Why the transformation model separates what control theory unifies

Control theory treats mapping and time as inseparable because they ARE mathematically inseparable in the frequency domain. The transformation model separates them because:

1. **Students are not engineers.** The Laplace domain is not accessible to art/design students.
2. **The separation is pragmatically useful.** "Choose a curve shape, then choose a smoothing speed" is actionable. "Design a transfer function in the s-domain" is not.
3. **Unity's implementation naturally separates them.** AnimationCurve handles the mapping; Lerp/SmoothDamp/DOTween handles the temporal smoothing. Two different tools, two different inspector fields.

The separation is a pedagogical convenience, not a mathematical truth. For the advanced ADSR layer, students who want more precision can think parametrically (attack/decay/sustain/release). But they will never need to think in terms of poles and zeros.

### What control theory adds that the model doesn't

**Stability analysis.** When output feeds back as input (feedback loops, P4+), control theory asks: does the system converge to a stable state, oscillate, or diverge? The transformation model doesn't address this because feedback is handled at the composition level, not the atom level. But when students build feedback loops in P4, stability becomes a real concern — a positive feedback loop between proximity and light intensity could oscillate or blow up. The instructor should be aware of control-theoretic principles even if students never hear the term "transfer function."

---

## Summary: What Each Field Contributes

| Field | Key concept | What it taught us |
|-------|-------------|-------------------|
| **Systems engineering (IPO)** | Input → Process → Output + Storage + Feedback | The overall architecture. Process = map. Storage = state. Feedback = composition. |
| **Audio synthesis (ADSR)** | Attack, Decay, Sustain, Release | The parametric model for temporal behavior. Four numbers describe any envelope. |
| **Synth signal chain** | Oscillator → Filter → Amplifier + LFO modulation | Map and envelope are sequential stages. Rhythm is a separate modulation source. |
| **Animation (easing)** | Ease-in, ease-out, named curves | The vocabulary for curve shapes. Directly usable in Unity (AnimationCurve, DOTween). |
| **Reactive programming** | map, filter, reduce, merge, zip | The vocabulary for composing streams. Maps to toolkit components with friendly names. |
| **Control theory** | Transfer functions, stability | The mathematical truth underneath. Map + time are inseparable in theory, separated in practice. |
