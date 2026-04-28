# Lecture 6 — Interaction Catalog

> All interactions use presence, gaze, contact, or stillness as input.
> No active interaction (grab, throw, press) — that's Lecture 7+.
> Each entry maps to the signal matrix and targets a specific Backrooms emotion.
> Every interaction is driven by a ScriptableObject profile — swap the profile, change the feel.

---

## Signal Matrix Overview

|  | **Bound** (output follows input) | **Unbound** (output plays independently) |
|---|---|---|
| **Continuous** | Columns, Proximity Fog, Proximity Hum, Proximity Chill, Dust Motes | Threshold Flicker |
| **Binary** | Zone Presence Hum, Gaze Drain, Gaze Glow, Floor Light | Room Entry, Contact Tone, Doorway Fog Pulse |
| **Continuous-as-threshold** | Stillness Dim, Stillness Drone | — |
| **Autonomous** | Breathing Light | — |

---

## Already Built

### 1. Column Glow
**`ColumnControllerV2` + `ColumnProfile`**

- **Input:** Proximity (continuous distance)
- **Relationship:** Bound
- **Output:** Material emission intensity + object scale
- **Matrix:** Continuous × Bound
- **Feel:** The columns notice you. Walk close, they brighten and grow. Walk away, they dim.
- **Profile controls:** Response curve, intensity range, scale range, attack/release speed
- **Profiles built:** Gentle (slow, subtle), Reactive (fast, dramatic)
- **Backrooms use:** Corridor columns that track you with light. With inverse curve: columns dim as you approach — the space pulls away from you.

### 2. Room Entry
**`Room1EntryControllerV2` + `Room1EntryProfile`**

- **Input:** TriggerSensor (binary — enter zone)
- **Relationship:** Unbound — fires once, plays to completion
- **Output:** Audio pitch ramp + ambient lighting + reflection intensity + ceiling emission (layered, staggered)
- **Matrix:** Binary × Unbound
- **Feel:** Cross a threshold and the room wakes up — sound, light, and emission arrive in a designed sequence.
- **Profile controls:** Per-channel curve, duration, delay
- **Profiles built:** Cinematic (slow stagger), Sudden (fast, compressed)
- **Backrooms use:** First room entry. The Backrooms "turn on" as you arrive. Different profiles change whether it feels like a welcome or a warning.

### 3. Stillness Dim
**`StillnessDimController` + `StillnessDimProfile`**

- **Input:** Player velocity (continuous, used as binary threshold)
- **Relationship:** Bound — tracks movement state
- **Output:** Ceiling emission + ambient intensity + reflection intensity
- **Matrix:** Continuous-as-threshold × Bound
- **Feel:** Stop moving and the space goes dark. Start moving and it wakes up. The space needs your motion to stay alive.
- **Profile controls:** Stillness threshold, dim delay/duration/curve, brighten duration/curve, target values per channel
- **Profiles built:** Creeping (slow dim, fast recovery), Nervous (fast dim, fast recovery)
- **Backrooms use:** The fluorescents only stay on if you keep walking. Stop and the hum dies, the glow fades. You are the power source.

### 4. Gaze Drain
**`GazeDrainController` + `GazeDrainProfile`**

- **Input:** GazeSensor (binary — looking/not looking)
- **Relationship:** Bound — ramps while gazing, recovers when looking away
- **Output:** Post-processing saturation + vignette
- **Matrix:** Binary × Bound
- **Feel:** Stare at something and the world drains of color, vision narrows. The space punishes your attention.
- **Profile controls:** Onset delay/duration/curve, release duration/curve, saturation range, vignette range
- **Profiles built:** Creeping (delayed onset, full drain), Sticky (fast drain, very slow recovery)
- **Backrooms use:** An object at the end of a corridor. Stare at it and the world goes monochrome. You can only cross safely by not looking.

---

## New Interactions — Students Build These

Each interaction below includes: what it does, where it sits on the matrix, what the profile SO would contain, and what different profiles feel like. Students write the spec, generate the controller and profile with AI, then create 2-3 profile presets and swap them.

---

### 5. Proximity Hum
**Continuous × Bound — Proximity → Sound**

A vent or pipe in the ceiling. Walk near it and you hear a low electrical hum. The closer you get, the louder and lower-pitched it becomes.

- **Input:** ProximitySensor (continuous distance)
- **Output:** AudioSource volume + AudioSource pitch
- **Components needed:** ProximitySensor on the vent, AudioSource with looping hum clip (spatial blend = 1.0)

