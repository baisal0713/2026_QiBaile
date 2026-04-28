# Multimedia Design 4 — Interaction Design for Artists

## Course Plan

---

### Course Overview

This course repositions interaction design as an expressive medium for artists and designers. Where most art and installation practice treats the audience as a viewer, this course treats the audience as a participant whose actions are the primary material of the work.

Students entering this module have completed two prior Unity courses covering editor fundamentals, 3D environment design, lighting, materials, animation, and basic first-person controllers. This course builds on that technical foundation by shifting the focus from *how to build* to *what the participant does and what that doing means*.

The central thesis draws on C. Thi Nguyen's concept of "agency as art" — the idea that interactive works sculpt the experience of acting, choosing, and deciding, much as painting sculpts the experience of seeing. The course applies this lens across a progression of increasing interaction complexity, from simple trigger-response patterns through stateful systems, branching logic, feedback loops, and multi-system interconnection.

Each session is anchored in the analysis of real interactive artworks and installations, ensuring that technical skills are always in service of expressive intent.

The final output is a personal interactive work — an installation, experience, or interactive environment — in which the participant's actions produce meaning that could not exist without those actions.

---

### Course Structure

- **Total contact hours:** 40
- **Number of sessions:** 16
- **Session duration:** 2.5 hours
- **Primary tool:** Unity (with a custom no-code interaction framework)
- **Prerequisites:** Multimedia Design 2 and 3 (Unity fundamentals, 3D environment design, basic interaction)

---

### Session Format

Each session follows a consistent structure:

| Block | Duration | Description |
|-------|----------|-------------|
| Reference analysis | ~20 min | One or two real interactive artworks are examined: what does the participant do, what interaction logic is at work, and what quality of agency does the work produce? |
| Technique introduction | ~40 min | A new interaction technique is introduced through a guided example project. Students build alongside the instructor using the interaction framework. |
| Personal project work | ~50 min | Students apply the session's technique to their personal project, with individual mentorship. |
| Share and critique | ~15 min | Brief group sharing using a consistent critical vocabulary: *What did the participant do? What did that feel like? Could this be a video?* |

Personal project work begins in session 1 and continues through every session. Project direction is formalized in session 9, a working prototype is due in session 11, and the final project is presented in session 16.

---

### Progression

The course advances through four phases of increasing complexity:

**Phase 1 — Foundations (Sessions 1–4):** The course philosophy is introduced alongside a review of the interaction framework. Sessions progress from single trigger-response interactions through sequenced multi-phase experiences, stateful systems with memory and accumulation, and expressive movement design.

**Phase 2 — Depth (Sessions 5–8):** More complex interaction logic is introduced: branching paths with irreversible consequences, physics tuned for expression rather than simulation, stateful NPCs and dialogue systems, and self-sustaining feedback loops.

**Phase 3 — Integration (Sessions 9–11):** Multiple interaction systems are connected into unified works. Installation and input design are addressed. A formal prototype review provides structured group critique.

**Phase 4 — Production (Sessions 12–16):** Dedicated to project refinement, playtesting, iteration, and final presentation. Sessions become progressively less structured, shifting from guided instruction to mentorship and studio time.

---

### Session Descriptions

---

**Session 1 — What Is Interactive Art?**

Introduction of the course thesis: interaction as expressive medium. The key critical question — *"Could this experience be replaced by a video? If so, the interaction is not yet doing its work"* — is established as a recurring evaluation tool. The session includes a review of the trigger-action interaction pattern (familiar from prior courses) reframed through the lens of designed agency.

*Reference artworks (candidates):*
- *Passage* (Jason Rohrer) — studied for how a single linear traversal (walking right) encodes an entire emotional arc through minimal interaction and irreversible time progression
- *September 12th* (Gonzalo Frasca) — studied for how a surface-level simple interaction (click to fire) produces a systemic argument that can only be understood through participation
- *Boundary Functions* (Scott Snibbe) — studied for how the simplest possible trigger (bodily presence in a room) produces social meaning that is literally impossible without multiple participants

---

**Session 2 — The Experience Goes Somewhere**

