# Lecture 4: Bodies in Space — Interactive Environments

## Overview

**Theme:** From living ecosystems to responsive spaces — the body as interface, the environment as instrument. How does a space know you're there, and what does it do with that knowledge?

**Duration:** ~2.5 hours

**Starting point:** Students have built autonomous ecosystems (Lectures 1–3). They understand sensors, energy, emergence, and the player's presence as a force. Now we shift: instead of a world that lives on its own, we build a world that **responds to you**.

**By the end:** Students have a responsive room with four layers of interaction — presence, gaze, contact, and pickup — each producing distinct environmental feedback (light, surface, sound, atmosphere). They've also learned to write specs and use AI to generate custom controllers.

---

## What's Already Built

| Component | What it does | Students used it? |
|-----------|-------------|-------------------|
| `ProximitySensor` | Detects objects by tag within radius (OverlapSphere) | Yes — from Lecture 3 |
| `GazeSensor` | Detects objects viewer is looking at (dot product + distance) | No — new this lecture |
| `TriggerSensor` | Detects objects entering/exiting trigger collider | No — new this lecture |
| `RaycastSensor` | Ray/sphere cast along forward axis, tracks hit point | No — new this lecture |
| `SensorResponse` | Bridges sensor state → UnityEvents (first detected, while detected, all lost) | No — new this lecture |
| `MaterialColor` | Animates material color property via DOTween | Yes — from Lecture 3 |
| `MaterialEmissionIntensity` | Animates emission glow intensity | Yes — from Lecture 3 |
| `MaterialFloat` | Animates any float shader property | No — new this lecture |
| `Scale` | Animates transform scale via DOTween | No — new this lecture |
| `Gate` | Boolean state holder, fires on change | No — new this lecture |

### What We Need to Build (in this lecture, via specs + AI)

| Module | Purpose | When |
|--------|---------|------|
| `LightControl` | Animate Light component (color, intensity, range) | Step 2 |
| `SoundPlayer` | Play/fade AudioSource with spatial blend | Step 4 |
| `AtmosphereControl` | Fog density/color, PP volume weight | Step 5 |

---

## Artist References (~10 min)

Open with the framing question: *"Last three lectures, the world lived on its own. You entered it, and your presence was a disturbance. Today: the world exists **for** you. It watches. It listens. It responds."*

Show 3 short clips (~2 min each):

### 1. Daan Roosegaarde — *Dune* (2006–ongoing)
Hundreds of light fibers along a public walkway. They glow and produce sound as people walk past. Presence → light + sound. The simplest version of what we're building today.

*"One sensor. One response. Hundreds of copies. That's it. And it feels alive."*

### 2. Random International — *Rain Room* (2012)
Rain falls everywhere in a dark room — except where you stand. Cameras track your position, shut off water nozzles above you. Presence → absence. You walk through rain without getting wet.

*"The space doesn't add something. It removes something. That's still a response. And arguably the most powerful one in this list."*

### 3. Chris Milk — *The Treachery of Sanctuary* (2012)
Three shadow panels. Panel 1: your silhouette dissolves into birds. Panel 2: you grow wings. Panel 3: you flap your arms and release birds upward. Same input (body), three escalating responses.

*"Same sensor — your body. But the mapping changes. The design isn't the technology. It's the relationship between what you do and what happens."*

### Key framing

*"Today's question: What does the space know about you? Four things:"*
1. **Presence** — you're near something
2. **Gaze** — you're looking at something
3. **Contact** — you're touching something
4. **Interaction** — you picked something up

*"And what can the space do with that knowledge? Also four:"*
1. **Light** — brightness, color, shadow
2. **Surface** — material, emission, transparency
3. **Sound** — tone, ambient, spatial
4. **Atmosphere** — fog, post-processing, sky

*"The design space is the matrix — any input can drive any output. Today we'll build that matrix."*

---

## Step 0: Scene Setup (~10 min)

**Goal:** A simple enclosed space with objects to interact with. Nothing fancy — a room, some pillars, moody lighting.

### Build the room

1. Create a new scene: **"Responsive Room"**
2. Build a simple enclosed space:
   - Floor: Plane, scale (5, 1, 5), dark material
   - Walls: 4 stretched cubes or a simple room model
   - Ceiling: optional (open ceiling = skybox visible, useful later for atmosphere)
3. Lighting:
   - Set ambient light low (dark blue or near-black)
   - One dim directional light (intensity 0.3)
   - The room should feel **dark but not black** — we're going to add light through interaction

### Add pillars

