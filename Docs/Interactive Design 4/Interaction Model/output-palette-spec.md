# Output Palette — Scene Spec

> A static reference scene showing what each output domain looks and feels like across its range.
> No interaction, no scripts. Just objects with different parameter values — perceptual calibration.

---

## Purpose

Before designing relationships (input → output), students need to know what the output space feels like. What does light intensity 3 vs 5 look like? What does smoothness 0.2 vs 0.8 feel like on a surface? This scene answers those questions through direct comparison.

## Project Context

- **Unity URP project**
- **Scene location:** `Assets/_Lab/` (alongside `_Lab_Primitives.unity`)
- **Scene name:** `_Lab_OutputPalette`
- First-person controller for walkthrough (use Starter Assets FPS prefab from `Assets/Starter Assets/`)
- Dark ambient environment (low ambient light, dark floor/walls) so output values are clearly visible
- Bloom enabled in a global URP Volume (makes emission visible)

## Layout Principle

Each output domain = one **row** of identical objects.
Each object in the row = one value in the range.
Objects are spaced ~2m apart, with a small world-space label above each showing the parameter name and value.

Rows are spaced ~5m apart so they don't bleed into each other visually.

Labels can be simple TextMeshPro (world-space, small, readable at ~3m). Format: `property: value` (e.g., `intensity: 3.0`).

---

## Rows to Build

### Row 1 — Light Intensity
- 5 Point Lights on short pedestals (cubes), warm white color
- Values: **0.5, 1, 2, 4, 8**
- Range 5, same color for all
- Dark surroundings so the pool of light is the content

### Row 2 — Emission Intensity
- 5 cubes with identical emissive material (white or warm orange)
- Emission intensity values: **0, 0.5, 1, 3, 6**
- Requires: material instances (not shared), `_EMISSION` keyword enabled, HDR emission color = baseColor * intensity
- Bloom makes this glow visibly

### Row 3 — Emission Color
- 5 cubes, all at emission intensity 3
- Colors: **warm orange, cool cyan, magenta, green, white**
- Shows the expressive range of emission hue

### Row 4 — Base Color Gradient
- 6 spheres, all same smoothness (0.5) and metallic (0)
- Colors: **black → dark gray → mid gray → light gray → white, plus one saturated color**
- Shows how base color reads under the scene lighting

### Row 5 — Smoothness
- 5 spheres, same base color (mid-gray), metallic 0
- Smoothness values: **0, 0.25, 0.5, 0.75, 1.0**
- Shows matte → mirror progression

### Row 6 — Metallic
- 5 spheres, same base color (mid-gray), smoothness 0.5
- Metallic values: **0, 0.25, 0.5, 0.75, 1.0**
- Shows dielectric → conductor progression

### Row 7 — Alpha / Transparency
- 5 cubes, material surface type set to **Transparent**
- Alpha values: **1.0, 0.75, 0.5, 0.25, 0.1**
- Place a bright-colored plane behind the row so transparency is visible

### Row 8 — Scale
- 5 identical cubes (same material)
- Uniform scale values: **0.3, 0.6, 1.0, 1.5, 2.5**
- All resting on the same floor plane (aligned at base, not center)

### Row 9 — Particle Emission Rate
- 5 particle systems, identical settings except emission rate
- Rates: **2, 10, 30, 80, 200** particles/sec
- Use simple upward-drifting white particles, short lifetime (~2s)
- Same start size, speed, color

### Row 10 — Particle Size
- 5 particle systems, same emission rate (20/sec)
- Start sizes: **0.05, 0.1, 0.2, 0.5, 1.0**
- Shows how particle scale changes perceived density/weight

---

## Rows NOT Included (and why)

| Domain | Why deferred |
|--------|-------------|
| **Sound** | Requires headphones + interaction to compare. Will be in the input palette or a separate audio palette. |
| **Fog / Atmosphere** | Global effect — can't show multiple values side by side. Needs interactive toggle. |
| **Post-Processing** | Global — same issue. Needs A/B switching, not static comparison. |
| **Camera** | FOV/shake are per-camera. Deferred. |
| **Position / Rotation** | Spatial — meaningful only in motion. Deferred to interaction stations. |

---

## Scene Setup Checklist

1. Create new scene `_Lab_OutputPalette` in `Assets/_Lab/`
2. Dark floor plane (scale 20x20), dark material
3. Optional low walls or columns to separate rows visually
4. Directional light at low intensity (~0.3), slightly warm
5. Global URP Volume with Bloom enabled (intensity ~1, threshold ~1)
6. Place FPS controller at one end
7. Build rows sequentially along one axis (a walkable corridor of output references)
8. Each row gets a header label: larger TextMeshPro with the domain name ("LIGHT INTENSITY", "EMISSION", etc.)

## What This Is NOT

- Not interactive (no sensors, no controllers, no scripts)
- Not the interaction palette (that comes later, with relationships)
- Not exhaustive (we can add rows later — dissolve, fresnel, normal map strength, etc.)
- Not precious — this is a calibration tool, not a finished artwork
