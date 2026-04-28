# Backrooms Interaction Catalog

> A comprehensive catalog of interaction designs for the Backrooms teaching scene.
> Organized by interaction model tier (complexity) and cross-referenced by output domain.
> Each entry maps to the transformation model: Input → Relationship → Output.
> The Backrooms aesthetic: liminal dread through wrongness, not monsters. Every interaction
> amplifies the feeling that the space is alive, aware, and slightly wrong.
> Last updated: March 2026.

---

## Available Assets

### Geometry
- **BackroomsLite** — modular floor/ceiling/wall/door/stair prefabs. Floor prefabs have a 2-material renderer: slot 0 = floor, slot 1 = ceiling (emissive)
- **Backrooms (full)** — separate ceiling, floor, wall, light, vent, door, pitfall, and prop meshes. Includes Poolrooms variant with water shader
- **Maksym Skrypka Liminal Space** — animated floor/wall shadergraph, decal meshes, eye decal shader, ceiling variants (with lights, with vents)

### Audio
- **Backrooms ambience** (`Backrooms/Audio/`) — ambient loop
- **Before Dark** — layered ambient tracks (DARK/FULL/LIGHT/MEDIUM variants, each with INTRO/LOOP/OUTRO)
- **Entity SFX** — creature/entity sounds (usable as distant unexplained sounds)
- **Stingers** — NEUTRAL and POSITIVE one-shots (usable as unbound triggers)
- **Backrooms Forever DEMO** — additional ambient music
- **Backrooms Music Vol. 1** — ambient soundtrack

### Shaders
- **ORM Shader** (BackroomsLite) — ceiling material with `_EmissionColor` (HDR), `_EMISSION` keyword, `_BaseColor`
- **Animated floor/wall** (Maksym Skrypka) — shader-driven surface animation, drivable parameters
- **Decal / Decal eye** (Maksym Skrypka) — wall stain/mark shaders, eye decal for "being watched" effect
- **Water shader** (Backrooms/Poolrooms) — animated water surface
- **Sonar shader** — expanding ring visualization from a point (collision/position driven)
- **Simple Toon + Outline** — stylized rendering with outline pass

### Existing Modules (Ludocore)
- **Sensors:** ProximitySensor, GazeSensor, TriggerSensor, RaycastSensor, CollisionSensor
- **Glue:** SensorResponse, ThresholdResponse, GateResponse, ColumnController, CeilingLightDimmer
- **Effects:** MaterialColor, MaterialEmissionIntensity, MaterialFloat
- **Transform:** Move, Rotate, Scale
- **Physics:** Force, RadialForce, Torque
- **State:** Counter, Gate, Chance, VisibilityGate
- **Timing:** Timer, TimeScale
- **Spawning:** Spawner

### Post-Processing (URP Volume)
Bloom, Color Adjustments (temperature, saturation, contrast), Vignette, Film Grain, Chromatic Aberration, Depth of Field, Motion Blur

---

## Output Domains for the Backrooms

### Light
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| intensity | Light | 0–8+ | Fluorescent brightness. The primary channel. |
| color | Light | Color | Warm yellow-white → sickly green → cold blue |
| range | Light | 0–20+ | Pool size. Isolation (small) vs. surveillance (large) |
| shadowStrength | Light | 0–1 | Hard = institutional. Soft = dreamlike |

### Emission
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| _EmissionColor | Material | HDR color | Fluorescent tube glow. Separate from light — tube can glow without illuminating |
| emission hue | Material | Color | One tube slightly greener = something wrong with that tube specifically |

### Fog
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| fogDensity | RenderSettings | 0–0.1 | Thin haze → can't see end of corridor |
| fogColor | RenderSettings | Color | Yellow = fluorescent wash. Gray = void |
| fogStart/End | RenderSettings | 0–100 | Visibility range. Short = oppressive |

### Sound
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| volume | AudioSource | 0–1 | Hum presence/absence. Silence is also an output |
| pitch | AudioSource | 0.5–2 | 0.95 = something off. 0.8 = dread |
| cutoffFrequency | AudioLowPassFilter | 800–22000 | Muffled = through walls. Clear = present |
| spatialBlend | AudioSource | 0–1 | 3D = locatable. 2D = sourceless, everywhere |
| reverbDecay | AudioReverbZone | 0.1–20 | Big reverb in small room = space is wrong |

