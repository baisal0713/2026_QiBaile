# ID4 — Course Design Summary

## Identity

Interaction Design 4 at NABA, taught by Petar. Art and design students (8–12, no coding background) learn to treat interaction itself as creative material. The thesis: agency is art. We design what it feels like to be an agent in a responsive world.

## Tools & Method

Unity with the LudoCore no-code framework. AI-assisted development (GitHub Copilot). Students work in the inspector, never in code. They describe interactions as specs; AI generates the controllers. Progression: Replicate → Reconfigure → Recombine → Generate.

## Format

16 sessions × 2.5 hours = 40 total hours. Six instructor-led projects (L1–L13), personal projects (L14–L15), exam workshops (L17–L18).

## Conceptual Frameworks (in progress)

**PLAY** — compositional grammar (adapted from *Advanced Game Design*):
- **P**arts — objects, entities, variables that compose the system
- **L**oops — circular interactions between parts, feedback, emergent dynamics
- **A**ctions — operations on parts, rules, methods that change state
- **Y**ields — emergent properties, the "more than the sum of its parts"

**Input → Variable → Output** — the atomic interaction. Every interaction in every project follows this pattern. The design lives in how the variable relates input to output:
- **Direct/Continuous** — input drives output in real time (distance → brightness)
- **Threshold** — input crosses boundary, triggers discrete event
- **Accumulated** — input adds up over time toward a transformation
- **Conditional** — same input, different output depending on current state
- **Branching** — input causes irreversible fork, excludes other paths
- **Sequential** — input advances position in ordered series, gates progression

**Grammar / Vocabulary / Syntax** — three analytical layers:
- Vocabulary = catalog of possible inputs and outputs (the palette)
- Grammar = PLAY — how interactions compose into systems
- Syntax = Data / Simulation / Presentation — implementation architecture

## The Six Projects

| # | Project | Lectures | Primary Variable Mapping | The participant... |
|---|---------|----------|--------------------------|-------------------|
| P1 | Ecosystem | L1–L3 | Direct + Threshold | watches life emerge from rules |
| P2 | Presence Room | L4–L5 | Direct/Continuous | is sensed by the space |
| P3 | Active Interaction | L6–L7 | Threshold + Direct | acts on the world deliberately |
| P4 | Interaction + State | L8–L9 | Accumulated + Conditional | is remembered by the space |
| P5 | Narration & Choices | L10–L11 | Branching + Conditional | faces irreversible decisions |
| P6 | Progression | L12–L13 | Sequential (all types layered) | experiences transformation over time |

**Arc:** watch life → be sensed → act → be remembered → choose → transform.

## Cross-Cutting Concerns

- **Physical interfaces** (MIDI, keyboard, OSC): introduced in P5 as alternative input layer, not standalone project. Principle: design the interaction first, bind the input later.
- **NPCs / social agents**: deferred. Not fundamentally different from ecosystem creatures — more evolved sensing and response. Students encounter as reference, not required build.
- **Audio as primary material**: woven into all projects as response layer, never centered as sole focus.

## Recurring Lessons Learned

Sessions hold 2–3 milestones max (consistently plan 2–3× more than fits). Hardest content belongs in the middle of the session, not the end. Git never demonstrated live despite repeated intent. Homework improving but needs concrete deliverables. Spec-driven AI workflow introduced in L4 — reusable for all subsequent projects.

## Key Documents

- `course-overview.md` — course identity, constraints, objectives
- `framework_architecture.md` — Interaction Toolkit: Data/Simulation/Presentation, module conventions
- `interaction-framework.md` — triggers, actions, conditions, spine levels L0–L5
- `lecture-planning-lessons.md` — critical planning lessons, session checklist
- `presentation-outline-philosophy.md` — 19-slide deck: agency as art, enactivism, Nguyen, Campbell
- `why-agency-art.md` — full philosophical foundation
- `notes - curriculum.md` — 10 curriculum areas, what's cut, open questions
- `Projects/P1–P6/design.md` — per-project design space documents