- Create a cylinder: scale (0.5, 2, 0.5)
- Give it a material with emission enabled (dark/off for now)
- Add a Point Light as child (intensity 0, range 5, warm color)
- Duplicate 6–8 times, spread around the room
- Make it a prefab: **"Pillar"**

### Add the player

- Add a first-person controller (Unity Starter Assets or simple capsule + camera + movement)
- Tag as **"Player"**
- Place at room entrance

### Test
- Walk around. Dark room, dark pillars, nothing responds. Good. *"This is your canvas. Right now the space is dead. Let's wake it up."*

---

## Step 1: Presence → Light (Generic Wiring) (~15 min)

**Goal:** Pillars glow when the player walks near them. First, we do it the "old way" — generic modules wired in Inspector.

**Concept:** This is the approach students already know from Lecture 3. Stack components, wire events. It works, but let's see what it feels like at scale.

### Wire it up on one pillar

1. Add `ProximitySensor` to the Pillar
   - Radius: **8**
   - Required tags: **["Player"]**

2. Add `SensorResponse`
   - Assign the `ProximitySensor`

3. Add `MaterialEmissionIntensity`
   - Assign the pillar's `Renderer`
   - Emission color: warm orange/gold
   - Target intensity: **3**
   - Duration: **0.8**

4. Wire in Inspector:
   - `SensorResponse.firstDetectedEvent` → `MaterialEmissionIntensity.Play()`
   - For fade-out, we need a second `MaterialEmissionIntensity` with target intensity 0
   - `SensorResponse.allLostEvent` → second `MaterialEmissionIntensity.Play()`

5. For the Point Light... we don't have a LightControl module yet. So we'd need to manually animate it somehow.

### Test
- Walk near a pillar. It glows. Walk away. It fades.

### The problem

*"It works. But look at this component stack:"*
- ProximitySensor
- SensorResponse
- MaterialEmissionIntensity (glow on)
- MaterialEmissionIntensity (glow off)
- And we still can't control the Point Light

*"Five components for one behavior. Now imagine doing gaze, contact, AND pickup on every pillar. That's 20 components per object. The Inspector becomes unreadable. There has to be a better way."*

---

## Step 2: The Spec-Driven Approach (~20 min)

**Goal:** Introduce specs and AI-generated controllers. Replace the 5-component stack with one clean script.

### The concept

*"Instead of wiring modules together in the Inspector, we're going to describe what we want in plain language — a spec — and let AI write a script that does exactly that. One script, one behavior, one name."*

### Write the first spec together

Do this on screen, live. Open a text file or notepad:

```
# GlowOnPresence

PURPOSE: Makes an object glow when the player is nearby.
LAYER: Presentation
USAGE: Add to any object with a Renderer and a child Point Light.

## References
- ProximitySensor (on same object — detects nearby objects by tag)
- Renderer (the object's mesh renderer)
- Light (child point light)

## Inspector Config
- emissionColor (Color, default warm orange)
- activeIntensity (float, default 3.0) — emission intensity when detected
- idleIntensity (float, default 0.0) — emission intensity when not detected
- activeLightIntensity (float, default 2.0) — point light intensity when detected
- idleLightIntensity (float, default 0.0) — point light intensity when not detected
- fadeSpeed (float, default 0.5) — animation duration in seconds

## Behavior
- On Awake: cache material instance, enable emission keyword
- Every frame: check if ProximitySensor.HasDetections
  - If yes and not already glowing: animate emission to activeIntensity,
    animate light intensity to activeLightIntensity, over fadeSpeed seconds (use DOTween)
  - If no and currently glowing: animate both back to idle values
- Use DOTween for smooth animation
- Follow Ludocore coding style: [SerializeField] private fields,
  PascalCase methods, namespace Ludocore
```

### Feed to AI

Paste the spec into GitHub Copilot / ChatGPT / Claude. The AI generates a script like:

