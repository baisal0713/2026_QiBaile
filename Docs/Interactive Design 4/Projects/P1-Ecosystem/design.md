# P1 — Ecosystem
**Lectures:** L1–L3
**Status:** Completed

## Description
A self-regulating multi-species ecosystem. Students build autonomous creatures that sense, pursue, flee, consume, and self-replicate — then observe emergent behavior arise from simple rules. The player enters as a disturbance, not a controller. This is PLAY at full density: many Parts with Actions forming Loops that Yield emergence.

## Interaction Core
- **Input:** Autonomous agent sensors (proximity detection between species)
- **Variable relationships:** Direct (energy depletes over time), Threshold (death on zero energy, replication on full energy)
- **Output:** Movement, consumption, population dynamics, visual energy feedback

## Interaction Palette
- Timer lifecycle (energy depletion)
- Scale animation (growth)
- Spawner (population seeding)
- NavMesh navigation (pursuit, flee)
- Proximity sensing between species (predator–prey–flora)
- Self-replication on energy threshold
- Player presence as disturbance (creatures flee player)

## Relevant Documents
- `../../Lecture 1/Lecture 1 raw_clean.txt` — Framework introduction, Game of Life, cellular automata
- `../../Lecture 1/Lecture 1 summary.txt` — Analytical summary of L1
- `../../Lecture 2/Lecture 2 raw_clean.txt` — 6-step staircase build
- `../../Lecture 2/Lecture 2 summary.txt` — Summary of L2
- `../../Lecture 3/Lecture 3 Guide.md` — Pre-lecture planning guide for ecosystem build
- `../../Lecture 3/Lecture 3 raw_clean.txt` — Flora, Fauna, Predator, 3-organism cascade
- `../../Lecture 3/Lecture 3 raw_teachersummary.txt` — Teacher summary of L3
- `../../_meta/framework_architecture.md` — Interaction Toolkit architecture (Data/Simulation/Presentation)
- `../../_meta/interaction-framework.md` — Full framework with triggers, actions, spine levels

## Art References
- Conway's Game of Life
- Boids (Craig Reynolds)
- Ecosystem simulations

## Open Questions
- Could a student replicate this from scratch as a personal project baseline?
- What's the minimum viable ecosystem (2 species or 3)?