### Post-Processing
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| temperature | Color Adjustments | -100–100 | Warm (+10) to cold (-30). Subliminal tint shift |
| saturation | Color Adjustments | -100–100 | Drain = lifelessness. -30 = institutional. -100 = wrong |
| vignette | Vignette | 0–1 | Tunnel vision, claustrophobia. 0.2–0.45 range |
| bloom intensity | Bloom | 0–10 | Harsh fluorescent overexposure |
| filmGrain | Film Grain | 0–1 | Security camera degradation |
| chromatic aberration | Chromatic Aberration | 0–1 | Perceptual failure. Use sparingly in spikes |
| depth of field | Depth of Field | varies | Focal length shift = losing focus |

### Material / Surface
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| _Smoothness | Material | 0–1 | Dry (0.2) → damp (0.6). Wet floor, no water source |
| _BaseColor | Material | Color | Yellowing walls, darkening carpet |
| _BumpScale | Material | 0–2 | Surface damage / deterioration |
| animated_floor params | ShaderGraph | varies | Subtle surface movement (Maksym Skrypka shader) |
| animated_wall params | ShaderGraph | varies | Wall surface distortion |
| decal_eye params | ShaderGraph | varies | "Being watched" eye decal |

### Transform / Spatial
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| localScale | Transform | 0.8–1.2 | Corridor shrinking. Ceiling lowering. Imperceptible |
| localPosition | Transform | small offsets | Objects drift. Exit sign recedes. Furniture shifts |
| localRotation | Transform | small angles | Objects orient toward player. Columns track you |

### Camera
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| fieldOfView | Camera | 55–70 | ±3 degrees. Room feels too big or too small |

### Particles
| Property | Component | Range | Backrooms use |
|---|---|---|---|
| emissionRate | ParticleSystem | 0–50 | Dust motes, drips, floor fog |
| startSize | ParticleSystem | 0.01–0.5 | Dust = tiny. Fog = medium |
| startSpeed | ParticleSystem | 0–2 | Slow drift = stale air |

---

## Tier 1 — Bound, Simple Envelopes

*The space notices you. Single input→output chains. Students learn: a relationship has character defined by its envelope.*

**Feel: The space is alive.**

### 1.1 Fluorescent Stalkers ★
- **Input:** Proximity (continuous, distance)
- **Relationship:** Bound, inverse — closer = dimmer
- **Output:** Ceiling emission intensity (`_EmissionColor`)
- **Envelope:** Slow attack (light takes a beat to notice you), very slow release (lingers after you leave, watching you go)
- **Complexity:** Low — already built as `CeilingLightDimmer`
- **Uncanny because:** The timing is wrong. Lights should respond instantly. These wake up.
- **Variation A:** Normal (closer = brighter). Mechanical, responsive, safe. The control version.
- **Variation B:** Inverse (closer = dimmer). Rain Room principle. Presence suppresses.
- **Teaching moment:** Same input, same output, inverted curve = completely different felt quality.

### 1.2 The Hum
- **Input:** Proximity to ceiling panels (continuous, distance)
- **Relationship:** Bound, linear
- **Output:** AudioSource volume + slight pitch shift (per-panel spatial audio)
- **Envelope:** Fast attack, fast release (normal tracking)
- **Complexity:** Low — same sensor pattern as CeilingLightDimmer, drives AudioSource instead
- **Uncanny because:** It's NOT uncanny. This is the normal grounding layer. Walk between lights and hear the handoff. The hum establishes what "normal" feels like so everything else feels wrong by contrast.
- **Setup:** Each ceiling panel (or every Nth panel) gets a looping AudioSource with the fluorescent hum. spatialBlend = 1.0 (3D). Volume and pitch driven by proximity.

### 1.3 Breathing Walls
- **Input:** Proximity (continuous, distance) + Time (autonomous sine wave)
- **Relationship:** Bound, inverse + autonomous
- **Output:** Wall segment localScale.y (subtle pulse, ±2%)
- **Envelope:** The sine wave is always running. Proximity dampens the amplitude — walls hold their breath when you're close, resume when you walk away.
- **Complexity:** Low-medium — two inputs composited (multiply proximity with sine amplitude)
- **Uncanny because:** The space is alive but shy. It moves when you're not near. Peripheral vision catches it.

