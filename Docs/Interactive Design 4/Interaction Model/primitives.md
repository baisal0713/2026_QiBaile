# Interaction Primitives

> A catalog of building blocks for the ID4 interaction lab.
> Lists every input, relationship configuration, and output primitive available to students.
> Reference document — not a scene design. The lab scene draws from this list.
> Last updated: March 2026.

---

## Inputs

An input is anything the system can read about the participant or the world. Each input produces either a **continuous** signal (a flowing value) or a **binary** signal (on/off).

### Spatial (body in space)

| Input | Signal | What it reads | Unity implementation |
|-------|--------|---------------|---------------------|
| **Proximity** | Continuous (distance) | How far the participant is from an object | ProximitySensor — OverlapSphere or collider distance |
| **Gaze direction** | Continuous (dot product) | How directly the participant is looking at an object | GazeSensor — dot product between camera forward and direction to target |
| **Gaze duration** | Continuous (seconds) | How long the participant has been looking at an object | GazeSensor — accumulated time while dot product exceeds threshold |
| **Presence** | Binary (inside/outside) | Whether the participant is inside a zone | TriggerSensor — OnTriggerEnter/Exit |
| **Contact** | Binary (touching/not) | Whether the participant is standing on or touching a surface | TriggerSensor on floor tile or surface collider |
| **Stillness** | Continuous (seconds) | How long the participant has been stationary | Custom — tracks velocity, counts seconds below threshold |
| **Velocity** | Continuous (speed) | How fast the participant is moving | CharacterController.velocity.magnitude |

### Direct manipulation (hands, controls)

| Input | Signal | What it reads | Unity implementation |
|-------|--------|---------------|---------------------|
| **Grab / hold** | Binary (holding/not) | Whether the participant is holding an object | XR Grab Interactable or custom pickup system |
| **Throw / release** | Binary (event) | The moment an object is released | OnRelease event from grab system |
| **Push / force** | Continuous (force) | How hard or fast a physics impact is | Collision.relativeVelocity.magnitude |

### Workspace UI (screen-space, raycast-driven)

| Input | Signal | What it reads | Unity implementation |
|-------|--------|---------------|---------------------|
| **Slider** | Continuous (0–1) | A direct value from a UI slider | Unity UI Slider |
| **Button** | Binary (press) | A discrete click event | Unity UI Button |
| **Toggle** | Binary (on/off) | A persistent on/off switch | Unity UI Toggle |
| **Dropdown** | Discrete (index) | A selection from a list | Unity UI Dropdown |

### Inspector (debugging and teaching)

| Input | Signal | What it reads | Unity implementation |
|-------|--------|---------------|---------------------|
| **SerializeField float** | Continuous | A value exposed in the inspector, adjustable at runtime | [SerializeField] float in custom controller |
| **SerializeField bool** | Binary | A toggle exposed in the inspector | [SerializeField] bool in custom controller |
| **AnimationCurve** | Continuous (shape) | A drawable curve in the inspector | [SerializeField] AnimationCurve |

Inspector inputs are not "interactions" in the experiential sense — they are diagnostic tools. Every custom controller should expose its key parameters as SerializeFields so students can tune and observe while in Play mode.

### Autonomous (no participant required)

| Input | Signal | What it reads | Unity implementation |
|-------|--------|---------------|---------------------|
| **Time** | Continuous (clock) | Elapsed time or oscillating cycle | Time.time, Mathf.Sin(Time.time * frequency) |
| **Random** | Continuous or binary | Noise or stochastic events | Random.Range, Perlin noise |

---

## Relationship Configurations

These are the common configurations of the transformation model — signal type × relationship type × envelope character. Not an exhaustive list, but the essential patterns that cover the vast majority of interactions students will build.

Each configuration is described abstractly. Any input can drive any output through any of these.

### Bound configurations

The output depends on the input. The system follows the participant.