```csharp
using DG.Tweening;
using UnityEngine;

namespace Ludocore
{
    /// <summary>Makes an object glow when the player is nearby.</summary>
    public class GlowOnPresence : MonoBehaviour
    {
        [Header("References")]
        [SerializeField] private ProximitySensor sensor;
        [SerializeField] private Renderer targetRenderer;
        [SerializeField] private Light pointLight;

        [Header("Settings")]
        [SerializeField] private Color emissionColor = new Color(1f, 0.6f, 0.2f);
        [SerializeField] private float activeIntensity = 3f;
        [SerializeField] private float idleIntensity = 0f;
        [SerializeField] private float activeLightIntensity = 2f;
        [SerializeField] private float idleLightIntensity = 0f;
        [SerializeField] private float fadeSpeed = 0.5f;

        private Material _material;
        private bool _isGlowing;
        private Tween _emissionTween;
        private Tween _lightTween;

        private void Awake()
        {
            if (targetRenderer)
            {
                _material = targetRenderer.material;
                _material.EnableKeyword("_EMISSION");
            }
        }

        private void Update()
        {
            if (!sensor) return;

            if (sensor.HasDetections && !_isGlowing)
            {
                _isGlowing = true;
                AnimateTo(activeIntensity, activeLightIntensity);
            }
            else if (!sensor.HasDetections && _isGlowing)
            {
                _isGlowing = false;
                AnimateTo(idleIntensity, idleLightIntensity);
            }
        }

        private void AnimateTo(float emission, float light)
        {
            _emissionTween?.Kill();
            _lightTween?.Kill();

            float current = GetCurrentIntensity();
            _emissionTween = DOTween.To(
                () => current,
                x => { current = x; _material.SetColor("_EmissionColor", emissionColor * x); },
                emission,
                fadeSpeed);

            if (pointLight)
                _lightTween = pointLight.DOIntensity(light, fadeSpeed);
        }

        private float GetCurrentIntensity()
        {
            Color c = _material.GetColor("_EmissionColor");
            float maxBase = Mathf.Max(emissionColor.r, Mathf.Max(emissionColor.g, emissionColor.b));
            if (maxBase <= 0) return 0;
            return Mathf.Max(c.r, Mathf.Max(c.g, c.b)) / maxBase;
        }

        private void OnDestroy()
        {
            _emissionTween?.Kill();
            _lightTween?.Kill();
            if (_material && Application.isPlaying) Destroy(_material);
        }
    }
}
```

### Compare

*"Look at the pillar now:"*

**Before (generic wiring):**
```
[Pillar]
  ├── ProximitySensor
  ├── SensorResponse
  ├── MaterialEmissionIntensity (glow on)
  ├── MaterialEmissionIntensity (glow off)
  └── ??? (no light control)
```

**After (spec-driven):**
```
[Pillar]
  ├── ProximitySensor
  └── GlowOnPresence
```

*"Two components. The script name tells you what it does. And it handles the light too."*

### Apply to all pillars

- Remove the old SensorResponse + double MaterialEmissionIntensity from the pillar
- Add `GlowOnPresence`, wire the 3 references
- Apply to prefab → all pillars update

### Test
- Walk through the room. Pillars glow as you approach, fade as you leave. A corridor of light follows you through the dark.

---

## Step 3: Gaze → Surface (~20 min)

**Goal:** Objects change appearance when you look at them. Introduce the GazeSensor and write a second spec.

### Introduce GazeSensor

Show the concept on the whiteboard or screen:

*"Presence asks: are you near? Gaze asks: are you looking? It's a cone from your eyes. If the object is inside the cone — you're gazing at it."*

Quick look at the component:
- `GazeSensor` on the object (not the player!)
- It automatically uses the main camera as "viewer"
- `threshold`: how directly you must look (0.9 = tight cone, 0.7 = wide)
- `maxDistance`: how far gaze reaches
- Same base class as ProximitySensor — same events, same `HasDetections`

*"The object asks: is the camera looking at ME? Each object answers independently. Self-contained."*

### Write the spec together

```
# RevealOnGaze

PURPOSE: Object surface changes when the player looks at it.
LAYER: Presentation
USAGE: Add to any object with a Renderer. The object reveals hidden
       details (emission, color shift) when gazed at.

## References
- GazeSensor (on same object)
- Renderer (mesh renderer)

## Inspector Config
- idleColor (Color, default dark gray)
- revealColor (Color, default white)
- emissionColor (Color, default cyan)
- revealEmission (float, default 2.0)
- idleEmission (float, default 0.0)
- revealSpeed (float, default 0.3)
- fadeSpeed (float, default 1.0) — slower fade out feels more lingering

## Behavior
- When GazeSensor.HasDetections becomes true:
  animate _BaseColor to revealColor over revealSpeed
  animate _EmissionColor to emissionColor * revealEmission over revealSpeed
- When HasDetections becomes false:
  animate _BaseColor back to idleColor over fadeSpeed
  animate _EmissionColor back to emissionColor * idleEmission over fadeSpeed
```

### Have students generate it

