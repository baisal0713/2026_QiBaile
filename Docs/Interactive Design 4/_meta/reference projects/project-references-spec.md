# Project References — Selection Spec

> We need ~10 real-world interactive artworks/experiences to serve as the basis for tutorial projects.
> Each will be reimagined in Unity as a small, buildable project that teaches specific interaction areas at a specific spine level.

---

## Selection Criteria

Every reference artwork MUST satisfy ALL of the following:

### 1. Agency is central, not decoration
The participant DOES something, and that doing is the core of the work — not a secondary feature layered onto a visual installation. If you could remove the interaction and the work would still "work" as a video or photo, it fails this test.

**Test**: Can you describe the work by describing what the participant *does* and what *happens as a result*? If the description is just "you stand in a room and it's beautiful" — reject.

### 2. Reimaginable in Unity by students
The core interaction can be distilled into a small Unity project achievable in ~2-3 hours of guided work. It doesn't need to look like the original — it needs to *feel* like the same interaction principle.

**Test**: Can you describe the Unity reimagination in one sentence? "First-person, you walk toward NPCs and they dissolve on approach" = good. "Full-body motion capture with real-time fluid simulation" = not buildable.

### 3. Maps to a specific spine level
The interaction logic of the reference should clearly sit at one of the spine levels:

| Level | What it means | What the reference should demonstrate |
|-------|--------------|--------------------------------------|
| L0 Reaction | trigger → action | Single clear cause-effect interaction |
| L1 Sequence | A then B then C | The experience has phases or progression |
| L2 State | variables change outcomes | Same action behaves differently based on context |
| L3 Branching | choices create divergent paths | Participant decisions lead to different experiences |
| L4 Feedback Loops | action → world change → new conditions | Circular dynamics, the interaction sustains itself |
| L5 Interconnection | systems influence each other | Emergence from multiple interacting subsystems |

### 4. Exercises specific interaction areas
The reference should naturally require 1-3 interaction areas from the vocabulary, so students practice those areas while building the project.

### 5. Notable / real / citable
Should be a known work by a recognized artist or studio, or a notable indie game/experience. Students gain cultural literacy alongside technical skill. Obscure is fine if the work is genuinely good — but "I saw it at a festival once and can't find documentation" is too thin.

### 6. Emotionally / conceptually legible
The work should have a clear expressive intent that students can grasp quickly. "This is about loneliness." "This is about revealing the invisible." "This is about the weight of choice." The concept should be statable in one sentence.

### 7. Variety across the set
The full set of ~10 references should cover:
- [ ] Different spine levels (not all L0-L1)
- [ ] Different interaction areas (not all just proximity triggers)
- [ ] Different emotional registers (not all melancholy)
- [ ] Different spatial types (open environments, enclosed spaces, abstract voids, populated scenes)
- [ ] Different participant roles (explorer, destroyer, caretaker, witness, intruder)

---

## What We're NOT Looking For

- Pure visual installations with no meaningful interaction (Kusama infinity rooms, Turrell light spaces)
- Works where "interaction" means "your body is tracked and visuals change" with no agency structure (most teamLab)
- Multiplayer/social works that can't be reduced to single-participant Unity projects (Abramovic's relational works)
- Works that require hardware we can't simulate (haptics, smell, full-body tracking)
- AAA games — too complex to distill into a 2-hour project

---

## Reinterpretation is Valid

Not every reference needs to be an interactive work in the first place. A strong visual/spatial artwork with no interaction can be *reinterpreted* through interaction — the question becomes: "What if the participant had agency in this?" This is itself a design exercise.

Examples:
- Kusama's infinity rooms are passive — but what if your movement created or destroyed the reflections?
- Turrell's light spaces are contemplative — but what if the light responded to your pace, your stillness, your gaze?
- Eliasson's Weather Project is atmospheric — but what if the sun's behavior was driven by collective participant action?