Interactions that unfold over time: sequenced phases, staged progression, and environments that transform step by step. Object manipulation (spawning, transforming, enabling/disabling) and environment shifts (lighting transitions, fog, atmosphere) are introduced as the building blocks of phased experiences.

*Reference artworks (candidates):*
- *The Unfinished Swan* (Giant Sparrow) — studied for its chapter structure, where a single verb (throwing) produces radically different spatial revelations in each phase (paint in white void, water on dry ground, light in darkness)
- *Gris* (Nomada Studio) — studied for its use of sequential color restoration as both game mechanic and emotional narrative, where each new color transforms the entire landscape and unlocks new abilities
- *Night Walk* (Moment Factory) — studied for its zone-based environmental sequencing: a linear path through a forest where each section triggers distinct light, fog, and audio transformations, producing narrative without text

---

**Session 3 — The World Remembers**

Introduction of state: variables, conditions, and accumulated change. The same action now produces different results depending on what has happened before. Sensory feedback is deepened to reflect state — sounds that evolve with repetition, visual density that tracks accumulation, environments that darken or brighten based on participant history.

*Reference artworks (candidates):*
- *Wooden Mirror* (Daniel Rozin) — studied for its pure state-driven output: 830 individually addressable elements whose rotation state maps directly to real-time input data, producing a portrait that exists only as continuously updated state
- *Reactive Table* (teamLab) — studied for its accumulation logic: flowers spawn at touch points, grow over time, attract insects, and eventually decay — creating a visible history of contact that transforms the surface
- *Walden, a game* (Tracy Fullerton) — studied for its state-feedback coupling: the world's color saturation is a continuous variable driven by the player's movement speed and attentiveness, making the aesthetic environment a direct readout of behavioral state

---

**Session 4 — Movement as Expression**

Students have built first-person controllers in prior courses. This session reframes movement parameters — speed, acceleration, camera field of view, spatial access — as expressive design decisions. Movement is connected to world-state: parameters that shift in response to accumulated conditions, spatial gating based on participant history, and camera behaviors that respond to context.

*Reference artworks (candidates):*
- *Dear Esther* (The Chinese Room) — studied for the design decision to remove every interaction verb except walking and looking, and how that constraint concentrates all meaning into spatial traversal and ambient narration
- *Journey* (thatgamecompany) — studied for its movement constraint design: limited flight tied to a consumable scarf resource, momentum-based sand surfing, and the deliberate absence of verbal communication as a social constraint that forces meaning into spatial behavior
- *Flower* (thatgamecompany) — studied for its non-anthropomorphic character control: the player embodies wind through tilt input, and the act of moving through space is simultaneously the act of transforming the environment (touching flowers blooms them)

---

**Session 5 — Choices That Matter**

Introduction of branching: divergent paths, irreversible consequences, and accumulated state producing different experiences for different participants. World-space UI (diegetic interfaces embedded in the 3D environment) is introduced as both a technical tool and an expressive surface — the form of the interface itself communicates meaning.

*Reference artworks (candidates):*
- *Papers, Please* (Lucas Pope) — studied for its diegetic desk interface as moral architecture: the physical act of stamping documents, cross-referencing details, and managing time pressure produces ethical weight through bureaucratic interaction, not narrative exposition
- *Kentucky Route Zero* (Cardboard Computer) — studied for its non-consequential branching: dialogue choices do not alter the plot but define the characters' identities and emotional histories, making selection an act of authorship rather than strategy
- *The Stanley Parable* (Galactic Cafe) — studied for its compliance/defiance fork structure: a narrator describes what the player "will" do, and every moment of obedience or rebellion produces meta-commentary on the nature of agency within designed systems

---

**Session 6 — Physics as Expression**

Physics systems are reframed from simulation tools to expressive parameters. Mass, drag, bounciness, and force application are treated as design decisions that encode emotional register — weight, fragility, resistance, elasticity. The inherent unpredictability of physics systems is positioned as a form of branching: the same action produces different physical outcomes each time.

