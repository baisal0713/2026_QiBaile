# The Interactive Palette — Design Document

> A persistent showcase scene for ID4.
> A walkable reference of interaction atoms — every station demonstrates one Input → Map → Output combination.
> Used by the instructor to demonstrate and by students to explore independently.
> All six projects point to and draw from this palette.

---

## What This Is

A hallway (or room, or open space) containing 15–20 stations. Each station is a simple object — a column, a pedestal, a wall panel, a floor tile — with one interaction atom wired to it. The participant walks through and experiences the atoms.

Each station has a world-space UI label that names:
- The **input** (what the system knows about you)
- The **map type** (continuous, on/off, or one-shot)
- The **output** (what changes in the world)

The palette is not a project. It is not art. It is a **test bench with atmosphere** — abstract, clear, browsable. It grows as the course progresses: new stations are added as new components and map types are introduced.

---

## The Three Dimensions

### Inputs — What the System Knows About You

| Input | Signal type | How it works in Unity |
|-------|------------|----------------------|
| **Proximity** | Continuous float (distance) | ProximitySensor — OverlapSphere, returns distance to nearest tagged object |
| **Gaze** | Continuous float (dot product / duration) | GazeSensor — dot product between camera forward and direction to object |
| **Contact** | Discrete event (enter/exit) | TriggerSensor — OnTriggerEnter/Exit on a collider |
| **Stillness** | Continuous float (time since last movement) | Custom — tracks player velocity, counts seconds below threshold |
| **Velocity** | Continuous float (movement speed) | CharacterController.velocity.magnitude or Rigidbody velocity |
| **Input action** | Discrete event (press/release) | InputTrigger — Unity Input System action |
| **UI slider** | Continuous float (0–1) | Unity UI Slider — direct manipulation for testing |
| **UI button** | Discrete event (click) | Unity UI Button — direct trigger for testing |
| **Time** | Continuous float (clock) | Mathf.Sin(Time.time * frequency) or similar — self-driving input |

For the palette, the primary spatial inputs are **proximity** (walk toward/away) and **contact** (step on/off). UI slider and button are included on select stations as diagnostic tools — students can isolate the map behavior by driving values directly.

---

### Map Types — How Input Relates to Output

| Map type | Behavior | Key parameters |
|----------|----------|----------------|
| **Continuous** | Output follows input in real time | Curve (linear, eased, inverse), Smoothing (instant → slow) |
| **On/Off** | Output switches between two states | Trigger condition, Transition speed (snap → fade), Asymmetry (in ≠ out) |
| **One-shot** | Output plays once and finishes | Duration, Shape (burst, swell, snap-and-tail) |

---

### Outputs — What Changes in the World

Organized by perceptual category, not by Unity component.

#### Brightness

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Point/Spot light | Light | intensity, range, shadow strength |
| Emissive material | Material (URP) | _EmissionColor intensity (HDR multiplier) |
| Bloom | Volume (Post-processing) | bloom intensity, bloom threshold |
| Ambient light | RenderSettings | ambientIntensity |

#### Color / Temperature

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Light color | Light | color (lerp between warm/cool) |
| Material base color | Material | _BaseColor |
| Fog color | RenderSettings | fogColor |
| Color grading | Volume | temperature, tint, saturation |
| Skybox tint | Material (skybox) | _Tint, _Exposure |

#### Density / Presence

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Fog | RenderSettings | fogDensity, fogStartDistance, fogEndDistance |
| Particles | ParticleSystem | emissionRate, startSize, startSpeed, startColor |
| Object spawning | Spawner script | spawn rate, count |
| Object activation | GameObject | SetActive (on/off) |
| Terrain detail | Terrain | detailDensity, detailDistance |

#### Scale / Weight / Space

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Transform scale | Transform | localScale (uniform or per-axis) |
| Vertex displacement | Shader Graph | displacement amount (requires custom shader) |
| Camera FOV | Camera / Cinemachine | fieldOfView |
| Depth of field | Volume | focalLength, aperture |
| Vignette | Volume | intensity |

#### Sound

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Volume | AudioSource | volume |
| Pitch | AudioSource | pitch |
| Spatial blend | AudioSource | spatialBlend (2D ↔ 3D) |
| Low-pass filter | AudioLowPassFilter | cutoffFrequency |
| Reverb | AudioReverbZone | room, decayTime |

#### Motion / Rhythm

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Rotation | Transform | Rotate (continuous or tween) |
| Position tween | Transform / DOTween | position (orbit, drift, bounce) |
| Animation speed | Animator | speed parameter |
| Flicker | Light / Material | randomized intensity over time |

#### Surface / Material

| Output | Unity component | Key drivable properties |
|--------|----------------|------------------------|
| Smoothness | Material | _Smoothness |
| Metallic | Material | _Metallic |
| Alpha / dissolve | Material (Shader Graph) | _Cutoff or dissolve threshold |
| Fresnel / rim glow | Material (Shader Graph) | fresnel power |
| Normal map strength | Material | _BumpScale |
| Tiling / UV offset | Material | _MainTex_ST (scrolling textures) |

