# Curriculum — 16 Lectures

> **Multimedia Design 4: Interaction Design for Artists**
> 16 sessions x 2.5 hours = 40 hours total
> Students: last-year artists/designers. Already completed 2 Unity courses (editor, 3D, lighting, materials, FPS controllers, animation, basic VR).
> What they lack: designing interaction as expression, complex interaction logic, multi-system integration, installation practice, authored agency.

---

## The Two Axes

This curriculum is built on two axes from `notes-curriculum-thinking.md`:

**The Spine — Interaction Complexity (vertical progression)**
How complex is the *logic* of the interaction?

```
L0  Reaction        → trigger → action. Stateless. One-shot.
L1  Sequence         → A then B then C. Phases. The experience goes somewhere.
L2  State            → The world remembers. Same action, different outcome.
L3  Branching        → Choices matter. Consequences. Irreversibility.
L4  Feedback Loops   → Action changes world changes conditions for action. Circular.
L5  Interconnection  → Multiple systems influencing each other. Designed emergence.
```

**The Areas — Interaction Vocabulary (horizontal material)**
What does the participant interact *with*?

```
Tier 1 (simpler):   Object manipulation, Environment shifts, Sensory feedback
Tier 2 (mid):       UI interaction, Character control (advanced), Physics
Tier 3 (complex):   NPCs / agents, Narrative / progression logic
Transversal:        Input design, Installation practice
```

The spine advances through the course. Areas are layered in as the spine deepens. "Authored agency" is the design lens applied at every level, not a separate topic.

---

## Session Structure (recurring)

| Block | Duration | What happens |
|-------|----------|--------------|
| **Reference + Theory** | ~20 min | Analyze 1–2 reference artworks through the spine lens: what spine level is this? What areas does it use? What agency does it design? |
| **Spine Concept** | ~15 min | Introduce the session's complexity layer. How does today's logic level deepen what came before? |
| **Technique / Tutorial** | ~40 min | Guided implementation using the no-code framework + Unity. Students build inside the session's example project. |
| **Make + Mentorship** | ~50 min | Diverge from the example. Apply to personal project. Roaming individual mentorship. |
| **Share / Critique** | ~15 min | Quick share. "What did you do? What did that feel like? Could it be a video?" |

---

## Progression Overview

| Phase | Sessions | Spine Level | Focus |
|-------|----------|-------------|-------|
| **1. Foundations** | 1–4 | L0 → L2 | Course thesis + framework. Reaction, sequence, state. Tier 1 areas. |
| **2. Depth** | 5–8 | L2 → L4 | Complex logic + Tier 2–3 areas. Branching, feedback loops. |
| **3. Integration** | 9–11 | L4 → L5 | Interconnection. Multi-system projects. Prototype milestone. |
| **4. Production** | 12–16 | — | Project work, testing, polish, critique, final. Progressively relaxed. |

Personal project work starts from session 1. By session 9, direction is locked. By session 11, working prototype.

---

## PHASE 1: FOUNDATIONS

---

### Lecture 1 — Agency as Art + The Framework

**Spine level:** L0 — Reaction (trigger → action, stateless)

**Theme:** The course thesis. Interactive art sculpts what it feels like to be an agent. The no-code framework is how we build it.

**Theory:**
- Nguyen's core claim: the medium is agency itself
- Goals, abilities, constraints → temporary agency
- The Nouliness test: could this be a video? If yes, it's not yet interaction design
- Show 2–3 works and analyze: what spine level? What areas? What agency?

**Unity / Framework:**
- Introduction to the no-code interaction framework: triggers, actions, events
- The trigger-action pattern: proximity trigger → change color / play sound / toggle object
- Build the simplest possible interaction: enter a zone, something responds
- (Students already know the Unity editor — this is framework orientation, not editor orientation)

**Possible reference projects:**
- *Passage* (Jason Rohrer) — a 5-minute life. Walk right, age, die. Total meaning through minimal interaction. **Spine: L1 (sequence) but analyzable at L0.**
- *September 12th* (Gonzalo Frasca) — fire missiles, create more terrorists. The political argument IS the interaction. **Spine: L4 (feedback loop), but the surface interaction is L0 (click → missile).**
- *Boundary Functions* (Scott Snibbe) — stand in a room, Voronoi diagrams of personal space appear. Only exists with people present. **Spine: L0 (pure reaction) — but the meaning is social.**