### 1.4 Carpet Memory
- **Input:** Proximity to floor panels (continuous, distance)
- **Relationship:** Bound, asymmetric envelope
- **Output:** Floor material `_BaseColor` darkening
- **Envelope:** Instant attack (darkens on contact), extremely slow release (30+ seconds to recover)
- **Complexity:** Low — same sensor-to-material pattern, asymmetric smoothing
- **Uncanny because:** You leave a visible trail that slowly fades. The carpet remembers where you stepped. Not state — just a very long release tail.
- **Technical note:** Needs material instances per floor panel (same pattern as CeilingLightDimmer but slot 0).

### 1.5 Tracking Columns
- **Input:** Proximity or player position (continuous)
- **Relationship:** Bound, continuous
- **Output:** Column/post localRotation — slowly orients toward player
- **Envelope:** Very slow attack (0.5°/sec). Instant release (snaps to rest when out of range).
- **Complexity:** Low — uses existing `LookAt` module or simple Quaternion.Slerp
- **Uncanny because:** Structural columns shouldn't rotate. The movement is so slow you question whether it happened.

### 1.6 Proximity Fog
- **Input:** Proximity to a zone center (continuous, distance)
- **Relationship:** Bound, linear
- **Output:** RenderSettings.fogDensity
- **Envelope:** Medium attack, medium release
- **Complexity:** Low — single value driven by distance
- **Uncanny because:** At this tier it's not uncanny yet — just spatial. The space gets hazier as you go deeper. Establishes fog as a responsive material.

---

## Tier 2 — Bound, Shaped Curves and Asymmetric Envelopes

*The space is wrong. Same relationship type, but curve and range create specific character. Students learn: the shape of the mapping IS the design.*

**Feel: The space is wrong.**

### 2.1 The Reluctant Corridor
- **Input:** Proximity / depth into corridor (continuous)
- **Relationship:** Bound, ease-in curve (steep)
- **Output:** Fog density + fog color shift (yellow → gray)
- **Envelope:** Slow attack, medium release
- **Range:** Narrow input range — you have to walk deep before anything happens, then it thickens rapidly
- **Complexity:** Medium — shaped curve, narrow range, fog driving
- **Uncanny because:** The corridor resists your presence, then gives in all at once. Feels like crossing a boundary you shouldn't have.

### 2.2 Attention Leak
- **Input:** Gaze direction + duration on wall panel (GazeSensor, continuous dot product + accumulated time)
- **Relationship:** Bound, logarithmic curve
- **Output:** Wall panel emission (rises while looked at). Using decal shader or emission on specific panels
- **Envelope:** Fast initial response (logarithmic — reacts quickly then plateaus). Very slow release (sticky — the glow lingers after you look away).
- **Complexity:** Medium — gaze sensor, accumulation, logarithmic curve
- **Uncanny because:** The wall reacts to being seen, then catches itself. Like it didn't mean to show you that. The stickiness means you see the afterglow and know it was responding.
- **Asset opportunity:** Use the Maksym Skrypka decal or decal_eye shader on specific wall marks.

### 2.3 Wrong Echo
- **Input:** Player velocity (continuous, speed)
- **Relationship:** Bound, inverse shaped curve
- **Output:** Footstep AudioSource pitch
- **Envelope:** Fast tracking
- **Curve:** Walk slowly = pitch 1.0 (normal). Walk fast = pitch drops to 0.85 (wrong)
- **Complexity:** Medium — reads CharacterController velocity, drives audio pitch
- **Uncanny because:** Not scary — just wrong. Your own footsteps sound deeper when you hurry. Penalizes urgency.

### 2.4 The Warm Spot
- **Input:** Proximity to a specific invisible zone (continuous)
- **Relationship:** Bound, gaussian/bell curve (peaks at zone center, falls off smoothly)
- **Output:** Post-processing color temperature (+15 warmer at center)
- **Envelope:** Slow attack, slow release
- **Complexity:** Medium — Volume override lerping, zone-based
- **Uncanny because:** One corner of one room is slightly warm. No visible reason. Like something was there recently. Or is there now.