---

## Station List

Each station demonstrates one atom: one input, one map type, one primary output. Organized in clusters by map type so the hallway has structure. Within each cluster, stations vary the output to show that the same map type feels different on different components.

### Cluster 1: Continuous

Stations where the output follows the input in real time. Walk closer, something changes. Walk away, it changes back. The relationship is always alive.

| # | Input | Map | Output | Description |
|---|-------|-----|--------|-------------|
| 1 | Proximity | Continuous (linear) | Emission intensity | **The baseline.** Column glows as you approach, dims as you leave. Linear curve, moderate smoothing. The L4 pillar — students know this one. |
| 2 | Proximity | Continuous (eased) | Emission + Light | Same column, but eased curve — slow start, fast finish. Compare directly with Station 1 to feel how the curve shape changes the character. Light intensity follows the same curve. |
| 3 | Proximity | Continuous (inverse) | Emission intensity | **Absence station.** Column glows when you're far away. Approach and it dims. The Rain Room principle — presence suppresses. |
| 4 | Proximity | Continuous (linear) | Particles (rate + size) | Not light — particles. Emission rate and particle size increase as you approach. Feels alive, organic, less geometric than the glow stations. |
| 5 | Proximity | Continuous (linear) | Sound (pitch + volume) | Audio-only station. A sustained tone rises in pitch and volume as you approach. Spatial audio — the sound is located on the object. Requires headphones. |
| 6 | Proximity | Continuous (linear) | Fog density + color temperature | **Atmosphere station.** Approaching this object doesn't change the object — it changes the entire room. Fog thickens, color grading warms. Global scope, not local. |
| 7 | Stillness | Continuous (slow ramp) | Bloom + ambient + particles | **Patience station.** Stand still anywhere in this zone. After a few seconds, the space softens — bloom increases, ambient warms, gentle particles emerge. Move and it snaps back. Stillness as input. |

### Cluster 2: On/Off

Stations where the output has two states and switches between them. Cross a boundary, something changes. Clear, binary, defined.

| # | Input | Map | Output | Description |
|---|-------|-----|--------|-------------|
| 8 | Contact (floor) | On/Off (fast in, fast out) | Material color + sound | **Snap station.** Step on a floor tile — it lights up and plays a tone. Step off — instant reset. Crisp, tactile, immediate. |
| 9 | Contact (floor) | On/Off (fast in, slow out) | Material color + sound | **Linger station.** Same floor tile, but the color fades slowly when you step off. The sound tails away. The space remembers your step briefly. Compare with Station 8. |
| 10 | Proximity (threshold) | On/Off (moderate in, moderate out) | Light + material + sound | **Threshold station.** Walk toward this object — nothing happens. Nothing. Then at exactly 2 meters, it smoothly activates: light, glow, ambient tone. The boundary is the design. |
| 11 | Gaze (duration) | On/Off (slow in, slow out) | Material dissolve / reveal | **Attention station.** Look at a dark wall panel. After 2 seconds of sustained gaze, it slowly dissolves to reveal an emissive pattern underneath. Look away — it slowly fades back. Attention is the input; patience is the cost. |

### Cluster 3: One-shot

Stations where the input triggers something that plays once and finishes independently. Fire and forget.

| # | Input | Map | Output | Description |
|---|-------|-----|--------|-------------|
| 12 | Contact (collision) | One-shot (burst) | Particles + sound + camera shake | **Impact station.** Walk into this object. A particle burst explodes outward, a percussive sound fires, the camera shakes briefly. One moment, then done. Doesn't matter if you stay. |
| 13 | Input action (button) | One-shot (swell) | Light + emission + fog | **Pulse station.** Press a button. A wave of light swells outward from the object — emission rises, light brightens, nearby fog pulses — then subsides over 3 seconds. A slow, deliberate one-shot. |
| 14 | Proximity (threshold) | One-shot (spawn burst) | Spawner + particles | **Threshold burst.** Walk toward this object. At 3 meters, a ring of small objects spawns around it with a particle flourish. It only fires once per approach — leave and return to trigger it again. |

### Cluster 4: Combinations and Special Cases

Stations that layer multiple map types or demonstrate edge cases.

| # | Input | Map | Output | Description |
|---|-------|-----|--------|-------------|
| 15 | Proximity (continuous) + Proximity (threshold) | Continuous + One-shot | Emission + particle burst | **Layered station.** As you approach, the column glows continuously (like Station 1). But at 1.5 meters, a one-shot particle burst fires as a bonus event. Two map types on one object, two felt moments. |
| 16 | Time (clock) | Continuous (sine wave) | Emission + scale | **Breathing station.** No participant input. This object pulses on its own — emission and scale oscillating on a sine wave. Time as input, continuous map, rhythmic output. It's alive whether you're watching or not. |
| 17 | Gaze + proximity | On/Off (compound condition) | Material reveal + sound | **Compound station.** The wall panel only reveals if you are BOTH close (proximity < 3m) AND looking at it (gaze active). Either alone does nothing. Demonstrates compound conditions. |
| 18 | Velocity | Continuous (linear) | Particles (trail) + sound (pitch) | **Speed station.** Walk slowly — nothing. Walk fast — particles trail behind you and a wind sound rises in pitch. Your movement speed is the input. The faster you move, the more the space reacts. |