| Configuration | Signal | Envelope | What it feels like |
|---------------|--------|----------|-------------------|
| **Linear tracking** | Continuous | Fast attack, fast release | Output mirrors input proportionally. Mechanical, direct, transparent. The default. |
| **Smoothed tracking** | Continuous | Slow attack, slow release (symmetric) | Output follows input but lags behind. Heavy, contemplative, underwater. |
| **Asymmetric tracking** | Continuous | Fast attack, slow release | Output catches up quickly but lingers when input retreats. Eager then sticky. |
| **Eased tracking** | Continuous | Fast attack, fast release + non-linear curve | Output follows input but the curve shapes the response — slow start, fast finish (or inverse). Organic, weighted. |
| **Inverted tracking** | Continuous | Fast attack, fast release + inverted curve | More input produces less output. Presence suppresses. The Rain Room principle. |
| **Binary snap** | Binary | Instant attack, instant release | Output jumps between two states. Crisp, mechanical, clear boundary. A light switch. |
| **Binary fade** | Binary | Slow attack, slow release (symmetric) | Output transitions gradually between two states. Atmospheric, gentle, zone-like. |
| **Binary asymmetric** | Binary | Fast attack, slow release | Snaps on, fades off slowly. The space lingers — remembers your presence briefly after you leave. |
| **Binary inverse asymmetric** | Binary | Slow attack, fast release | Fades on gradually, snaps off. Reluctant to respond, quick to forget. |

### Unbound configurations

The output is independent of the input after triggering. The system continues on its own.

| Configuration | Signal | Envelope | What it feels like |
|---------------|--------|----------|-------------------|
| **Burst** | Binary (event) | Instant attack, fast decay, no sustain | A flash. Instant peak, rapid falloff. Impact, collision, percussive. |
| **Swell** | Binary (event) | Slow attack, slow decay | A breath. Gradual rise to peak, gradual return. Organic, deliberate. |
| **Snap and tail** | Binary (event) | Instant attack, slow decay | Lightning and afterglow. Sharp onset, long lingering tail. |
| **Overshoot** | Binary (event) | Fast attack with decay, then settle | Output spikes past its target and bounces back. Elastic, alive, springy. |
| **Timed playback** | Binary (event) | Custom curve over duration | A designed temporal shape — the student draws the response as a curve over time. Full control. |

### Notes on configurations

These configurations are not types — they are **presets**. Every one is just a specific setting of curve, range, and envelope. Students should understand that the design space is continuous, not categorical. These presets are starting points and reference vocabulary, not boxes.

The coupling quality questions apply to every configuration: is this eager or reluctant, attentive or indifferent, precise or forgiving, sticky or crisp, alive or still?

---

## Outputs

An output is anything the system can change in the world. Organized by perceptual domain — what the participant experiences — not by Unity component hierarchy.

### Lighting

What the participant sees in terms of brightness and light quality.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Point / spot light intensity | How bright a light source is | Light | intensity, range |
| Light color / temperature | The warmth or coolness of a light | Light | color (lerp between values) |
| Light shadow | Shadow presence and softness | Light | shadowStrength |
| Emission intensity | Self-illumination of a surface | Material (URP Lit) | _EmissionColor (HDR multiplier) |
| Emission color | The hue of self-illumination | Material (URP Lit) | _EmissionColor |

### Material & Surface

What objects look and feel like — their surface qualities.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Base color | The main color of a surface | Material | _BaseColor |
| Smoothness | Matte to glossy | Material | _Smoothness (0–1) |
| Metallic | Non-metal to metal appearance | Material | _Metallic (0–1) |
| Alpha / opacity | Transparent to opaque | Material (Surface Type: Transparent) | _BaseColor.a or _Alpha |
| Dissolve | Gradual disappearance with edge effect | Material (Shader Graph) | dissolve threshold + edge color |
| Fresnel / rim glow | Edge glow based on view angle | Material (Shader Graph) | fresnel power |
| Normal map strength | Perceived surface bumpiness | Material | _BumpScale |
| Tiling / UV offset | Scrolling or shifting texture | Material | _MainTex_ST |

### Transform & Geometry

Physical changes to objects in space — position, rotation, scale.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Scale (uniform) | Object grows or shrinks | Transform | localScale (all axes) |
| Scale (per-axis) | Object stretches or squashes | Transform | localScale (individual axes) |
| Position | Object moves, drifts, orbits | Transform | localPosition / DOTween |
| Rotation | Object spins or turns | Transform | localRotation / Rotate() |
| Vertex displacement | Surface deforms (bulge, ripple, wave) | Shader Graph | displacement amount |