**Profile: `ProximityHumProfile`**
- `maxDistance` (float) — detection range
- `responseCurve` (AnimationCurve) — distance → intensity mapping
- `volumeClose` / `volumeFar` (float) — volume range
- `pitchClose` / `pitchFar` (float) — pitch range (e.g., 0.85 close, 1.0 far)
- `attackSpeed` / `releaseSpeed` (float) — smoothing

**Profile presets:**
| Profile | Pitch range | Attack | Release | Feel |
|---|---|---|---|---|
| **Normal** | 1.0 → 0.95 | Fast | Fast | Realistic electrical hum. Grounding. |
| **Dread** | 1.0 → 0.7 | Slow | Very slow | Pitch drops dramatically. The hum follows you. |
| **Mosquito** | 0.8 → 1.5 | Fast | Fast | Pitch rises as you approach. Irritating, anxious. |

**Backrooms feel:** Every ceiling vent hums. The hum is the Backrooms' heartbeat. "Normal" establishes what sounds right. "Dread" on one specific vent tells you something is wrong with that spot.

**Teaching value:** Same input as columns (ProximitySensor), completely different output (audio instead of emission). Proves the sensor is reusable — the design lives in the mapping, not the sensor.

---

### 6. Proximity Fog
**Continuous × Bound — Proximity → Atmosphere**

Walk deeper into a corridor and the fog thickens. The far end disappears. Walk back and it clears.

- **Input:** ProximitySensor on a zone marker at the corridor's end (continuous distance)
- **Output:** RenderSettings.fogDensity + RenderSettings.fogColor

**Profile: `ProximityFogProfile`**
- `maxDistance` (float) — how far the fog starts responding
- `responseCurve` (AnimationCurve) — distance → fog mapping
- `fogDensityFar` / `fogDensityClose` (float) — e.g., 0.01 → 0.06
- `fogColorFar` / `fogColorClose` (Color) — e.g., yellow-white → gray
- `attackSpeed` / `releaseSpeed` (float) — smoothing

**Profile presets:**
| Profile | Density range | Color shift | Speed | Feel |
|---|---|---|---|---|
| **Reluctant** | 0.01 → 0.04 | Yellow → gray | Slow attack, medium release | The corridor resists. You have to push deep before it thickens. |
| **Aggressive** | 0.01 → 0.08 | Yellow → near-white | Fast attack, slow release | Fog rushes in. Leaving is slow — the fog doesn't want to let go. |

**Backrooms feel:** One corridor is foggier than the others. The fog is a bound response to your depth — not a static weather effect.

**Teaching value:** First interaction that drives RenderSettings (global state) proportionally from proximity. Students see that fog is just another float being shaped by the same model.

---

### 7. Gaze Glow
**Binary × Bound — Gaze → Material Emission**

Wall stains or marks. Look at one and it begins to glow. Look away and the glow lingers, then fades.

- **Input:** GazeSensor on the wall mark (binary — detected/not)
- **Output:** Material emission intensity on the wall panel

**Profile: `GazeGlowProfile`**
- `onsetDuration` (float) — how fast the glow ramps
- `onsetCurve` (AnimationCurve)
- `releaseDuration` (float) — how fast it fades
- `releaseCurve` (AnimationCurve)
- `emissionGazed` (float) — target emission intensity when looking
- `emissionRest` (float) — emission when not looking (usually 0)

**Profile presets:**
| Profile | Onset | Release | Feel |
|---|---|---|---|
| **Shy** | 2s, ease-in | 0.5s, ease-out | Slow to respond, quick to hide. The stain doesn't want you to see it glow. |
| **Sticky** | 0.3s, linear | 5s, ease-in | Snaps on fast, lingers long. The glow stays after you look away. Like it wanted to be seen. |

**Backrooms feel:** Scattered wall marks that only glow when watched. With a Sticky profile, you look at a stain, look away, and catch it still glowing in your peripheral vision. The Backrooms want your attention.

**Teaching value:** Same input as Gaze Drain (GazeSensor), different output (emission instead of post-processing). Same profile structure. Students see the pattern repeating.

---

### 8. Contact Tone
**Binary × Unbound — Contact → Sound**

Floor tiles that play a tone when you step on them. The tone plays to completion regardless of whether you stay or leave.

- **Input:** TriggerSensor on thin floor tiles (binary — enter)
- **Output:** AudioSource one-shot (spatial, 3D)