### 2.5 Dampened Wetness
- **Input:** Depth / distance from start (continuous, can use Z position or room count)
- **Relationship:** Bound, linear with narrow output range
- **Output:** Floor material `_Smoothness` (0.2 → 0.6)
- **Envelope:** N/A — position-based, not time-based
- **Complexity:** Low-medium — material float driving
- **Uncanny because:** The floor gets wetter the deeper you go. No water source visible. Just damp. The reflections appear gradually.

### 2.6 Fluorescent Startup Sequence
- **Input:** Proximity (panel first enters sensor range)
- **Relationship:** Bound with unbound onset — first 0.3s is a rapid flicker (on-off-on-off-on), then settles to normal bound tracking
- **Output:** Ceiling emission oscillation → steady state
- **Envelope:** Burst onset, then transitions to bound
- **Complexity:** Medium — state transition between two behaviors
- **Uncanny because:** Real fluorescents do this. But these do it because you approached. The light needed a moment to "notice" you.

---

## Tier 3 — Unbound (Triggered Responses)

*Things that happen and let go. Input fires, output runs independently. Students learn: unbound relationships feel fundamentally different from bound ones. The participant acts; the world takes over.*

**Feel: Things happen without explanation.**

### 3.1 The Flicker
- **Input:** TriggerSensor zone in a doorway (binary, enter)
- **Relationship:** Unbound, burst envelope
- **Output:** A light 2–3 rooms ahead flickers violently for 3 seconds, then stabilizes
- **Envelope:** Instant onset, rapid oscillation (random intensity between 0 and max for 3s), then settle
- **Complexity:** Medium — trigger zone wired to distant light, timed playback
- **Uncanny because:** Your crossing caused something far away. Spatial separation between cause and effect. Was that you?
- **Audio layer:** The flickering light's hum spikes in pitch during the flicker (same burst envelope on pitch).

### 3.2 Distant Door
- **Input:** TriggerSensor zone (binary, enter)
- **Relationship:** Unbound, delayed trigger — 2 second delay, then one-shot sound
- **Output:** Door slam AudioSource placed behind the player's entry point. spatialBlend = 1.0
- **Envelope:** 2s silence → instant slam → done
- **Complexity:** Low-medium — delayed event, spatial audio placement
- **Audio:** Use entity SFX or stinger from the Backrooms Audio library.
- **Uncanny because:** You turn around. Nothing. The delay is the design.

### 3.3 Peripheral Shift
- **Input:** GazeSensor on a specific object (binary, on gaze lost)
- **Relationship:** Unbound, triggered on gaze exit
- **Output:** A nearby object's localPosition shifts by 10–20cm over 0.5 seconds
- **Envelope:** Smooth ease-out movement, fires only when you look away
- **Complexity:** Medium — gaze exit event, position tween
- **Uncanny because:** You never see it move. You just notice things aren't where they were. Gaslighting as interaction design. The space rearranges itself behind your attention.

### 3.4 The Sigh
- **Input:** TriggerSensor zone at room entrance (binary, enter)
- **Relationship:** Unbound, swell envelope
- **Output:** Ambient exhale/breath sound (5-second swell up and fade). Use a LIGHT or MEDIUM loop from the Before Dark audio, played as a one-shot swell
- **Envelope:** Slow attack (2s rise), brief hold, slow decay (3s fade)
- **Complexity:** Low — trigger → play audio with volume envelope
- **Uncanny because:** The room breathes out when you enter. As if it was holding its breath.

### 3.5 Sonar Pulse
- **Input:** Collision or trigger zone (binary event)
- **Relationship:** Unbound, expanding ring
- **Output:** Sonar shader — expanding visible ring across all surfaces from the trigger point
- **Envelope:** Instant onset, expanding outward, fading as it goes
- **Complexity:** Medium — uses SimpleSonarShader system already in the project
- **Uncanny because:** Your presence sends a visible ripple through the space. Like echolocation — but the space is locating you, not the other way around.

