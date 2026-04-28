# Curriculum — Areas to Cover

> This is a working document. Areas are listed by necessity, not by week order.
> The lecture-by-lecture plan will be built from this once areas are scoped and prioritized.

---

## What Changed from Previous Iterations

Previous versions of this course tried to cover Unity comprehensively — editor basics, C# fundamentals, 3D graphics, physics, shaders, VFX, animation, terrain, NPCs, dialogue, cameras, VR, optimization, publishing. It was too much. Students got lost in technical breadth and never arrived at meaningful authorship.

**This time**:
- The no-code interaction framework absorbs most of the technical complexity
- Techniques are taught *inside* example projects, not as standalone topics
- Every technical topic must justify itself by enabling a specific type of interactive expression
- If it doesn't serve agency, it doesn't make the cut

---

## Area 1: Foundations — Unity as a Creative Environment

What students need to simply *work* in Unity:
- Editor interface, scene view, hierarchy, inspector
- GameObjects, components, prefabs
- Importing and organizing assets
- Using the no-code interaction framework (triggers, actions, events)
- Building and testing a scene

**Not covered**: C# from scratch, project architecture, scripting patterns. The framework handles this.

---

## Area 2: Space and Environment

Designing the world the participant inhabits:
- Scene composition and spatial layout
- Terrain and ProBuilder for rapid environment building
- Lighting — real-time, baked, ambient, atmospheric
- Skyboxes, fog, post-processing (bloom, color grading, etc.)
- Environmental storytelling — how space communicates before any interaction happens

**Connection to philosophy**: The environment is not decoration — it's the first layer of agency. Where can I go? What draws me? What feels forbidden?

---

## Area 3: Movement and Perspective

How the participant exists in the space:
- First-person controller setup
- Camera as expressive tool — not just "the player's eyes"
- Cinemachine for cinematic moments and transitions
- Walkability — what's reachable, what's blocked, how movement itself carries meaning
- Hybrid input considerations (mouse/keyboard, controller, potentially VR)

**Connection to philosophy**: Movement is the most basic form of agency. Choosing where to go, what to look at — this is already interaction design.

---

## Area 4: Interaction Systems

The core of the course — how the participant acts on the world:
- The no-code framework: triggers → events → actions
- Proximity triggers, input triggers, gaze triggers, timed triggers, conditional triggers
- Actions: object manipulation, visual/audio feedback, environment changes, spawning, destroying
- Sequences of interaction — chained events, multi-step interactions
- World-space UI as interaction surface (not just menus — diegetic interfaces)

**Connection to philosophy**: This is where agency is designed. What can the participant do? What can't they? What does each action *feel like*?

---

## Area 5: Physics and Materiality

Giving the world physical presence:
- Rigidbodies, colliders, forces
- Physics materials (bounce, friction)
- Object weight, momentum, tactile quality
- Physics as interaction — pushing, throwing, stacking, breaking
- Physics as expression — gravity as metaphor, weightlessness, resistance

**Connection to philosophy**: Physicality is a layer of agency. A heavy object *feels* different to move. That feeling is designable.

---

## Area 6: Animation and Life

Making things move with intention:
- Unity Animator basics — states, transitions, blend trees
- Animation events tied to interaction
- Animated environments — doors, machines, natural elements
- Humanoid characters — importing, retargeting, basic movement
- Ragdoll physics as expressive tool

**Connection to philosophy**: Animation bridges the gap between static environment and living world. When things move in response to the participant, the world becomes an agent too.

---

## Area 7: NPCs and Behavioral Interaction

Other presences in the space:
- NavMesh for basic pathfinding
- Simple AI behaviors — approach, flee, wander, follow
- NPC responses to player proximity and actions
- Group behaviors
- NPCs as emotional/narrative instruments (the "Nouliness" model)

**Connection to philosophy**: NPCs are the most direct way to design *social* agency. The participant's relationship to other beings is a rich expressive space.

---

## Area 8: Feedback and Sensory Design

How the world responds to the participant:
- Sound — spatial audio, ambient layers, reactive sound
- Visual feedback — material changes, particle effects, screen effects
- Timing and rhythm of feedback — immediate vs. delayed, subtle vs. dramatic
- The difference between *feedback* (response to action) and *ambiance* (persistent atmosphere)

**Connection to philosophy**: Feedback closes the agency loop. Without it, actions feel meaningless. The *quality* of feedback shapes the *quality* of the experience.

---

## Area 9: Narrative and Progression

Structuring the experience over time:
- State machines for managing phases/progression
- Simple conditionals and objectives
- Dialogue systems (lightweight — Yarn Spinner or custom)
- Branching and consequences
- Pacing — when to act, when to wait, when to withhold

**Connection to philosophy**: Narrative in interactive art isn't story — it's the *arc of agency*. How does the participant's relationship to the world change over time?

---

## Area 10: Design Theory and Critical Framework

The thinking behind the making:
- What is interaction design? What are constraints? How do you navigate a design space?
- Agency as art (Nguyen) — goals, abilities, constraints as designable elements
- Epiphany through action (Campbell/Joyce) — the aesthetic endgame
- Reference analysis — breaking down real interactive artworks
- Critique method: "What did you *do*? What did that *feel like*? Could this be a video?"

**Not a separate lecture block** — woven into every session. But may need 1-2 dedicated sessions early on.

---

## Areas Explicitly Deferred or Cut

These appeared in previous iterations but don't serve the new course:
- ~~C# programming fundamentals~~ → framework handles it
- ~~Shader Graph / custom shaders~~ → too technical for 40hrs; use pre-made shaders in asset package
- ~~VFX Graph~~ → same; pre-made effects in asset package
- ~~VR-specific setup and XR toolkit~~ → out of scope unless reintroduced later
- ~~Build/publish pipeline~~ → final session only if needed
- ~~Performance optimization~~ → not a priority for 40hrs

---

## Open Questions

- [ ] How many of these 10 areas get dedicated sessions vs. being embedded in project tutorials?
- [ ] What's the right order? (Likely: Foundations → Space → Movement → Interaction → then branches)
- [ ] Which areas can be merged? (e.g., Physics + Interaction, Animation + NPCs)
- [ ] How much design theory per session? (5 min? 15 min? A full first session?)
- [ ] Where do real-world reference analyses land in the schedule?
- [ ] Which areas does the no-code framework need to cover before students can use it?