*Reference artworks (candidates):*
- *Tumble Room* (William Forsythe) — studied for its treatment of the participant's body as a force vector in a field of lightweight physics objects (suspended balloons), where every movement displaces, collides, and settles the surrounding elements
- *Katamari Damacy* (Keita Takahashi) — studied for its deliberately clumsy twin-stick control scheme as a source of physical comedy, and its single mechanic (rolling adhesion) producing a scale progression from tabletop objects to continental landmasses
- *Getting Over It* (Bennett Foddy) — studied for its use of a single physics tool (a hammer) in a punishing environment where setback is total, making the physics feel itself — frustration, persistence, loss of progress — the explicit subject of the work

---

**Session 7 — Characters and Conversation**

Introduction of NPCs and dialogue systems. The definition of "NPC" is broadened beyond humanoid characters to include any entity that responds to the participant with stateful, apparently intentional behavior — including narrators, environmental agents, and abstract systems. Dialogue integration (Ink or Yarn Spinner), simple behavioral state machines, and NPC memory are introduced.

*Reference artworks (candidates):*
- *Florence* (Mountains) — studied for its wordless NPC design: relationship dynamics expressed through changing micro-mechanics (speech-bubble puzzles that simplify as comfort grows, shared domestic actions, the physical act of tearing a photo)
- *The Stanley Parable* (Galactic Cafe) — studied for the narrator as NPC: a disembodied voice that tracks the player's actions, adapts its script in response to compliance or defiance, and serves as both guide and antagonist
- *Eliza* (Zachtronics) — studied for its script-adherence mechanic: the player reads AI-generated therapy dialogue to patients and must choose whether to follow the script or deviate, making the tension between system output and human judgment the core interaction

---

**Session 8 — Feedback Loops**

Introduction of circular interaction logic: action changes the world, the changed world alters the conditions for further action, and the cycle sustains itself. Positive loops (escalation), negative loops (resistance), and mixed loops are examined as expressive structures. A single state variable is used to drive multiple systems simultaneously — light, audio, physics, and NPC behavior all responding to the same accumulating condition.

*Reference artworks (candidates):*
- *September 12th* (Frasca) — studied for its self-reinforcing loop: missile strikes produce civilian casualties, mourning civilians become new combatants, more combatants invite more strikes. The systemic argument emerges exclusively from the loop structure.
- *Outer Wilds* (Mobius Digital) — studied for its resetting loop with persistent knowledge: a 22-minute solar system cycle resets all physical state on death, but the player's understanding persists, making knowledge itself the only form of progress
- *Flower* (thatgamecompany) — studied for its positive restoration loop: blooming flowers transforms the landscape, which reveals more flowers, which invites more blooming — a self-reinforcing cycle of agency and environmental recovery

---

**Session 9 — Everything Talks to Everything**

Multi-system integration: connecting physics, environment, NPCs, feedback, and movement into a unified interactive ecosystem. The concept of designed emergence is introduced — setting up interconnections between systems such that unscripted moments arise from the interactions between them.

This session includes a formal **project concept review**: each student presents their project direction, identifies which interaction systems are at work, and receives group and instructor feedback. Project scope is finalized.

*Reference artworks (candidates):*
- *Journey* (thatgamecompany) — studied for its integration of movement physics (sand surfing, flight), environmental responsiveness (wind, light), audio feedback (dynamic score), and anonymous social interaction into a seamless, wordless whole
- *teamLab Borderless* — studied for its architectural approach to system interconnection: individual works are not contained to rooms but flow between spaces, with participant touch affecting flowers, flowers affecting water, water affecting creatures across boundaries
- *Rain World* (Videocult) — studied for its autonomous ecosystem simulation: predator-prey dynamics, weather cycles, and migration patterns operate independently of the player, who is simply another creature navigating a system that does not revolve around them

---

**Session 10 — From Screen to Space**

Practical considerations for interactive work in physical exhibition contexts. Input abstraction (designing for keyboard during development while targeting alternative devices for exhibition), standalone build configuration, and installation robustness (auto-launch, crash recovery, unattended operation) are covered.