### 3.6 The Blink
- **Input:** Timer (autonomous, random interval 45–90 seconds)
- **Relationship:** Unbound, micro-burst
- **Output:** Screen goes black for exactly 2 frames (0.033s). Post-processing or fullscreen overlay
- **Envelope:** Instant on, instant off. 2 frames.
- **Complexity:** Low — timer + screen overlay toggle
- **Uncanny because:** Too fast to be sure it happened. Like an involuntary blink you didn't authorize. You'll question your own perception.

### 3.7 Stinger Events
- **Input:** TriggerSensor zones placed at key architectural moments (doorways, turns, dead ends)
- **Relationship:** Unbound, one-shot
- **Output:** Audio stinger from the STINGERS/NEUTRAL library. One-shot, no repeat until zone is re-entered.
- **Envelope:** Follows the audio clip's own shape
- **Complexity:** Low — trigger → play audio
- **Uncanny because:** A musical accent at a spatial moment. Not jump-scare — just emphasis. The space punctuates your journey.

---

## Tier 4 — Conditions and Composition

*The space has rules. Relationships are gated by conditions or layered together. Students learn: multiple simple atoms composed together create emergent felt quality.*

**Feel: The space has rules you don't know.**

### 4.1 The Stare Test
- **Input:** Gaze duration on a specific wall stain/mark (continuous, accumulated seconds)
- **Condition:** Gaze duration > 5 seconds (threshold)
- **Relationship:** Bound, activated only after threshold
- **Output:** Ambient light temperature shifts cold (-20), low drone fades in (Before Dark DARK variant)
- **Envelope:** Slow attack once threshold crossed. Fast release if you look away before 5s — nothing happens.
- **Complexity:** Medium-high — gaze accumulation, threshold condition, two output channels
- **Uncanny because:** Rewards (punishes?) sustained attention. The space tests whether you're really looking. If you are, it responds. If you glance and move on, nothing.
- **Asset opportunity:** Use decal_eye shader on the stain. The eye becomes visible only after the threshold.

### 4.2 Still Water
- **Input:** Player velocity (continuous) + Proximity to puddle zone (binary condition)
- **Condition:** Proximity gates the velocity→ripple relationship. Only active when close.
- **Relationship:** Bound, continuous (velocity → ripple intensity)
- **Output:** Particle system ripples on floor, or water shader distortion parameter (Water_shader from Poolrooms)
- **Complexity:** Medium-high — compound condition, velocity reading, shader/particle driving
- **Uncanny because:** The puddle only reacts to your footsteps when you can see it. Like it's performing for you.

### 4.3 Layered Room (The Aware Room)
- **Input:** Multiple — proximity + floor contact + time
- **Relationship:** Composition of three independent atoms on one space:
  1. Proximity → fog density (bound, continuous)
  2. Floor tile contact → faint whisper audio (unbound, burst — use Entity SFX at very low volume)
  3. Time → slow light intensity pulse on all room lights (autonomous, sine wave)
- **Output:** Fog + sound + light
- **Complexity:** High — three atoms layered, no interaction between them
- **Uncanny because:** Each layer is simple alone. Together they make the room feel aware. The fog responds to you. The whispers react to your steps. The lights breathe on their own. The composition creates a presence that no single atom could.

### 4.4 Conditional Corridor
- **Input:** Proximity (continuous)
- **Condition:** Only active in one direction. A bool or direction check gates the relationship.
- **Relationship:** Bound — lights dim as you walk one way. Walking back = lights stay at whatever level. One-directional response.
- **Output:** Ceiling emission
- **Complexity:** Medium — directional condition
- **Uncanny because:** The corridor only darkens in one direction. Going back doesn't restore it. The way out is darker than the way in.

### 4.5 Compound Gaze Reveal
- **Input:** Gaze + proximity (both required)
- **Condition:** Proximity < 3m AND gaze active
- **Relationship:** Bound, slow attack
- **Output:** Wall panel material dissolves / reveals hidden pattern (using animated_wall shader or emission reveal)
- **Complexity:** Medium-high — compound AND condition, shader property driving
- **Uncanny because:** Neither proximity nor gaze alone does anything. You have to be close AND looking. A secret the space only shows to the committed.

---

## Tier 5 — State (Memory)

*The space remembers. Variables persist across interactions. Same input produces different output based on history. Students learn: state transforms interaction from reaction into relationship.*

**Feel: The space remembers you.**

