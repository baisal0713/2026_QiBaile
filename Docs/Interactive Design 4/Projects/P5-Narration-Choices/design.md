# P5 — Narration & Choices
**Lectures:** L10–L11
**Status:** Not started

## Description
Deliberate, visible, irreversible decisions through diegetic interfaces — world-space buttons, objects on altars, physical levers. Branching paths, mutually exclusive outcomes, the weight of choosing. This project layers everything — presence, physics, memory, progression — but adds moral or aesthetic gravity. Also introduces narration: how to convey story, context, and consequence through the space itself. Physical interfaces (MIDI, keyboard, OSC) introduced here as an alternative input layer.

## Interaction Core
- **Input:** Deliberate choices via diegetic controls (levers, altars, placements), physical interfaces
- **Variable relationships:** Branching (input causes irreversible fork), Conditional (same space, different state based on prior choices)
- **Output:** Divergent spatial configurations, narrative text/voice, mutually exclusive environmental states

## Interaction Palette
- Diegetic choice interfaces — world-space buttons, altars, levers, pressure plates
- Branching paths — BranchAction checks variable, routes to mutually exclusive outcomes
- Narration delivery — world-space text, environmental storytelling, triggered voice/text
- Consequence visibility — the space shows what you chose and what you lost
- Physical interface layer — MIDI controller, keyboard, OSC as alternative inputs to the same variable pipeline

## Relevant Documents
- `../../_meta/interaction-framework.md` — BranchAction, conditions system, SequenceAction, InputTrigger
- `../../_meta/framework_architecture.md` — Data layer for branching state
- `../../_meta/presentation-outline-philosophy.md` — Agency as art, the weight of decisions

## Art References
- *Papers, Please* — moral weight through bureaucratic interaction
- *The Stanley Parable* — branching, narration, the space remembers and comments
- *Before Your Eyes* — involuntary input (blinking) drives irreversible narrative
- *Her Story* — non-linear narrative assembled through player investigation

## Open Questions
- How to handle narration technically — world-space TextMeshPro? Audio triggers? Both?
- How much branching is feasible in 2 sessions (2 branches? 3?)?
- Physical interfaces: do students bring controllers, or is one demo unit shared?
- Is this where NPCs/social agents could optionally appear (narrator character)?