**Profile: `ContactToneProfile`**
- `responseCurve` (AnimationCurve) — time → volume shape of the tone
- `duration` (float) — how long the tone plays
- `delay` (float) — pause before tone starts
- `volumeMax` (float) — peak volume
- `pitchMin` / `pitchMax` (float) — random pitch range per trigger (variation)

**Profile presets:**
| Profile | Duration | Curve shape | Feel |
|---|---|---|---|
| **Burst** | 0.3s | Instant peak, fast decay | Percussive. The floor flinches. |
| **Swell** | 3s | Slow rise, slow fall | A breath. The tile exhales under your weight. |
| **Snap & Tail** | 4s | Instant peak, very long tail | Sharp onset, lingering reverb. Footsteps echo wrong. |

**Backrooms feel:** A corridor of tiles. Each step triggers a tone that fades at its own pace. With "Snap & Tail," walking down the corridor leaves a trail of overlapping, slowly-dying sounds behind you. You hear where you've been.

**Teaching value:** First unbound interaction students build. The key difference from bound: step on the tile and leave immediately — the tone still plays to completion. The output is independent of the input after triggering.

---

### 9. Zone Presence Hum
**Binary × Bound — Contact/Presence → Sound + Light**

Step into a room and a low ambient hum fades in, with a subtle light shift. Step out and it fades. The envelope defines the room's personality.

- **Input:** TriggerSensor on a room-sized trigger zone (binary — inside/outside)
- **Output:** AudioSource volume (looping ambient) + light intensity

**Profile: `ZonePresenceProfile`**
- `attackDuration` / `attackCurve` — how the room greets you
- `releaseDuration` / `releaseCurve` — how it lets you go
- `volumeInside` / `volumeOutside` (float)
- `lightIntensityInside` / `lightIntensityOutside` (float)

**Profile presets:**
| Profile | Attack | Release | Feel |
|---|---|---|---|
| **Switch** | 0.05s | 0.05s | Instant. Clinical. The room toggles. |
| **Atmospheric** | 2s, ease-in-out | 2s, ease-in-out | Slow crossfade. The room gradually acknowledges you. |
| **Clingy** | 0.2s | 6s, ease-in | Fast on, refuses to let go. Walk to the next room and hear the previous one still fading behind you. |

**Backrooms feel:** Each room has its own hum. "Clingy" rooms leave sonic trails — you walk forward but the hum behind you is still dying. The space remembers your presence.

**Teaching value:** Binary × Bound — the missing quadrant that completes the matrix. Binary doesn't mean boring. The envelope turns a simple in/out into three completely different emotional experiences.

---

### 10. Proximity Chill
**Continuous × Bound — Proximity → Post-Processing**

Walk toward a specific spot (a stain, a corner, an invisible zone) and the color temperature drops. The image shifts cold. Walk away and warmth returns.

- **Input:** ProximitySensor (continuous distance)
- **Output:** Volume Color Adjustments — temperature + optional film grain

**Profile: `ProximityChillProfile`**
- `maxDistance` (float)
- `responseCurve` (AnimationCurve)
- `temperatureFar` / `temperatureClose` (float) — e.g., 0 → -30
- `filmGrainFar` / `filmGrainClose` (float) — e.g., 0 → 0.3
- `attackSpeed` / `releaseSpeed` (float)

**Profile presets:**
| Profile | Temperature range | Film grain | Speed | Feel |
|---|---|---|---|---|
| **Subtle** | 0 → -15 | None | Medium | You don't notice it happening. Just a vague unease near that corner. |
| **Arctic** | 0 → -40 | 0 → 0.3 | Fast attack, slow release | Visible cold. The image turns blue and grainy. Like a security camera in a freezer. |

**Backrooms feel:** One corner of one room is cold. No visible reason. The temperature shift is slight enough to feel subliminal. Or with "Arctic" — a dead zone where the image degrades.

**Teaching value:** Combines ProximitySensor (same input as columns and fog) with post-processing (same output domain as Gaze Drain). Students see that any input can drive any output — the model is universal.

---

### 11. Stillness Drone
**Continuous-as-threshold × Bound — Stillness → Sound**

Stand still and a low drone fades in. The longer you stand, the louder and lower it gets. Move and it cuts. Same input as Stillness Dim, different output.

- **Input:** CharacterController velocity (threshold: moving/still)
- **Output:** AudioSource volume + pitch (looping drone clip)

**Profile: `StillnessDroneProfile`**
- `stillnessThreshold` (float)
- `onsetDelay` / `onsetDuration` / `onsetCurve`
- `releaseDuration` / `releaseCurve`
- `volumeStill` / `volumeMoving` (float)
- `pitchStill` / `pitchMoving` (float)

