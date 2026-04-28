# Input Palette — Scene Spec

> A walkable scene showing the raw signal produced by each input type.
> Each station = one sensor + a world-space text readout of its value.
> No output components (no lights, no materials, no effects). Just the signal, visible as text/UI.
> The student walks around and discovers what each input type "sees."

---

## Purpose

Before designing relationships, students need to feel what each input signal does — its shape, range, responsiveness, noise. This scene isolates inputs. Each station answers: "What does this sensor know about me, and how does that knowledge behave as I move/look/act?"

---

## Project Context

- **Unity URP project**
- **Scene location:** `Assets/_Lab/`
- **Scene name:** `_Lab_InputPalette`
- First-person controller (Starter Assets FPS from `Assets/Starter Assets/`)
- Dark, minimal environment — floor plane, optional low walls between stations
- **No output components** — no lights reacting, no materials changing. Only world-space text/UI displaying the raw signal value.

### Key documents to read before building

1. **`Docs/Interactive Design 4/Interaction Model/primitives.md`** — The full catalog of inputs, their signal types (continuous/binary), and Unity implementations. This is the source of truth for what inputs exist.
2. **`Docs/Interactive Design 4/Interaction Model/transformation-model-v2.md`** — Sections "Signal" and "Core Statement" only. Explains continuous vs binary signal types.
3. **`Docs/Interactive Design 4/Interaction Model/primitives scene lab notes.txt`** — Section on "3 input channels" (body/spatial, world interaction, world-space UI). Context for how inputs are categorized.

### Existing scripts to understand

All in `Assets/Scripts/Modules/Sensors/`:

- **`Sensor.cs`** (base class) — all sensors inherit from this. Manages signals (detected objects + distance). Key API: `HasDetections`, `TryGetNearest(out Signal)`, `Signals` list. Each Signal is a struct with `Object` (GameObject) and `Distance` (float).
- **`ProximitySensor.cs`** — OverlapSphere detection. Reports distance to nearest tagged object. Continuous signal.
- **`GazeSensor.cs`** — Dot product between camera forward and direction to target. Has `threshold` (how direct the look must be) and `maxDistance`. Reports as detected/not + distance.
- **`TriggerSensor.cs`** — OnTriggerEnter/Exit. Binary detection. Requires collider with isTrigger.
- **`RaycastSensor.cs`** — Forward raycast or spherecast. Reports hit object + distance.
- **`CollisionSensor.cs`** — OnCollisionEnter/Exit. Reports collision objects.

Also read:
- **`Assets/Scripts/Modules/Glue/SensorResponse.cs`** — Shows how sensor signals are consumed (OnFirstDetected, OnWhileDetected, OnAllLost events). You probably won't use this component directly, but it shows the API pattern.

---

## Station Design

Each station is a physical area in the scene containing:

1. **A sensor** (existing Ludocore sensor or a small custom script)
2. **A visible zone/object** marking where the input is active (a floor area, an object to look at, etc.)
3. **A world-space text display** (TextMeshPro) showing the raw signal value, updated every frame
4. **A label** identifying the input name and signal type

Each station needs a small **display controller script** that reads the sensor (or input source) and writes the value to a TextMeshPro. These can be per-station scripts or a small set of reusable ones — whatever is cleaner. Follow Ludocore conventions: `namespace Ludocore`, `[SerializeField] private` fields, PascalCase methods.

---

## Stations

### Continuous Signals

**Station: Proximity**
- ProximitySensor on a pedestal/column, tag "Player"
- Display shows: `distance: 7.32` (updating every frame)
- Student walks toward/away and sees the float change smoothly
- Radius ~10m so the value is visible from a distance

**Station: Gaze Direction**
- GazeSensor on a wall-mounted object (panel or sphere), tag "Player"
- Display shows: `dot: 0.87` + `detected: true/false`
- Student looks at the object, sees the dot product spike; looks away, it drops
- Set threshold ~0.7 so the detection boundary is experienceable

**Station: Gaze Duration**
- GazeSensor on an object, but display shows **accumulated seconds** while detected
- Display shows: `gaze time: 3.2s` — counts up while looking, resets to 0 when looking away
- Needs a small custom script: reads GazeSensor.HasDetections, accumulates Time.deltaTime while true, resets on false