> **NOTE:** The in-class example project for this session will be designed later. It should be a minimal trigger-action scene built with the framework — enter a zone, something changes. The reference projects above are for analysis/discussion, not reproduction.

**Student output:** First framework interaction. Homework: describe an interaction you've experienced that could NOT be a video.

---

### Lecture 2 — Sequence: The Experience Goes Somewhere

**Spine level:** L1 — Sequence (ordered chain, phases, linear progression)

**Theme:** A single reaction is a toy. A *sequence* of reactions is an experience. Things unlock. Stages progress. The world transforms step by step.

**Theory:**
- From reaction to sequence: A then B then C
- Pacing: when to advance, when to hold, when to withhold
- The participant as traveler through designed phases
- Analyze a reference work: where are the phases? What triggers each transition?

**Areas introduced:** Object manipulation + Environment shifts

**Unity / Framework:**
- Sequencing triggers: chained events, delays, ordered unlocks
- Timed triggers: things that happen after a duration
- Object manipulation: transforms (move, rotate, scale), spawning from prefabs, destroying, enable/disable
- Environment shift basics: lerping light color, fog density, skybox blend — the world changes in phases

**Possible reference projects:**
- *The Unfinished Swan* (Giant Sparrow) — each chapter introduces a new way your throws reveal the world. Clear phase progression through a single verb.
- *Gris* (Nomada Studio) — colors return in sequence. Each color unlocks abilities and transforms the landscape. Environment-as-inner-state, phased.
- *Night Walk* (Moment Factory) — a path with zones. Walk here → the forest lights up. Walk further → fog rolls in. Linear sequence, rich environmental transformation.

> **NOTE:** The in-class example project will be designed later. It should be a multi-phase scene where the participant's actions advance the experience through 3–4 distinct stages, using object manipulation and environment shifts.

**Student output:** A sequenced interaction — something that goes somewhere, with at least 3 phases.

---

### Lecture 3 — State: The World Remembers

**Spine level:** L2 — State (variables, conditionals, different outcomes from same action)

**Theme:** The most powerful moment in interaction design: doing the same thing twice and getting a different result. The world has memory now. It knows what you've done.

**Theory:**
- State = the world has variables: visited/unvisited, alive/dead, 0/1/2/3
- Same trigger, different response depending on conditions
- Accumulation: each action changes the conditions for the next action
- The participant realizes: "my actions have consequences that persist"

**Areas deepened:** Object manipulation + Sensory feedback (feedback now varies with state)

**Unity / Framework:**
- State variables: int, bool, float flags tracked by the framework
- Conditional triggers: "only fire if X is true" / "respond differently based on count"
- Feedback that reflects state: sound pitch rises with count, particles grow denser, environment darkens
- Introduction to the state-driven feedback loop: action → state change → feedback changes → participant adjusts behavior

**Possible reference projects:**
- *Wooden Mirror* (Daniel Rozin) — 830 tiles whose rotation state is driven by camera input. The "state" is the current image. Every pixel = a variable.
- *Reactive Table* (teamLab) — flowers grow where you've touched, accumulate, decay over time. The table remembers your history of contact.
- *Walden, a game* (Tracy Fullerton) — the world's color saturation tracks your attention. Rush and it grays. Slow down and it blooms. Movement speed IS a state variable that drives the entire aesthetic.

> **NOTE:** The in-class example project will be designed later. It should be a scene where the same action produces different results depending on accumulated state — a world that remembers.

**Student output:** An interaction with memory. The participant does something, the world changes, and the next time they do the same thing, the response is different.

---

### Lecture 4 — Movement as Expression

**Spine level:** Still L2 (State) — but applied to how the participant's *body* exists in the space.

**Theme:** Your students already have FPS controllers. This session asks: what does the movement *mean*? Speed, weight, camera behavior, and spatial constraint are expressive tools, not defaults.