---

## Station Anatomy

Every station is a prefab containing:

```
[Station Root]
├── Visual Object (column, panel, tile, pedestal)
│   ├── Renderer (with configured material)
│   └── Optional: Light, ParticleSystem, AudioSource
├── Sensor (ProximitySensor, GazeSensor, TriggerSensor, etc.)
├── Controller (spec-generated script: one per station)
└── Label (World-space Canvas)
    ├── Input name ("Proximity")
    ├── Map type ("Continuous — eased curve")
    ├── Output name ("Emission + Light")
    └── Coupling question ("Does this feel eager or reluctant?")
```

The **controller** is the interaction atom — it reads the sensor, applies the map, drives the output. Each station has its own controller script, generated from a spec using the AI workflow. The spec follows the course's module conventions (header comment, SerializeField, public methods).

The **label** is a small world-space UI panel floating near the station. It names the three dimensions plus poses one coupling quality question. Students can read it while experiencing the interaction.

---

## Build Plan

### Phase 1: Core (before L5)

Build the continuous cluster (Stations 1–6) and the basic on/off stations (8, 10). These cover the map types students already know from L4 and introduce curve shape variation. ~10 stations.

### Phase 2: Expansion (L5–L7)

Add the gaze station (11), one-shot stations (12–14), and the compound station (17). These introduce new sensor types and the one-shot map type. ~15 stations.

### Phase 3: Full palette (L8+)

Add the special cases — stillness (7), velocity (18), breathing (16), layered (15). Plus any stations students contribute from their own projects. ~18+ stations.

### Student contributions

A student who writes a spec for a new controller — e.g., "gaze duration drives vertex displacement" — can add it to the palette as a new station. The palette grows. By the end of the course, it's a collective library.

---

## Scene Layout

The palette scene is a long, dim hallway or open room with stations arranged in clusters. The visual language is minimal — dark floor, dark walls, each station is a simple geometric object (cylinder, cube, panel) that lights up only through its interaction. The room is dark by default; the participant's presence illuminates it.

```
[Entrance]

  Cluster 1: CONTINUOUS
  ┌─────────────────────────────┐
  │  [1]  [2]  [3]             │  Proximity → Brightness
  │  [4]  [5]  [6]  [7]       │  Proximity → Other outputs
  └─────────────────────────────┘

  Cluster 2: ON/OFF
  ┌─────────────────────────────┐
  │  [8]  [9]                  │  Contact → Surface + Sound
  │  [10] [11]                 │  Threshold + Gaze
  └─────────────────────────────┘

  Cluster 3: ONE-SHOT
  ┌─────────────────────────────┐
  │  [12] [13] [14]            │  Events → Bursts
  └─────────────────────────────┘

  Cluster 4: COMBINATIONS
  ┌─────────────────────────────┐
  │  [15] [16] [17] [18]      │  Layered + Special
  └─────────────────────────────┘

[End / Loop back]
```

Spacing between stations: enough that each one's response zone doesn't overlap with its neighbors. Students should be able to experience one station at a time in isolation.

---

## Relationship to the Six Projects

The palette is not a project — it is a reference that all projects draw from.

| Project | Stations to reference |
|---------|----------------------|
| P1 Ecosystem | (Pre-palette — ecosystem modules are the precursor) |
| P2 Presence Room | Stations 1–7: continuous proximity driving various outputs |
| P3 Active Interaction | Stations 8–9, 12–14: contact, collisions, one-shot responses |
| P4 Interaction + State | Station 7 (stillness), 11 (gaze duration) — inputs that imply accumulation |
| P5 Narration & Choices | Station 17 (compound conditions), 11 (gaze as attention/choice) |
| P6 Progression | Station 15 (layered types), 16 (time-driven) — composition and temporal arcs |

When introducing a new project, the instructor walks students through the relevant palette stations first: "Before we build the Presence Room, let's visit Stations 1–6 and feel the difference between linear and eased proximity, between local and global scope."

---

## Open Questions

- [ ] Should each station have a UI slider override that lets students bypass the spatial input and drive the value directly? Useful for diagnosis but adds visual clutter.
- [ ] How many stations can coexist in one scene before performance degrades? (Particle systems, lights, post-processing — may need LOD or activation distance.)
- [ ] Should the palette be one scene or multiple scenes (one per cluster)?
- [ ] Audio stations require headphones. Flag these visually?
- [ ] Does the palette need a "reset" mechanism (reload scene) for accumulated/one-shot stations?