### 5.1 Dimming
- **Input:** TriggerSensor on room entrance (binary, enter)
- **State:** IntVariable `visitCount` increments on each entry
- **Relationship:** visitCount → light intensity multiplier (bound to state, not to input)
- **Output:** Room light intensity. Visit 1 = full. Visit 3 = noticeably dimmer. Visit 6 = barely lit.
- **Complexity:** Medium — counter, variable-driven output
- **Uncanny because:** The room decays because of you. Your presence degrades it. Each visit costs the space something.

### 5.2 The Rearrangement
- **Input:** GazeSensor on a specific object (binary, detected)
- **State:** BoolVariable `wasObserved` set to true on gaze. On next room entry (TriggerSensor + condition: wasObserved == true), the object's position shifts. Reset bool.
- **Relationship:** Unbound, delayed by re-entry — the change happens between visits
- **Output:** Object localPosition offset (10–20cm)
- **Complexity:** High — two sensors, state variable, conditional activation, positional change
- **Uncanny because:** It only moves between your visits. Never while you watch. You can't catch it. State changes the scene while you're elsewhere.

### 5.3 One-Way Doors
- **Input:** TriggerSensor on doorway (binary, enter)
- **State:** IntVariable `doorPassCount` increments. Condition: if count > 1, activate the door behind you (close it).
- **Relationship:** Conditional activation — first pass = fine, second pass = door closes behind
- **Output:** GameObject activation (door mesh appears / collider enables)
- **Complexity:** Medium — counter + conditional activation
- **Uncanny because:** First time through: normal. Second time: you realize you can't go back. The space didn't change — your relationship to it changed. Irreversible.

### 5.4 Accumulated Dread
- **Input:** Multiple sources feed a single FloatVariable `unease`:
  - Entering new rooms (+1.0)
  - Staring at stains (+0.5 per 5s gaze)
  - Standing still too long (+0.3 per 10s idle)
  - Walking fast through flickering lights (+0.2)
- **State:** FloatVariable `unease` accumulates (never decreases, or decays very slowly)
- **Relationship:** unease → multiple outputs (bound to state variable)
- **Output:**
  - Post-processing saturation (0 → -40 over unease range)
  - Vignette (0.15 → 0.45)
  - Color temperature (+10 → -20)
  - Film grain (0 → 0.3)
  - Fog density (0.01 → 0.04)
- **Complexity:** High — multiple inputs feeding one variable, one variable driving multiple outputs
- **Uncanny because:** The space doesn't get worse because of one thing. It gets worse because of everything you do. The degradation is holistic and irreversible. By the time you notice, you're deep in it.

### 5.5 Light Failure Cascade
- **Input:** Timer (autonomous, random interval 30–60 seconds)
- **State:** After `unease` or `visitCount` crosses a threshold, the timer starts. Each tick picks a random tracked ceiling panel and permanently sets its emission to zero.
- **Relationship:** Unbound, one-shot per panel. State-gated start.
- **Output:** Individual ceiling panel emission → 0 (permanent)
- **Complexity:** High — state threshold, random selection, permanent change
- **Uncanny because:** The space is dying. Lights fail one by one. First one: huh. Third one: this is happening. Sixth one: darkness.

---

## Tier 6 — Feedback Loops and Progression

*The space evolves. Output feeds back to input. The system amplifies or dampens itself. Students learn: circular causation, emergent dynamics, pacing.*

**Feel: The space is closing in.**

### 6.1 The Panic Loop
- **Input:** Player velocity (continuous)
- **Relationship:** Bound — velocity → light flicker intensity. But flickering lights make the player want to run. Running increases velocity. Velocity increases flicker.
- **Output:** Light intensity oscillation amplitude + frequency. Also: footstep pitch drops (from Tier 2.3).
- **Feedback:** Positive loop. Capped by output range so it doesn't blow up.
- **Complexity:** High — feedback loop with cap
- **Uncanny because:** The space amplifies your anxiety. Running makes it worse. The only way to calm it is to stop — but the flickering makes stopping feel dangerous. The design traps you between two bad options.

