# P2 — Presence Room
**Lectures:** L4–L5
**Status:** L4 completed, L5 upcoming

## Description
A responsive space where the participant's body is the only input. No buttons, no grabbing — just being there. Proximity, gaze, stillness, and absence drive light, sound, material, and atmosphere. The room reads you. This project teaches that the quality of a single Input → Variable → Output chain is the entire art — the curve, the feel, the subtlety of the response.

## Interaction Core
- **Input:** Proximity, gaze, stillness, absence, contact (floor triggers)
- **Variable relationships:** Primarily Direct/Continuous (floats driving floats — distance controls brightness, emission, particle rate)
- **Output:** Emissive materials, light color/intensity, sound, particles, post-processing, atmosphere

## Interaction Palette
- Proximity → emissive intensity, light, sound, material color (built in L4)
- Binary → continuous response (ProximitySensor evolution, built in L4)
- Particles driven by proximity (emission rate, speed, size mapped to distance)
- Absence-driven growth (objects grow while player is far, freeze on approach)
- Gaze → dissolve/reveal (shader property driven by gaze duration)
- Stillness → atmospheric shift (post-processing transition rewards patience)
- Contact → floor ripple via particles (trigger zones on floor)

## Relevant Documents
- `../../Lecture 4/Lecture 4 Guide.md` — Pre-lecture planning guide, spec-driven AI workflow
- `../../Lecture 4/Lecture 4 raw_clean.txt` — Pivot from ecosystems to responsive spaces
- `../../Lecture 4/Lecture 4 summary.txt` — Summary of L4
- `../../Lecture 4/Lecture 4 critique.txt` — Critique with suggestions
- `../../_meta/framework_architecture.md` — Data/Simulation/Presentation layers
- `../../_meta/interaction-framework.md` — ProximityTrigger, GazeTrigger definitions

## Art References
- teamLab immersive installations
- Olafur Eliasson — Weather Project, Your Rainbow Panorama
- Random International — Rain Room
- United Visual Artists — responsive light installations

## Open Questions
- How many interaction channels per session (L5 plan)?
- Audio work blocked by missing headphones — resolved?
- Dark room + emissive materials + bloom as default visual language?