This is the first time students use the spec-driven workflow themselves:
1. Type or copy the spec
2. Feed to AI (Copilot, ChatGPT, Claude)
3. Save the generated .cs file in their project
4. Drop on a pillar alongside `GazeSensor`
5. Configure in Inspector

### Create "wall panels" to demonstrate gaze

- Add flat quads or cubes to the walls
- Give them a dark material
- Add `GazeSensor` (threshold: 0.85, maxDistance: 20) + `RevealOnGaze`
- When you look at a panel, it lights up. Look away, it slowly fades.

### Test

Walk through the room. Pillars glow when you're near (presence). Wall panels reveal when you look at them (gaze). Two layers of response, two completely different feelings.

*"Presence is passive — the space notices your body. Gaze is active — the space notices your attention. They feel different because the agency is different."*

---

## Step 4: Contact → Sound (~20 min)

**Goal:** Stepping on floor zones triggers sound. Introduce TriggerSensor and the SoundPlayer spec.

### Introduce TriggerSensor

*"Presence is a radius. Gaze is a cone. Contact is physical — you step on it, walk through it, collide with it."*

Quick look at the component:
- `TriggerSensor` requires a Collider with `isTrigger = true`
- Uses `OnTriggerEnter` / `OnTriggerExit`
- Same sensor base class — same `HasDetections`, same events

### Build floor zones

1. Create a flat cube: scale (2, 0.05, 2) — thin floor tile
2. Add a Box Collider, check `Is Trigger`
3. Give it a subtle material (slightly lighter than the floor)
4. Add `TriggerSensor`, required tags: **["Player"]**
5. Duplicate 5–6 times in a path across the room

### Write the SoundPlayer spec

```
# SoundPlayer

PURPOSE: Plays and fades an AudioSource with simple controls.
LAYER: Presentation
USAGE: Add to any GameObject with an AudioSource.

## References
- AudioSource (on same object)

## Inspector Config
- playOnEnable (bool, default false)
- fadeInDuration (float, default 0.5)
- fadeOutDuration (float, default 1.0)
- targetVolume (float, 0-1, default 0.8)

## Public Methods
- Play() — fade in to targetVolume over fadeInDuration
- Stop() — fade out to 0 over fadeOutDuration, then stop
- PlayOneShot(AudioClip clip) — play a clip once at targetVolume

## Behavior
- Play: if not playing, AudioSource.Play(), then DOTween volume
  from 0 to targetVolume
- Stop: DOTween volume to 0, on complete AudioSource.Stop()
- Expose UnityEvents: playedEvent, stoppedEvent
```

### Write the contact controller spec

```
# SoundOnContact

PURPOSE: Plays a sound and changes floor tile color when stepped on.
LAYER: Presentation
USAGE: Add to floor trigger zones.

## References
- TriggerSensor (on same object)
- SoundPlayer (on same object)
- MaterialColor (on same object, optional — for visual feedback)

## Inspector Config
- contactColor (Color, default white with low alpha)
- idleColor (Color, default dark)

## Behavior
- When TriggerSensor detects something: call SoundPlayer.Play(),
  animate material to contactColor
- When TriggerSensor loses all: call SoundPlayer.Stop(),
  animate material back to idleColor
```

### Students generate both scripts, wire them up

1. Generate `SoundPlayer` → add to floor tiles alongside an `AudioSource`
   - AudioSource: loop = true, spatial blend = 1.0 (3D), volume = 0
   - Assign an ambient tone/drone clip (provide a few .wav files)
2. Generate `SoundOnContact` → add alongside `TriggerSensor`
3. Each tile gets a different audio clip — walking across the room plays a spatial composition

### Test

Walk across the floor. Each tile you step on lights up and starts a sound. Step off, it fades. You're composing a soundscape by walking.

*"You're not pressing buttons. You're not choosing from a menu. You're playing the room with your feet."*

---

## Step 5: Pickup → Atmosphere (~25 min)

**Goal:** Pick up an object and the entire room transforms — fog, lighting, post-processing, color. This is the most dramatic interaction and the most complex to build.

### The concept

*"Presence, gaze, contact — those are about WHERE you are and WHAT you attend to. Pickup is about CHOICE. You take something. You carry it. The world knows what you chose."*

### Build pickup objects

Create 3 distinct objects on pedestals:
- **Warm Crystal** — orange/amber, rough shape
- **Cool Crystal** — blue/cyan, smooth shape
- **Dark Crystal** — purple/magenta, angular shape

Each will transform the room differently when picked up.

### Write the Pickup spec