### 6.2 Phase Shift
- **Input:** Accumulated exploration variable (from Tier 5.4 unease, or room count, or time)
- **State:** Thresholds on the variable define phases:
  - **Phase 1 (0–3):** Normal. Lights respond normally (Tier 1.1). Hum is present (Tier 1.2). Space is institutional.
  - **Phase 2 (3–6):** Lights are slightly wrong — envelope becomes asymmetric (slow attack). Hum pitch drops 3%. Subtle fog appears.
  - **Phase 3 (6–10):** Peripheral shift activates (Tier 3.3). Envelope asymmetry increases. Distant sounds start (Tier 3.2). Desaturation begins.
  - **Phase 4 (10+):** All interactions become aggressive — faster attacks, much slower releases. The space is clinging. Light failure cascade starts (Tier 5.5). Vignette tightens. Breathing walls are fully active but no longer shy.
- **Relationship:** State-driven parameter modification — same interactions, shifted parameters
- **Output:** Everything. The phase variable modifies attack/release/range/intensity of every interaction.
- **Complexity:** Very high — meta-system that modifies other systems
- **Uncanny because:** Same room. Same interactions. But the parameters shift. The space gets more aggressive, more sticky, more aware. By Phase 4, the space that once gently dimmed its lights when you approached now clings to you with slow releases and heavy envelopes.

### 6.3 The Infinite Staircase
- **Input:** TriggerSensor at bottom of stairs (binary, enter)
- **Relationship:** Unbound — teleport player back to top of stairs when they reach the bottom
- **Output:** Player position reset + brief screen black (2 frames, like Tier 3.6 blink)
- **State (optional):** Counter tracks loops. Each loop slightly modifies the stairwell — lights dimmer, hum louder, walls slightly narrower (scale 0.99^n)
- **Complexity:** Medium (basic teleport) to High (with accumulative changes)
- **Uncanny because:** Non-Euclidean space. You're going down but arriving at the top. The space loops. With accumulated state, each loop is subtly worse. The architecture is lying to you.

### 6.4 The Follower (Abstract)
- **Input:** Proximity to an abstract object (sphere, shadow, light anomaly)
- **Relationship:** Bound, inverse — the object follows you at a fixed distance (always N meters behind). Uses existing `Follow` module.
- **Feedback:** Your movement drives its movement. Its presence drives your anxiety. Your anxiety drives your movement.
- **Output:** The object's presence modifies local audio (low drone volume proportional to inverse distance) and vignette.
- **Complexity:** High — movement tracking, multiple output channels, psychological feedback
- **Uncanny because:** It never catches you. It never leaves. It's always exactly as far away as it wants to be. Running doesn't help because it maintains the distance. Stopping doesn't help because it stops too.

---

## Special / Atmosphere Layers (Always-On)

These are not interaction stations — they are persistent environmental systems that run throughout the scene.

### S.1 Ambient Hum Layer
- Always-on AudioSource with Backrooms ambience loop
- Volume driven by room — louder in open areas, quieter in corridors (proximity to walls drives low-pass filter)
- The baseline soundscape everything else sits on top of

### S.2 Dust Motes
- Subtle particle system, always on, very low emission (2–5/sec)
- Tiny size, slow drift, short lifetime
- Visible only in darker areas (where lights are dimmed by player presence)
- Positioned near ceiling lights

### S.3 Floor Fog
- Ground-hugging particle system in specific rooms/corridors
- Thin, white-gray, slow movement
- Emission rate can be bound to unease variable (more fog = deeper into dread)
- Uses existing Spawner or simple ParticleSystem

### S.4 Animated Surfaces
- Maksym Skrypka animated_wall and animated_floor shaders on select surfaces
- Subtle constant animation — the surface is alive
- Can be parameter-driven (animation speed bound to unease or proximity)

---

## Cross-Reference: By Output Domain

### Light / Emission
| Tier | Interaction | What it drives |
|---|---|---|
| 1.1 | Fluorescent Stalkers | Ceiling emission |
| 1.2 | The Hum | (audio, pairs with light) |
| 2.2 | Attention Leak | Wall panel emission |
| 2.6 | Fluorescent Startup | Ceiling emission flicker |
| 3.1 | The Flicker | Distant light oscillation |
| 5.1 | Dimming | Room light intensity (state) |
| 5.5 | Light Failure Cascade | Individual panel death |
| 6.1 | Panic Loop | Flicker amplitude from velocity |