*Reference artworks (candidates):*
- *Rain Room* (Random International) — studied for its input design (full-body position tracking via ceiling-mounted sensors) and its operational requirement to run reliably for 12+ hours per day across multi-month exhibition periods
- *Pulse Room* (Rafael Lozano-Hemmer) — studied for its sensor-to-output pipeline: a single biometric input (heart rate) drives 300 individually addressable light outputs, requiring robust real-time data handling and graceful degradation
- *Line Wobbler* (Robin Baumgarten) — studied for its inseparability of input device and experience: the door-stopper spring controller IS the interaction, demonstrating that input hardware is a design decision, not a technical afterthought

---

**Session 11 — Prototype Review**

Structured group critique of working prototypes. Each student demonstrates their project; the group experiences it hands-on (not as a passive demonstration). Feedback follows a consistent protocol focused on the quality of agency, irreducibility of interaction, and the relationship between the participant's actions and the work's meaning.

**Milestone: working prototype due.** The prototype need not be complete, but it must be interactive — a participant can engage with it and produce a meaningful experience.

---

**Session 12 — Polish and Craft**

Brief instruction (~30 minutes) on interaction refinement: easing curves, audio design, particle tuning, post-processing, and the micro-details of responsive feel. The remainder of the session is dedicated to project work with individual mentorship.

---

**Session 13 — Testing and Iteration**

Brief instruction (~20 minutes) on observational playtesting methodology and iterative refinement. Structured playtesting session in pairs: students observe someone else experiencing their work, record behavioral data, and debrief. Remaining time is dedicated to incorporating feedback.

---

**Session 14 — Open Studio**

Full session dedicated to project production. No new instruction. Individual mentorship and peer collaboration available throughout.

---

**Session 15 — Pre-Final Critique**

Formal group critique of near-final projects. Each project is experienced directly by the group. Critique addresses the quality and nature of the designed agency, the irreducibility of the interactive experience, and the degree to which meaning is produced through action rather than applied through other media (text, image, narrative exposition).

---

**Session 16 — Final Presentations**

Presentation and demonstration of completed projects. Each student delivers a brief artist statement articulating the interaction they designed and why. The group experiences each work directly. The session closes with a collective reflection on the range of agencies the class has produced — a shared library of different modes of interactive expression.

**Final project due.**

---

### Learning Outcomes

By the end of the course, students will be able to:

1. **Analyze interactive works as designed experiences of agency** — identifying how goals, constraints, and participant abilities produce specific qualities of experience
2. **Design interactions with increasing logical complexity** — from single trigger-response patterns through sequenced, stateful, branching, looping, and interconnected systems
3. **Implement interactive experiences in Unity** using a component-based interaction framework, covering object manipulation, environment control, physics, UI, character behavior, dialogue, and sensory feedback
4. **Evaluate interactive work using a critical vocabulary** centered on the irreducibility of interaction: whether meaning is produced through the participant's action or merely delivered alongside it
5. **Produce a personal interactive work** that demonstrates both conceptual understanding and technical implementation, suitable for exhibition in an installation or gallery context

---

### Key Milestones

| Session | Milestone |
|---------|-----------|
| 9 | Project concept finalized (direction, scope, system diagram) |
| 11 | Working prototype due (interactive, not necessarily complete) |
| 16 | Final project due (complete, exhibition-ready) |

---

### Theoretical References

- C. Thi Nguyen, *Games: Agency As Art* (Oxford University Press, 2020) — agency as designable medium; goals, abilities, and constraints as the materials of interactive art; value clarity and value capture
- Joseph Campbell, *The Power of Myth* (Anchor, 1988) — epiphany through experience; radiance and transparency as the aesthetic goal of art, applied here to interaction ("meaning shining through doing")
- Mihaly Csikszentmihalyi, *Flow* (Harper Perennial, 1990) — optimal experience as the collapse of distance between person and activity, reframed as a designable quality of interactive systems

---

### Production Principles

These principles are communicated to students as working values throughout the course:

- **Don't be precious** — willingness to abandon early ideas in favor of stronger ones
- **Experiment broadly** — produce many variations to discover what works
- **Test relentlessly** — an untested interaction does not yet exist as a work
- **Navigate constraints** — scope is a creative decision, not a limitation
- **Explore before committing** — the project will change shape through the process; that is expected and productive