```
# Pickup

PURPOSE: Raycast-based grab and drop system for first-person player.
LAYER: Simulation
USAGE: Add to the player's camera.

## References
- RaycastSensor (on same object — detects what player looks at)
- Transform holdPoint (empty child of camera, positioned in front)

## Inspector Config
- pickupRange (float, default 3.0)
- holdDistance (float, default 1.5)
- pickupKey (KeyCode, default E)
- pickupLayer (LayerMask — which objects can be picked up)

## State
- heldObject (GameObject, read-only) — currently held object, null if empty
- isHolding (bool, read-only)

## Public Methods
- TryPickup() — if RaycastSensor is hitting a valid object within range,
  pick it up (parent to holdPoint, disable collider/rigidbody)
- Drop() — release held object at current position
  (unparent, re-enable collider/rigidbody)

## Behavior
- Every frame: if pickupKey pressed and not holding → TryPickup()
- If pickupKey pressed and holding → Drop()
- While holding: held object follows holdPoint position (lerp)

## Events (UnityEvent)
- pickedUpEvent(GameObject) — fired when object is grabbed
- droppedEvent(GameObject) — fired when object is released
```

### Write the AtmosphereControl spec

```
# AtmosphereControl

PURPOSE: Animates fog, ambient light, and post-processing volume weight.
LAYER: Presentation
USAGE: Add to a manager object in the scene.

## Inspector Config
- fogColor (Color)
- fogDensity (float)
- ambientColor (Color)
- ppVolume (UnityEngine.Rendering.Volume, optional)
- ppWeight (float, 0-1)
- transitionDuration (float, default 2.0)

## Public Methods
- Apply() — animate all properties to configured values over transitionDuration
- Apply(float duration) — same with custom duration
- Reset() — animate back to initial values captured on Awake

## Behavior
- On Awake: capture current fog color, fog density, ambient color,
  PP weight as "initial" values
- Apply: use DOTween to animate RenderSettings.fogColor,
  RenderSettings.fogDensity, RenderSettings.ambientLight,
  and volume.weight to target values
- Reset: DOTween back to initial values
```

### Write the room controller spec

```
# CrystalRoomEffect

PURPOSE: When a crystal is picked up, transitions the room's atmosphere
         to match the crystal's mood.
LAYER: Simulation
USAGE: Add to each crystal object.

## References
- AtmosphereControl (a specific atmosphere preset for this crystal)

## Behavior
- Listen for Pickup.pickedUpEvent — if the picked object is this
  gameObject, call AtmosphereControl.Apply()
- Listen for Pickup.droppedEvent — if the dropped object is this
  gameObject, call AtmosphereControl.Reset()
```

### Scene setup

1. Enable fog in Lighting settings (start with low density, neutral color)
2. Add a Post-Processing Volume (Global) with a basic profile:
   - Bloom (low intensity)
   - Color Adjustments (neutral)
   - Vignette (subtle)
3. Create 3 `AtmosphereControl` objects, each configured differently:

| Crystal | Fog Color | Fog Density | Ambient | PP Feel |
|---------|-----------|-------------|---------|---------|
| Warm | Orange-amber | 0.04 | Warm gold | Bloom up, warm tint |
| Cool | Deep blue | 0.02 | Cool blue | Bloom soft, blue tint |
| Dark | Purple-black | 0.08 | Near-black | Vignette strong, desaturate |

### Students generate scripts, assemble

1. Generate `Pickup` → add to player camera with `RaycastSensor`
2. Generate `AtmosphereControl` → create 3 instances with different presets
3. Generate `CrystalRoomEffect` → add to each crystal
4. Tag crystals on a "Pickup" layer, set `pickupLayer` on Pickup component

### Test

Walk to a pedestal. Look at the crystal. Press E. Pick it up. The entire room shifts — fog rolls in, light changes, the mood transforms. Drop it. The room breathes back to normal. Pick up a different crystal. A completely different world.

*"Same room. Same walls. Same pillars. But the object you chose changed everything you see and hear and feel. That's what interaction design means — the mapping IS the art."*

---

## Step 6: Free Combination & Tuning (~15 min)

**Goal:** Students recombine and customize. This is their creative time.

### Suggestions

- **Layer interactions**: pillar glows on presence AND changes pattern on gaze
- **Cross-wire outputs**: picking up the warm crystal makes all pillar glows warmer
- **Add more contact zones**: floor tiles that change the room's ambient sound
- **Combine contact + gaze**: a wall panel that only reveals when you're standing on a specific tile AND looking at it (use `Gate` to combine conditions)
- **Add motion**: pillars that physically move (Scale, Rotate) when approached, not just glow