### Sound
| Tier | Interaction | What it drives |
|---|---|---|
| 1.2 | The Hum | Volume + pitch (per-panel spatial) |
| 2.3 | Wrong Echo | Footstep pitch |
| 3.2 | Distant Door | One-shot slam (spatial, behind) |
| 3.4 | The Sigh | Ambient exhale swell |
| 3.7 | Stinger Events | Musical accents at spatial moments |
| 4.1 | The Stare Test | Low drone fade-in |
| 4.3 | Layered Room | Whispers on contact |
| 6.4 | The Follower | Low drone proximity |

### Post-Processing
| Tier | Interaction | What it drives |
|---|---|---|
| 2.4 | The Warm Spot | Color temperature |
| 4.1 | The Stare Test | Temperature shift cold |
| 5.4 | Accumulated Dread | Saturation, vignette, temperature, grain, fog |
| 6.1 | Panic Loop | (indirect via flicker anxiety) |
| 6.2 | Phase Shift | Everything modulated by phase |

### Material / Shader
| Tier | Interaction | What it drives |
|---|---|---|
| 1.4 | Carpet Memory | Floor _BaseColor |
| 2.2 | Attention Leak | Wall emission / decal shader |
| 2.5 | Dampened Wetness | Floor _Smoothness |
| 4.1 | The Stare Test | decal_eye reveal |
| 4.5 | Compound Gaze Reveal | animated_wall shader / dissolve |

### Transform / Spatial
| Tier | Interaction | What it drives |
|---|---|---|
| 1.3 | Breathing Walls | Wall scale pulse |
| 1.5 | Tracking Columns | Column rotation toward player |
| 3.3 | Peripheral Shift | Object position (on gaze lost) |
| 5.2 | The Rearrangement | Object position (between visits) |
| 6.3 | Infinite Staircase | Player teleport |
| 6.4 | The Follower | Object follows at fixed distance |

### Fog
| Tier | Interaction | What it drives |
|---|---|---|
| 1.6 | Proximity Fog | fogDensity |
| 2.1 | The Reluctant Corridor | fogDensity + fogColor |
| 4.3 | Layered Room | fogDensity (one of three layers) |

### Camera
| Tier | Interaction | What it drives |
|---|---|---|
| 3.6 | The Blink | Screen black (2 frames) |
| 6.3 | Infinite Staircase | Brief blackout on teleport |

### Particles
| Tier | Interaction | What it drives |
|---|---|---|
| 3.5 | Sonar Pulse | Sonar shader ring |
| 4.2 | Still Water | Water ripple particles |

---

## Build Priority

### Phase 1 — The Living Space (Tier 1, one session)
Build 1.1 (already done), 1.2, 1.4. The space responds to you. Feels alive but not threatening.

### Phase 2 — The Wrong Space (Tier 2, one session)
Add 2.1, 2.3, 2.5. The space is now wrong. Curves and envelopes create character.

### Phase 3 — The Unexplained (Tier 3, one session)
Add 3.1, 3.2, 3.4. Things happen without cause. First unbound interactions.

### Phase 4 — The Aware Space (Tier 4, one session)
Add 4.1, 4.3. The space has rules. Composition creates emergence.

### Phase 5 — The Remembering Space (Tier 5, one session)
Add 5.1, 5.4. The space remembers. Accumulated dread as the capstone state system.

### Phase 6 — The Closing Space (Tier 6, optional/advanced)
Add 6.1, 6.2. Feedback loops and phase progression. The space evolves.

---

## Notes

- Every interaction in this catalog uses the existing Ludocore sensor/module infrastructure.
- "Complexity" ratings assume students use the Replicate → Reconfigure → Recombine → Generate progression.
- Audio interactions require headphones. Flag this in the scene.
- The Backrooms audio library provides ready-made ambience, stingers, and entity sounds — students don't need to source audio.
- The Maksym Skrypka shaders provide animated surfaces and the eye decal — high-impact with minimal setup.
- The sonar shader is already in the project and provides a unique visual feedback mechanism.
- All post-processing interactions require a global URP Volume with overrides. One PostProcessingController script can expose all overrides as drivable floats.
