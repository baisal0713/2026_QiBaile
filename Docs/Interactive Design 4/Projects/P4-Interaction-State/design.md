# P4 — Interaction + State
**Lectures:** L8–L9
**Status:** Not started

## Description
The room remembers. Every interaction mode from P3 gains weight because actions now have consequences that persist. The same space on your second visit is different from your first — not because of a script, but because the system accumulated your behavior. Accumulated and conditional variable mappings appear. This is where interaction becomes personal.

## Interaction Core
- **Input:** All P3 inputs (grab, throw, place, activate) + revisiting, repeated contact, time spent
- **Variable relationships:** Accumulated (repeated actions build toward transformation), Conditional (same action, different result depending on current state)
- **Output:** Persistent environmental changes, erosion/growth, irreversible transformations, phase shifts

## Interaction Palette
- Visit memory — zones that know how many times you've entered them (first visit neutral, tenth visit transformed)
- Erosion and growth — surfaces wear with repeated contact, objects grow with each interaction
- Irreversible action — break an object, it stays broken; open a door, it never closes
- Accumulation threshold — FloatVariable tracking total interaction, gating macro-level room transformation
- Object persistence — place something, leave, come back, it's still there

## Relevant Documents
- `../../_meta/interaction-framework.md` — Variables (BoolVariable, IntVariable, FloatVariable), VariableTrigger, SetVariable/ModifyVariable actions, conditions system, BranchAction
- `../../_meta/framework_architecture.md` — Data layer (shared state), ScriptableObject variables

## Art References
- *Shadow of the Colossus* — garden loses vegetation silently as you kill colossi
- *The Stanley Parable* — narrator remembers your choices, space folds on itself
- Rafael Lozano-Hemmer, *Pulse Room* — heartbeats accumulate as pulsing lightbulbs
- Jason Rohrer, *Passage* — time and movement are irreversible

## Open Questions
- How to demonstrate persistence across "visits" in a single Unity session? Scene reload? Zone re-entry?
- What's the minimum state architecture students need to understand (variable + condition)?
- Does this project build on P3's scene or start fresh?