**Theory:**
- Walking as design decision: Dear Esther's walk-only, Walden's speed-as-aesthetics
- Constraint as expression: what you CAN'T do shapes agency (Journey: no speech)
- Camera as mood: FOV, head-bob, post-processing, Cinemachine behaviors
- Movement parameters that change with state: you slow down as the world decays, you speed up as it wakes

**Areas introduced:** Character control (advanced — beyond basic FPS)

**Unity / Framework:**
- Custom movement tuning: speed curves, acceleration, drag as expressive parameters
- Cinemachine: camera behaviors that respond to state (damping, FOV shifts, follow offsets)
- State-driven movement: movement parameters that change based on world-state variables
- Spatial gating: areas that open/close based on state, participant count, or accumulated actions
- Movement + feedback coupling: footstep sounds, camera effects, particles tied to movement

**Possible reference projects:**
- *Dear Esther* (The Chinese Room) — WASD + look = the entire design. The decision to remove every other verb IS the artistic statement.
- *Journey* (thatgamecompany) — movement constraints (limited flight, momentum on sand) create emotional arcs. An anonymous stranger can join, but you can only chirp.
- *Flower* (thatgamecompany) — the character IS wind. Tilt to steer, touch flowers to bloom the world. Movement and environmental transformation are the same action.

> **NOTE:** The in-class example project will be designed later. It should be a walkable space where movement parameters (speed, camera, spatial access) are expressive choices tied to world-state — not engine defaults.

**Student output:** A space where how you move, where you can go, and what the camera does are deliberate, state-aware design choices.

---

## PHASE 2: DEPTH

---

### Lecture 5 — Branching: Choices That Matter

**Spine level:** L3 — Branching (divergent paths, consequences, irreversibility)

**Theme:** The participant makes a choice. The world forks. Some things can't be undone. History accumulates. Two people who play the same work have different experiences.

**Theory:**
- Branching ≠ dialogue trees. Branching = any moment where accumulated state creates divergent outcomes
- Irreversibility: the participant realizes "I can't go back." This is when agency becomes serious.
- Value clarity (Nguyen): the seduction of crisp choices. And its danger: value capture.

**Areas introduced:** UI interaction (choices need interfaces)

**Unity / Framework:**
- Branching logic: conditional paths based on accumulated state variables
- World-space UI: buttons, labels, prompts that exist IN the 3D world (diegetic interfaces)
- Choice presentation: how to surface a decision without breaking immersion
- Irreversible state changes: destroying objects permanently, one-way environment shifts
- UI as meaning: the interface itself communicates (a clinical menu vs. a hand-written note)

**Possible reference projects:**
- *Papers, Please* (Lucas Pope) — stamp APPROVED or DENIED. Each stamp is irreversible. The desk interface IS the moral engine.
- *Kentucky Route Zero* (Cardboard Computer) — choose dialogue, but choices define who the characters ARE, not where the plot goes. Authorship through selection.
- *The Stanley Parable* (Galactic Cafe) — obey or disobey. The game forks on compliance vs. defiance. The narrator is the system, the player is the disruptor.

> **NOTE:** The in-class example project will be designed later. It should present the participant with a meaningful, irreversible choice that changes the world-state and subsequent experience — using world-space UI as the choice surface.

**Student output:** An interaction with at least one meaningful fork. Two participants who make different choices have different experiences.

---

### Lecture 6 — Physics as Expression

**Spine level:** L3 (Branching) continues — physics outcomes branch based on how force is applied.

**Theme:** Physics isn't realism — it's feel. Weight, bounciness, friction, and force are expressive parameters. The gap between what you intend and what happens is where comedy, tragedy, and meaning live.

**Theory:**
- Physics as medium: Katamari's clumsy rolling, Octodad's impostor-body, Forsythe's Tumble Room
- Feel: mass, drag, bounce encode emotional register — a heavy world vs. a floaty world
- Emergence through physics: simple rules → unpredictable, unrepeatable behavior
- Physics branching: the same throw produces different results every time

**Areas introduced:** Physics interactions