### The matrix

Encourage students to think in terms of the input/output matrix:

|  | Light | Surface | Sound | Atmosphere |
|--|-------|---------|-------|------------|
| **Presence** | Pillar glow ✓ | ? | ? | ? |
| **Gaze** | ? | Panel reveal ✓ | ? | ? |
| **Contact** | ? | Tile color ✓ | Tile sound ✓ | ? |
| **Pickup** | ? | ? | ? | Room transform ✓ |

*"You've filled four cells. There are twelve more. Each one is a design decision. Which feel interesting? Which feel redundant? That's your judgment as a designer."*

---

## Step 7: Discussion & Reflection (~10 min)

### Look back at the references

- **Dune** = Presence → Light. One cell in the matrix, repeated hundreds of times.
- **Rain Room** = Presence → Atmosphere (absence of rain). Still one cell.
- **Treachery of Sanctuary** = Contact → Surface + Motion. Same input, escalating outputs.

*"These artists didn't fill the whole matrix. They found one or two cells and made them extraordinary. Quality of the mapping matters more than quantity."*

### The philosophical question

*"There are two kinds of space: a space you walk through, and a space that walks with you. After today, you know how to build the second kind. The question isn't what CAN you make the space do — it's what SHOULD it do? What does the response mean?"*

### Connect forward

*"Next time, we'll go deeper into how these responses can tell stories — spaces that remember what you did, that change permanently, that have a beginning and an end. Narrative in space."*

---

## Homework

### Required
- Complete the Responsive Room with at least 3 of the 4 interaction types (presence, gaze, contact, pickup)
- Write at least one original spec (not from class) and generate a controller with AI
- Each interaction must produce a visible/audible response

### Stretch
- Fill more cells in the matrix — combine inputs with new outputs
- Add a second room connected by a doorway, with a different mood/response set
- Make the crystals affect pillar behavior (warm crystal → pillars pulse faster, cool crystal → pillars breathe slowly)
- Use `Counter` or `Gate` to create compound conditions (requires BOTH gaze AND presence)
- Add creature elements from Lectures 1–3: a plant that only grows where you've walked, an entity that flees your gaze

---

## Session Notes for Instructor

### Pacing
- **Step 0** (scene setup) should be fast — have a starter scene ready if students are slow with room building
- **Steps 1–2** (generic → spec-driven) are the pedagogical pivot. Don't rush Step 2 — the spec-writing skill is what students take forward
- **Steps 3–4** (gaze + contact) are the hands-on core. Students should be generating their own scripts by Step 3
- **Step 5** (pickup + atmosphere) is the most complex. Some students may not finish — that's fine, it becomes homework
- **Step 6** (free combination) can expand or contract based on time

### Common issues to anticipate
- **GazeSensor not detecting**: threshold too high (0.95 = nearly exact aim). Lower to 0.7–0.8 for early testing
- **TriggerSensor not firing**: collider not set to `Is Trigger`, or player has no Rigidbody/CharacterController
- **Audio not spatial**: AudioSource spatial blend must be 1.0 for 3D sound. Also check AudioListener is on the player camera
- **Fog not visible**: check Lighting Settings → Fog is enabled. URP: may need to enable fog in the URP asset
- **Material emission not visible**: needs emission enabled in material AND the Global Illumination → Realtime GI or post-processing bloom to glow
- **AI-generated code doesn't compile**: most common issue is missing `using` statements or wrong namespace. Teach students to read the error, not fear it

### Key callbacks to prior lectures
- Lecture 1: Grammar/Vocabulary — sensors are grammar (rules), responses are vocabulary (actions)
- Lecture 3: ProximitySensor, MaterialEmissionIntensity — same tools, new context
- Lecture 3: "Your presence changed the ecosystem" → now "your presence changes the room"

### What's new in this lecture
- **GazeSensor** and **TriggerSensor** — two new sensor types
- **Spec-driven workflow** — the big methodological shift
- **AI as creative tool** — not just autocomplete, but architectural partner
- **Responsive environments** — from autonomous systems to reactive spaces
- **The input/output matrix** — a design framework they'll use for the rest of the course

### Forward threads for Lecture 5
- State and memory — spaces that remember what you did (permanent changes, not just reactive)
- Narrative progression — sequences, arcs, beginnings and endings in interactive space
- Multiple rooms / spatial narrative — different spaces with different rules
- Sound design deeper — reactive ambient layers, musical interaction