### Spawning & Instantiation

Objects appearing or disappearing from the scene.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Object activation | Showing/hiding existing objects | GameObject | SetActive(true/false) |
| Spawn | New objects appear in the scene | Custom Spawner | prefab, position, count, rate |
| Destroy | Objects are removed from the scene | GameObject | Destroy(gameObject, delay) |

### Particles & VFX

Ephemeral visual effects — clouds, trails, bursts, ambient texture.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Emission rate | How many particles per second | ParticleSystem | emissionRate |
| Particle size | How large individual particles are | ParticleSystem | startSize |
| Particle speed | How fast particles move | ParticleSystem | startSpeed |
| Particle color | The color or gradient of particles | ParticleSystem | startColor, colorOverLifetime |
| Particle shape | Where and how particles emit | ParticleSystem | shape module (cone, sphere, edge) |
| Burst | A one-time emission of N particles | ParticleSystem | emission.SetBursts() |
| Trail | Particles that follow movement | TrailRenderer or ParticleSystem trails | time, width, color gradient |

### Sound

What the participant hears. Requires headphones for spatial accuracy.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Volume | Loudness | AudioSource | volume (0–1) |
| Pitch | Frequency / speed of playback | AudioSource | pitch |
| Spatial blend | How positioned the sound is in space | AudioSource | spatialBlend (0 = 2D, 1 = 3D) |
| Low-pass filter | Muffled / clear | AudioLowPassFilter | cutoffFrequency |
| Reverb | Room character | AudioReverbZone | room, decayTime |
| Play / stop | Whether a sound is playing | AudioSource | Play(), Stop() |

### Environment & Atmosphere

Global changes to the scene — not tied to a single object.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Fog density | How thick the atmosphere is | RenderSettings | fogDensity |
| Fog distance | Where fog begins and ends | RenderSettings | fogStartDistance, fogEndDistance |
| Fog color | The color of the atmosphere | RenderSettings | fogColor |
| Ambient light intensity | Overall scene brightness | RenderSettings | ambientIntensity |
| Ambient light color | The tint of ambient light | RenderSettings | ambientLight |
| Skybox exposure | How bright the sky is | Skybox Material | _Exposure |
| Skybox tint | The color of the sky | Skybox Material | _Tint |

### Post-Processing (URP Volume)

Camera-level effects that change how the entire image looks.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Bloom intensity | Glow around bright areas | Volume → Bloom | intensity, threshold |
| Color temperature | Warm / cool shift of entire image | Volume → Color Adjustments | temperature |
| Saturation | Vivid / desaturated | Volume → Color Adjustments | saturation |
| Vignette | Darkened edges | Volume → Vignette | intensity |
| Depth of field | Focus / blur | Volume → Depth of Field | focalLength, aperture |
| Chromatic aberration | Color fringing at edges | Volume → Chromatic Aberration | intensity |
| Film grain | Texture / noise overlay | Volume → Film Grain | intensity |

### Camera

Changes to the participant's viewpoint itself.

| Output | What changes | Unity component | Key properties |
|--------|-------------|-----------------|----------------|
| Field of view | Wide / narrow view | Camera or Cinemachine | fieldOfView |
| Camera shake | Tremor or impact vibration | Cinemachine Impulse | amplitude, frequency, duration |
| Camera position | Viewpoint shifts | Cinemachine virtual cameras | priority switching, blend time |

---

## Notes on This Document

This is a **parts list**, not a design. It catalogs what is available. The lab scene will select from these primitives and combine them into stations — but that is a separate document.

Every output listed here is a float, a color, or a bool at the implementation level. This is what makes the transformation model universal: the relationship (bound/unbound, curve/range/envelope) works identically regardless of which specific output it drives. A light intensity and a particle emission rate are both just floats being shaped by the same mechanism.

The input categories (spatial, workspace UI, inspector, autonomous) reflect different **access modes** — different ways of feeding signal into the same system. A slider and proximity both produce a continuous float. A button and a contact zone both produce a binary event. The relationship doesn't care which one it came from.