**Unity / Framework:**
- Rigidbody tuning: mass, drag, gravity scale as expressive choices
- Physics materials: bounce, friction — surfaces that feel different
- Forces: AddForce, impulse, attraction/repulsion fields
- Joints: hinge, spring, fixed — connecting objects into physical systems
- Physics + state: objects that accumulate, collapse, pile up based on participant actions
- The ragdoll as expressive tool

**Possible reference projects:**
- *Tumble Room* (William Forsythe) — your body displaces hundreds of suspended balloons. You ARE a force in a physics field.
- *Katamari Damacy* (Keita Takahashi) — clumsy rolling, scale progression, accumulation. One mechanic, cosmic scope.
- *Getting Over It* (Bennett Foddy) — one tool (hammer), one physics system. Frustration and persistence as designed experience. The physics ARE the philosophy.

> **NOTE:** The in-class example project will be designed later. It should be a scene where physics parameters are deliberate expressive choices — not default settings — and where the participant's force produces emergent, unrepeatable outcomes.

**Student output:** A physics-driven interaction where weight, bounce, and force are tuned for feel, not realism.

---

### Lecture 7 — Characters and Conversation

**Spine level:** L3 → L4 transition — NPCs introduce branching that feeds back. The NPC remembers, and its behavior changes your options.

**Theme:** An NPC is any entity that responds with apparent intention. It doesn't need to be human, or even visible. A forest can be an NPC. A narrator can be an NPC. The room itself can behave like a character.

**Theory:**
- The NPC spectrum: scripted → branching → stateful → emergent
- Dialogue as identity (KRZ) vs. dialogue as moral weight (Papers Please) vs. dialogue as negotiation (Stanley Parable)
- Non-verbal NPCs: entities that respond through movement, sound, or environmental behavior
- NPC + state: the character that remembers what you've done and treats you differently

**Areas introduced:** NPCs / agents + Narrative logic

**Unity / Framework:**
- Simple NPC state machine: idle → alert → responding → retreating (via framework or Animator)
- Dialogue integration: Ink or Yarn Spinner — branching text with variables
- NPC memory: tracking relationship variables, referencing past player choices
- NavMesh basics: NPCs that move to/from the participant
- Trigger-based NPC behavior: proximity, gaze, action → NPC response with state awareness
- Animation integration: NPC states drive animations

**Possible reference projects:**
- *Florence* (Mountains) — micro-interactions as relationship moments. Speech bubbles as puzzles that get easier as comfort grows. Wordless NPC design.
- *The Stanley Parable* (Galactic Cafe) — the narrator is the NPC. It reacts to your compliance or defiance. Agency as negotiation with a system.
- *Eliza* (Zachtronics) — read the script or go off-script. The gap between the machine's words and your judgment IS the interaction.

> **NOTE:** The in-class example project will be designed later. It should feature at least one entity with stateful behavior — an NPC, narrator, or environment-as-character that remembers and responds differently over time.

**Student output:** A scene with an entity that responds to the participant with memory and apparent intention.

---

### Lecture 8 — Feedback Loops: The Interaction Sustains Itself

**Spine level:** L4 — Feedback loops (action changes world → world changes conditions for action → circular, self-sustaining)

**Theme:** The most powerful interactions are not linear — they are circular. The participant acts, the world changes, the changed world alters what the participant can or wants to do, and the cycle continues. The interaction breathes.

**Theory:**
- Positive feedback loops: the more you do X, the more X intensifies (escalation, addiction, collapse)
- Negative feedback loops: the more you do X, the harder X becomes (balance, homeostasis, resistance)
- Loop as metaphor: "the more you explore, the more the world decays" IS a statement about extraction
- Designing loops that produce meaning, not just engagement

**Areas revisited:** All Tier 1 areas (object, environment, feedback) now in loop configuration

**Unity / Framework:**
- Systems that feed back: action → state change → environment shift → new trigger conditions
- Variables that drive multiple systems: a single "decay" variable affects light, audio, NPC behavior, and movement speed simultaneously
- Balancing loops: tuning escalation/resistance curves
- Time-based feedback: things that change whether or not the participant acts (decay, growth, cycles)
- Audio mixing as loop indicator: the soundscape reflects the current state of the feedback system