The reinterpretation approach can work especially well for:
- Teaching students to **identify where agency could live** in a passive work
- Giving them a strong aesthetic/atmospheric starting point to build interaction *into*
- Practicing the core question: "What does the participant DO here, and why does it matter?"

When evaluating these, the criteria shift slightly — the reference provides the **aesthetic and spatial concept**, and the student/instructor provides the **interaction design**. The evaluation template should note whether the reference is being used as-is or reinterpreted.

---

## What We ARE Looking For

- Works where the participant's actions carry meaning
- Works where the *type* of interaction is the expressive tool (not just the visuals)
- Works that can be distilled to a single clear interaction principle
- Works spanning the range from simple (one trigger, one poetic response) to systemic (multiple dynamics creating emergence)
- Works from interactive art, art games, indie games, installations, experimental media — any field as long as the interaction is designed

---

## Evaluation Template

For each candidate reference:

```
**Title**:
**Artist/Studio**:
**Year**:
**What the participant does**: (describe the actions, not the visuals)
**What happens as a result**: (describe the system response)
**Core interaction principle**: (one sentence)
**Spine level**: L0 / L1 / L2 / L3 / L4 / L5
**Interaction areas used**: (from the 8 areas)
**Expressive intent**: (what it's "about" in one sentence)
**Unity reimagination**: (one-sentence description of the student project)
**Feasibility**: (can students build this in ~2-3 hours guided?)
```

---

## References Already on the Table

### Strong candidates (agency is central):

**Nouliness** (your own microgame)
- Walk toward NPCs, they dissolve on approach. World empties irreversibly.
- Spine: L3 (Branching/Memory — irreversible state change)
- Areas: NPCs, environment, character control
- About: loneliness, the impossibility of connection

**The Unfinished Swan** (Giant Sparrow, 2012)
- Throw paint into a white void to reveal the world. You can only see what you've marked.
- Spine: L2 (State — the world accumulates your actions)
- Areas: physics, environment, sensory feedback
- About: discovery, making the invisible visible

**Beyond Eyes** (Team17, 2015)
- Play as a blind girl. The world only renders around you, based on sound and proximity. What you imagine isn't always what's there.
- Spine: L2-L3 (State + mismatch between expectation and reality)
- Areas: environment, character control, sensory feedback
- About: perception, vulnerability, the gap between imagination and reality

**Lozano-Hemmer — Pulse Room** (2006)
- Participant holds a sensor. Their heartbeat drives a lightbulb. The bulb joins a room of hundreds of other visitors' recorded heartbeats.
- Spine: L1-L2 (Sequence + state accumulation)
- Areas: input design, environment, sensory feedback
- About: presence, the trace of being alive

**Chris Milk — The Treachery of Sanctuary** (2012)
- Three panels. Your shadow transforms: first into birds scattering, then birds attacking, then wings growing from your arms.
- Spine: L1 (Sequence — three phases)
- Areas: character control, environment, VFX/feedback
- About: creation, destruction, transcendence

### Weaker candidates (need scrutiny):

**Rain Room** — interaction is too thin (binary: present/absent). Visually spectacular but agency-flat.

**teamLab — Flowers and People** — responsive but not agentic. The system reacts to presence but there's no designed choice or consequence.

**Olafur Eliasson — The Weather Project** — no interaction at all. Great atmosphere reference, not an interaction model.

**Janet Cardiff — sound walks** — interesting (narrative + movement) but hard to distill into a Unity project without the physical site.

**Marina Abramovic** — relational, requires another human. Not reducible to single-participant Unity.

### Gaps to fill:
- [ ] Need a strong L0 reference (pure reaction, poetic simplicity)
- [ ] Need L4 references (feedback loops)
- [ ] Need L5 references (interconnected systems, emergence)
- [ ] Need references that exercise physics, UI interaction, NPC behavior specifically
- [ ] Need at least one reference with a different participant role (not just "explorer walking through space")

---

## Next Step

Search for and evaluate candidate artworks to fill the gaps above. For each, fill in the evaluation template and assess against the 7 criteria.