**Profile presets:**
| Profile | Onset | Release | Pitch | Feel |
|---|---|---|---|---|
| **Patient** | 3s delay, 4s duration | 1s | 1.0 → 0.7 | Waits a long time, then the drone creeps in. Rewards patience with dread. |
| **Nervous** | 0s delay, 0.5s | 0.3s | 1.0 → 0.9 | Instant response. Stop for half a second and the drone is there. Move and it snaps off. Jittery. |

**Backrooms feel:** Combine with Stillness Dim — stop moving and the lights dim AND a drone fades in. Two output channels, same input, reinforcing the same emotion: don't stop.

**Teaching value:** Demonstrates layering — two controllers sharing the same input (velocity) but driving different outputs (light vs. sound). The composition creates a feeling neither could alone.

---

### 12. Doorway Fog Pulse
**Binary × Unbound — Contact → Atmosphere**

Walk through a doorway trigger. A wave of fog thickens for 3 seconds, then slowly clears. One-shot — the fog pulse plays regardless of where you go after.

- **Input:** TriggerSensor in a doorframe (binary — enter)
- **Output:** RenderSettings.fogDensity (pulse up, then settle back)

**Profile: `FogPulseProfile`**
- `responseCurve` (AnimationCurve) — time → fog density shape (should rise then fall)
- `duration` (float) — total pulse length
- `delay` (float) — pause before pulse starts
- `fogDensityPeak` (float) — maximum fog during pulse
- `fogDensityRest` (float) — fog after pulse settles

**Profile presets:**
| Profile | Curve | Duration | Feel |
|---|---|---|---|
| **Cough** | Sharp spike, fast decay | 1.5s | Quick burst of fog. Like the doorway coughed. |
| **Tide** | Slow swell, slow decay | 6s | Fog rolls in like a wave, then recedes. Something stirred when you crossed. |

**Backrooms feel:** Walk through a doorway and for a few seconds, the corridor ahead disappears in fog. By the time it clears, you've forgotten which direction you came from. Spatial disorientation through a momentary atmospheric event.

**Teaching value:** Unbound interaction driving a global value (fog). The pulse curve is drawn in the inspector — students design the temporal shape of the response.

---

### 13. Floor Light
**Binary × Bound — Contact → Emission**

Thin floor tiles that glow while you're standing on them. Step off and the glow fades. With a slow release, you leave a trail of dimming footprints.

- **Input:** TriggerSensor on thin floor panels (binary — inside/outside)
- **Output:** Material emission intensity per tile (material instances)

**Profile: `FloorLightProfile`**
- `attackDuration` / `attackCurve`
- `releaseDuration` / `releaseCurve`
- `emissionOn` / `emissionOff` (float)
- `emissionColor` (Color)

**Profile presets:**
| Profile | Attack | Release | Feel |
|---|---|---|---|
| **Instant** | 0.05s | 0.05s | Hard switch. Diagnostic. The floor maps your position. |
| **Warm Trail** | 0.1s | 4s, ease-in | Snaps on, fades slowly. You leave glowing footprints that linger. You can see where you've been. |
| **Reluctant** | 1.5s | 0.3s | Slow to light up, quick to extinguish. The floor doesn't want to show you. |

**Backrooms feel:** A corridor of floor tiles with "Warm Trail." Each step lights up the tile, and the glow persists for seconds after you leave. Walking down the corridor, you can look back and see your path fading behind you. The space is recording you.

**Teaching value:** Binary × Bound with per-instance materials (like CeilingLightDimmer). The asymmetric envelope (fast attack, slow release) is the most expressive parameter — it's what makes the interaction feel alive vs. mechanical.

---

### 14. Threshold Flicker
**Continuous × Unbound — Proximity threshold → Light**

Walk within a certain distance of a specific ceiling panel, and a light two rooms away flickers violently for a few seconds, then settles. One-shot. Spatial separation between cause and effect.

- **Input:** ProximitySensor (continuous distance, used with ThresholdResponse)
- **Output:** Light intensity oscillation on a distant light

**Profile: `ThresholdFlickerProfile`**
- `flickerDuration` (float) — how long the flicker lasts
- `flickerFrequency` (float) — oscillations per second
- `flickerIntensityMin` / `flickerIntensityMax` (float)
- `settleIntensity` (float) — what the light holds at after the flicker
- `settleDuration` (float) — fade from flicker to settled state