**Possible reference projects:**
- *September 12th* (Frasca) — fire missiles → civilians die → mourners become terrorists → more targets → fire more missiles. A feedback loop that IS the political argument.
- *Outer Wilds* (Mobius Digital) — the solar system runs on a 22-minute loop. You die, you restart, but you KNOW more. Knowledge is the only persistent variable in an otherwise resetting world.
- *Flower* (thatgamecompany) — bloom flowers → world turns green → more flowers appear → more to bloom. Positive restoration loop. Your agency heals the landscape, and the healing creates more agency.

> **NOTE:** The in-class example project will be designed later. It should feature a self-sustaining interaction loop where the participant's actions change the world in a way that changes the conditions for their next action.

**Student output:** An interaction that feeds back on itself — where the world's response to the participant changes what the participant does next.

---

## PHASE 3: INTEGRATION

---

### Lecture 9 — Interconnection: Everything Talks to Everything

**Spine level:** L5 — Interconnection (multiple systems influencing each other, designed emergence)

**Theme:** Real interactive works are ecosystems. The physics affects the NPCs. The NPCs affect the environment. The environment affects the feedback. The feedback affects the participant's movement. Everything is connected — and moments the designer didn't script emerge from the connections.

**Theory:**
- Designed emergence: setting up conditions for unscripted moments (Indra's Net from Campbell)
- The ecosystem model: multiple systems with interfaces between them
- When to connect and when to isolate: not everything should talk to everything
- Journey, teamLab Borderless, and Flower as case studies in multi-system integration

**Unity / Framework:**
- Event buses / message systems: how systems communicate without hard dependencies
- Shared state variables: one variable drives physics, lighting, audio, and NPC behavior
- Scene architecture for complex interactions: organizing many systems cleanly
- Performance awareness: keeping frame rate stable when everything is responsive
- The integration checklist: for each system, ask "what feeds into it? What does it feed into?"

**Possible reference projects:**
- *Journey* (thatgamecompany) — movement (sand physics) + environment (wind, light) + feedback (music swells) + social (anonymous companion) — all interconnected, all responsive.
- *teamLab Borderless* — works flow between rooms. Touch affects flowers, flowers affect water, water affects creatures. No boundaries between systems.
- *Rain World* (Videocult) — a full ecosystem simulation. Predators hunt prey, weather cycles affect behavior, the player is just another creature in an indifferent world.

**Activity:** Project concept lock-in. Each student presents: what agency am I designing? What spine level does my project operate at? What systems are connected? Group feedback and instructor scope adjustment.

**Student output:** Final project direction declared. A system diagram showing which interaction areas are connected and how.

---

### Lecture 10 — Input Design + Installation Practice

**Spine level:** Transversal — not a new complexity layer, but essential practical knowledge.

**Theme:** Your interaction will exist in a physical space — a gallery, an installation, a screen in a room. The input device, the display, the physical setup are all design decisions. And: what happens when it crashes at 3am?

**Theory:**
- Input design: mouse/keyboard as dev stand-in. The real input might be a MIDI controller, a sensor, a camera, a custom object.
- The simulated-UI-to-real-device pipeline: design the interaction first, bind the input later
- Installation robustness: auto-launch, crash recovery, kiosk mode, multi-display
- Right-sizing for installations (Nguyen): museum visitors aren't gamers. Immediately graspable but deep enough for genuine agency.

**Unity / Framework:**
- Input System: abstracting input so one interaction works with keyboard, controller, or custom device
- OSC/MIDI integration basics: receiving external input
- Build settings: fullscreen, resolution, target platform
- Auto-launch and crash recovery: making a build that runs unattended
- Multi-display considerations
- Testing outside the editor: the build IS the artwork

**Possible reference projects:**
- *Rain Room* (Random International) — the input is your body's position. The output is absence of rain. The installation must run 12 hours a day without crashing.
- *Pulse Room* (Lozano-Hemmer) — the input is a heart-rate sensor. 300 lightbulbs must respond reliably. A single point of failure kills the piece.
- *Line Wobbler* (Robin Baumgarten) — the input IS a door-stopper spring. Custom hardware, single LED strip. The physical device and the game are inseparable.

> **NOTE:** The in-class example project will be designed later. It should involve building a standalone installation-ready build from a student's existing project, and mapping inputs to an alternative device (or simulated alternative input).

**Student output:** A standalone build of their project. Input abstracted so it could work with a non-keyboard device. Awareness of installation requirements.

---

### Lecture 11 — Prototype Review

**Spine level:** All levels — applied critique.

**Theme:** Is your prototype actually interactive, or is it an interactive illustration? The Nouliness test, applied to your own work. And: value clarity vs. value capture — are you simplifying your own work in ways that flatten it?

**Theory:**
- Nguyen's warning: value capture — when simplified metrics replace rich experience
- Applied critique: is the feedback loop meaningful, or just "juicy"?
- The Nouliness test on student work: could this be a video? What's irreducibly interactive?
- Scope surgery: what to cut, what to keep, what to double down on

**Activity (full session):**
- Each student demonstrates their working prototype
- The group EXPERIENCES each project (hands-on, not watching a demo)
- Structured feedback protocol:
  1. What did you DO? (describe actions, not visuals)
  2. What did that feel like? What quality of agency? (fluid? constrained? agonizing? liberating?)
  3. Could this be a video? What's irreducibly interactive?
  4. What spine level is this operating at? Could it go deeper?
  5. What one change would make the agency stronger?
- Instructor provides individual scope adjustments and technical direction

**Milestone:** Working prototype due. Not finished — playable. A person can walk up to it and interact.

**Student output:** Updated project plan: what to cut, what to refine, what spine level to target.

---

## PHASE 4: PRODUCTION

*Progressively relaxed. Less new content, more making time. Instructor shifts from lecturer to mentor.*

---

### Lecture 12 — Polish and Craft

**Brief (~30 min):**
- Juice: the small details that make interaction feel alive (easing curves, particle bursts, sound pitch variation, screen shake)
- The last 20% takes 80% — and it's the 20% the participant actually feels
- Audio craft: ambient loops, spatial placement, silence as design, Audio Mixer fine-tuning
- Animation curves: making transitions feel right (not linear, not instant)

**Unity tips:**
- Post-processing fine-tuning per zone
- Animation curves for smooth state transitions (Lerp with easing)
- Audio mixing: layers, ducking, spatial falloff
- Particle tuning: emission curves, color over lifetime, noise

**Remainder (~2 hours):** Project work. Individual mentorship focused on what to polish and what to leave alone.

---

### Lecture 13 — Testing and Iteration

**Brief (~20 min):**
- How to watch someone use your work: shut up and observe
- What to ask after: "What did you do?" not "Did you like it?"
- The one-change rule: change one thing, test again, repeat

**Activity (~60 min):**
- Structured playtest: students pair up, test each other's projects
- Observer records:
  - What did they do first?
  - What did they expect to happen?
  - What surprised them?
  - When were they most engaged? Most confused? Most lost?
- Debrief with partner

**Remainder (~50 min):** Project work incorporating playtest feedback.

---

### Lecture 14 — Open Studio

Full session: project work.

- Instructor available for troubleshooting and mentorship
- Students may collaborate, share techniques, help each other
- No new content
- Optional: lightning talks from students who solved interesting problems

---

### Lecture 15 — Pre-Final Critique

**Activity (~2 hours):**
- Each student presents their near-final project
- The group experiences each project directly (hands-on)
- Critique using the full course vocabulary:
  - What agency does the participant inhabit?
  - What spine level? (Reaction? State? Branching? Loop? Interconnection?)
  - Does it pass the Nouliness test?
  - What quality of agency? (Nguyen: fluid, constrained, agonizing, liberating)
  - Does meaning shine through the doing? (Campbell: radiance, epiphany through action)
- Each student receives: 1 thing that works, 1 thing to change

**Remainder (~30 min):** Final adjustment plan.

---

### Lecture 16 — Final Presentations

**Activity:**
- Each student presents and demonstrates their final project
- Brief artist statement: what agency did you design, and why?
- The group experiences each work directly
- Open discussion: what did you learn about designing interaction?

**Wrap-up:**
- The library of agencies: together, the class has built a collection of different modes of agency
- Course reflection: what surprised you about interaction as a medium?
- Where to go from here: festivals (Ars Electronica, A MAZE, IndieCade), communities, tools, further reading

---

## Summary Grid

| # | Title | Spine | Areas | Difficulty |
|---|-------|-------|-------|------------|
| 1 | Agency as Art + The Framework | L0 Reaction | Framework intro, object manip | * |
| 2 | Sequence: The Experience Goes Somewhere | L1 Sequence | Object manip + environment | * * |
| 3 | State: The World Remembers | L2 State | Object manip + feedback | * * |
| 4 | Movement as Expression | L2 State (applied) | Character control (adv.) | * * |
| 5 | Branching: Choices That Matter | L3 Branching | + UI interaction | * * * |
| 6 | Physics as Expression | L3 Branching | + Physics | * * * |
| 7 | Characters and Conversation | L3→L4 | + NPCs, narrative, dialogue | * * * * |
| 8 | Feedback Loops | L4 Feedback | All Tier 1 in loop config | * * * * |
| 9 | Interconnection | L5 Interconnection | All areas combined | * * * * * |
| 10 | Input Design + Installation | Transversal | Input, build, installation | * * * |
| 11 | Prototype Review | All (critique) | — | — |
| 12 | Polish and Craft | Production | Post-processing, audio, anim | * * * |
| 13 | Testing and Iteration | Production | Playtesting | — |
| 14 | Open Studio | Production | — | — |
| 15 | Pre-Final Critique | Critique | — | — |
| 16 | Final Presentations | Presentation | — | — |

---

## Reference Projects — Quick View

| Lec | Spine | Possible references (final choice TBD) |
|-----|-------|----------------------------------------|
| 1 | L0 Reaction | Passage (Rohrer), September 12th (Frasca), Boundary Functions (Snibbe) |
| 2 | L1 Sequence | The Unfinished Swan (Giant Sparrow), Gris (Nomada), Night Walk (Moment Factory) |
| 3 | L2 State | Wooden Mirror (Rozin), Reactive Table (teamLab), Walden (Fullerton) |
| 4 | L2 Movement | Dear Esther (Chinese Room), Journey (thatgamecompany), Flower (thatgamecompany) |
| 5 | L3 Branching | Papers Please (Pope), Kentucky Route Zero (Cardboard Computer), The Stanley Parable (Galactic Cafe) |
| 6 | L3 Physics | Tumble Room (Forsythe), Katamari Damacy (Takahashi), Getting Over It (Foddy) |
| 7 | L3→L4 NPCs | Florence (Mountains), The Stanley Parable (Galactic Cafe), Eliza (Zachtronics) |
| 8 | L4 Loops | September 12th (Frasca), Outer Wilds (Mobius Digital), Flower (thatgamecompany) |
| 9 | L5 Inter. | Journey (thatgamecompany), teamLab Borderless, Rain World (Videocult) |
| 10 | Transversal | Rain Room (Random International), Pulse Room (Lozano-Hemmer), Line Wobbler (Baumgarten) |
| 11 | Critique | *(student prototypes)* |
| 12–16 | Production | *(no new references)* |

---

## PRLW Mapping (Sellers) — Course Arc

```
Parts     →  L1  (elements exist and respond)
Rules     →  L2–L4  (elements follow ordering, conditional, and branching logic)
Loops     →  L5–L8  (logic creates divergent paths and circular feedback)
Wholes    →  L9  (everything talks to everything — designed emergence)
```

---

## Open Questions

- [ ] Which no-code framework components need to be ready by which session?
- [ ] AI policy: when can students use AI? (Proposal: AI-free for L1–L4 foundation; AI as production tool from L5+)
- [ ] Assessment criteria: weight of concept vs. execution vs. craft in final grade
- [ ] Intermediate graded checkpoints: L4? L9? L11?
- [ ] Exact readings to assign: which Nguyen chapters, which Campbell passages
- [ ] Should L10 (Installation) come earlier for students targeting physical installations?
- [ ] Fallback if L8–L9 are too complex: simplify Interconnection into a second Open Studio?
- [ ] How much time for personal project work vs. tutorial in Phase 2 sessions?