**Station: Stillness**
- No existing sensor — needs a small custom script
- Reads player's CharacterController.velocity (or transform delta), counts seconds while speed < threshold
- Display shows: `still: 4.1s` — counts up while stationary, resets on movement
- Place in a quiet corner — the station rewards not moving

**Station: Velocity**
- No existing sensor — needs a small custom script
- Reads player's CharacterController.velocity.magnitude
- Display shows: `speed: 2.34`
- Student walks slowly (low), runs (high), stops (zero)
- Noisy signal — that's the point

### Binary Signals

**Station: Presence (zone)**
- TriggerSensor on a visible floor area (slightly raised or tinted platform), tag "Player"
- Display shows: `inside: YES` / `inside: NO`
- Clear boundary — step in, flips; step out, flips back

**Station: Contact (floor tile)**
- TriggerSensor on a small thin floor tile, tag "Player"
- Display shows: `contact: YES` / `contact: NO`
- Physically similar to presence but framed differently — touching vs. being inside
- Smaller area than the presence zone to emphasize physicality

**Station: Button**
- World-space UI button (Canvas in world space, Button component)
- Player activates via raycast interaction (RaycastSensor on player camera + a small click handler)
- Display shows: `pressed` (momentary flash) then returns to `idle`
- This is a discrete event, not a held state — the display should show the event then clear

**Station: Toggle**
- World-space UI toggle
- Display shows: `state: ON` / `state: OFF`
- Persists after interaction — press once, stays on; press again, off

### Autonomous Signals (no player input)

**Station: Time (oscillating)**
- No sensor — a small script outputs `Mathf.Sin(Time.time * frequency)` mapped to 0–1
- Display shows: `time: 0.73` — oscillates continuously
- The student watches a signal that runs without them

**Station: Random**
- A small script that periodically (every ~1s) generates a new `Random.Range(0f, 1f)`
- Display shows: `random: 0.41` — jumps unpredictably
- Contrast with time: both autonomous, but one is ordered and the other is noise

---

## Custom Scripts Needed

Small, purpose-built scripts. Not generic framework modules — just what each station needs.

1. **GazeDurationDisplay** — accumulates gaze time from GazeSensor, writes to TextMeshPro
2. **StillnessDisplay** — reads player velocity, accumulates stillness seconds, writes to TMP
3. **VelocityDisplay** — reads player velocity magnitude, writes to TMP
4. **SineSignalDisplay** — outputs oscillating sine value, writes to TMP
5. **RandomSignalDisplay** — outputs periodic random value, writes to TMP
6. **ProximityDisplay** — reads ProximitySensor nearest distance, writes to TMP
7. **GazeDirectionDisplay** — reads GazeSensor detection state + dot product, writes to TMP
8. **BinaryDisplay** — reads any Sensor's HasDetections, writes YES/NO to TMP (reusable for presence + contact)
9. **ButtonDisplay** / **ToggleDisplay** — UI interaction handlers, write state to TMP

Some of these are trivial (3-line Update methods). Group or split as makes sense — the point is clarity, not minimalism.

---

## Scene Layout

Linear walkthrough — stations along a corridor or in a sequence.

Suggested order (matches learning progression):
1. Presence (binary) — simplest, most familiar
2. Contact (binary) — similar but physically smaller
3. Proximity (continuous) — evolution of presence into a flowing value
4. Gaze direction (continuous) — attention as input
5. Gaze duration (continuous) — patience as input
6. Stillness (continuous) — absence of action as input
7. Velocity (continuous) — quality of movement as input
8. Button (binary event) — intentional discrete action
9. Toggle (binary persistent) — intentional lasting action
10. Time (autonomous) — system without player
11. Random (autonomous) — noise without player

---

## What This Is NOT

- Not interactive in the relationship sense — no designed responses, no curves, no envelopes
- Not the interaction palette (that connects inputs to outputs through relationships)
- Not using existing Ludocore output modules (no MaterialColor, no Scale, no lights responding)
- Not exhaustive — Slider, Dropdown, push/force, throw can be added later