**Profile presets:**
| Profile | Duration | Frequency | Feel |
|---|---|---|---|
| **Nervous** | 1s | 20Hz | Brief, fast flicker. Like the light flinched. |
| **Dying** | 5s | 3Hz + randomness | Long, slow flicker. The light is struggling to stay on. |

**Backrooms feel:** You walk past a column and a light far down the hall flickers. Was that you? The spatial gap between your action and the response creates doubt. With "Dying" — you keep triggering lights that can't stay on.

**Teaching value:** Continuous input reduced to a threshold event, firing an unbound response. Combines ProximitySensor + ThresholdResponse (already exists) with a new flicker controller. Spatial separation between trigger and output is a key Backrooms design principle.

---

### 15. Breathing Light
**Autonomous × Bound — Time → Light**

Lights that pulse slowly on their own. No player input. The space is alive independently.

- **Input:** Time (Mathf.Sin, autonomous)
- **Output:** Light intensity or ceiling emission

**Profile: `BreathingLightProfile`**
- `frequency` (float) — oscillation speed (0.2 = slow breath, 1.0 = anxious pulse)
- `intensityMin` / `intensityMax` (float)
- `curve` (AnimationCurve) — shape of the oscillation (sine, or custom — sharp inhale, slow exhale)

**Profile presets:**
| Profile | Frequency | Curve | Feel |
|---|---|---|---|
| **Sleeping** | 0.15 Hz | Smooth sine | Slow, even breathing. The space is at rest. Peaceful but wrong — lights don't breathe. |
| **Anxious** | 0.6 Hz | Sharp rise, slow fall | Fast inhale, slow exhale. The space is nervous about something. |

**Backrooms feel:** One room where the lights breathe. Not responding to you — just alive on their own. Combined with other bound interactions (columns, stillness dim), the autonomous breathing becomes the baseline against which your influence is measured.

**Teaching value:** No player input at all. The interaction model still applies: input (time) → relationship (bound to sine) → output (light). This proves the model is universal. Also: contrasts player-driven interactions. Some things in the space have their own rhythm.

---

## Suggested Build Order for Students

### Phase 1 — Instructor demos (first half of session)
Students see the profile swap workflow on already-built controllers:
1. Column Glow — swap Gentle/Reactive profiles
2. Stillness Dim — swap Creeping/Nervous profiles
3. Gaze Drain — swap Creeping/Sticky profiles

### Phase 2 — Students build (second half of session)
Pick one from each category:

**Easy (one input, one output, existing module patterns):**
- Gaze Glow (#7) — almost identical structure to Gaze Drain, different output
- Floor Light (#13) — TriggerSensor + emission, clear binary bound pattern
- Breathing Light (#15) — no sensor needed, just time + output

**Medium (new output domain or layered outputs):**
- Proximity Hum (#5) — first audio-output interaction
- Zone Presence Hum (#9) — two outputs (sound + light) from one input
- Contact Tone (#8) — first unbound interaction students build

**Ambitious (global state or composition):**
- Proximity Fog (#6) — drives RenderSettings
- Proximity Chill (#10) — drives post-processing from proximity
- Stillness Drone (#11) — layer with Stillness Dim for compound effect

### Phase 3 — Combination (last 15-20 minutes)
Students pick two interactions that share an input or output and run them simultaneously:
- Stillness Dim + Stillness Drone = lights die AND drone rises when you stop
- Proximity Hum + Column Glow = walk near a column and it glows AND hums
- Gaze Drain + Gaze Glow = look at a stain: world desaturates AND stain glows (it's feeding on your attention)
- Contact Tone + Floor Light = step on tile: it lights up AND plays a tone

---

## Input × Output Matrix (reference)

Students can use this to find combinations they haven't tried yet.

|  | **Emission** | **Light** | **Sound** | **Fog** | **Post-Process** | **Material** | **Transform** |
|---|---|---|---|---|---|---|---|
| **Proximity** | Columns ✓ | — | Hum (#5) | Fog (#6) | Chill (#10) | — | — |
| **Gaze** | Glow (#7) | — | — | — | Drain ✓ | — | — |
| **Contact** | Floor Light (#13) | — | Tone (#8) | Fog Pulse (#12) | — | — | — |
| **Presence** | — | Zone (#9) | Zone (#9) | — | — | — | — |
| **Stillness** | Dim ✓ | — | Drone (#11) | — | — | — | — |
| **Time** | — | Breathing (#15) | — | — | — | — | — |

Empty cells are design opportunities — "What would proximity → transform feel like? What about gaze → fog?"
