# Game Dev 2 — Philosophy & Design Principles

## Working Document — March 2026

---

## Why This Course Exists

Architecture is the durable skill. Code generation is becoming cheap and fast — AI writes functional scripts on demand. But *organizing* a project so that systems are modular, data is separated from logic, and everything can be changed without breaking everything else — that remains expensive, human, and essential. This course teaches students to think architecturally: to design the structure before (and while) they build the thing.

The vehicle for learning architecture is building a game where architecture actually matters — one where independent systems interact, where the world is alive and reactive, where you can't get away with spaghetti because the systems need to talk to each other cleanly.

---

## Core Philosophy

### Code as Design Medium

Code is not just implementation. The way you structure a project — what you separate, what you connect, how data flows — is a design act. Access modifiers are design decisions. A ScriptableObject is a design choice about where truth lives. An event channel is a design choice about how systems communicate. Students should leave this course understanding that architecture *is* design, expressed in structure rather than pixels.

### Living Systems Over Static Worlds

The default indie game is a static environment the player walks through and discovers. This course pushes toward the opposite: **environments that are alive**, that change, that respond. Cycles run whether the player watches or not. NPCs have behaviors. Systems produce emergent interactions. The player doesn't just explore a world — they interact with and shape a living system.

This is the immersive sim sensibility, scaled to student scope: not Deus Ex, but a small world where things happen, react, and interconnect.

### Architecture Enables Emergence

These two ideas reinforce each other. You cannot build a living, reactive world with tightly coupled code. If the day-night cycle is hardwired to the NPC behavior which is hardwired to the environment state, changing any one thing breaks everything. Modular architecture — separated data, independent systems, event-driven communication — is what *allows* systems to interact without becoming spaghetti. The design ambition justifies the technical discipline.

### Speculative Development

AI is a design amplifier, not a replacement for understanding. The workflow is: understand the architecture → write a specification → generate code → evaluate and integrate critically. You need to know what you're asking for and whether what you got back is correct. This requires *more* architectural literacy, not less.

---

## Design Principles

These principles govern both the example project and student projects. They are not rigid rules but a shared direction.

### First-Person Perspective

The course works in first person. This is both an aesthetic choice (immersion, presence, direct interaction with the world) and a pragmatic one: first-person translates across PC, WebGL, Mobile, and VR with manageable adaptation. It's the perspective that makes cross-platform viable without rebuilding the entire interaction layer.

### Cross-Platform Awareness

Design with portability in mind. The same experience should be adaptable to PC, WebGL, and potentially VR or mobile. This isn't about shipping to four platforms — it's about making architectural choices (input abstraction, interaction patterns, UI approach) that don't lock you into one.

### World-Space and Diegetic UI

Minimize HUD. Prefer world-space UI, diegetic interfaces, and environmental communication over screen-space overlays. Information lives *in* the world: a health indicator is a visual change on the character or environment, not a floating bar. A dialogue happens in space, not in a text box bolted onto the screen. This reinforces immersion and demands cleaner architectural separation between game state and its presentation.

### Physics-Based and Spatial Interaction

Interactions should feel grounded: grabbing, pushing, placing, activating through proximity or physics. These patterns are inherently VR-compatible and produce more satisfying feedback than abstract button presses. Even on PC with mouse and keyboard, the *design* of interactions should be spatial and physical rather than menu-driven.

### Living Environments

The world has its own rhythms. Day-night cycles, weather, ecosystem behaviors, NPC routines — things happen whether the player is watching or not. The player enters a system already in motion and intervenes in it, rather than being the sole cause of all events. This is the key design distinction from the first course's more linear, player-triggered approach.

### Systemic Interaction and Emergence

Systems should be able to talk to each other and produce unplanned outcomes. Fire spreads. Sound attracts attention. Environmental changes affect NPC behavior. The goal is not to script every possible interaction but to build systems whose rules, when combined, produce emergent situations. This is where architecture pays off — decoupled systems connected through events and shared data *can* interact; tightly coupled systems *cannot*.

### Shaping the World

The player doesn't just observe — they change the environment. Upgrading structures, influencing cycles, redirecting flows. The world should be malleable in ways that persist and compound. This creates a feedback loop: player action → world change → new systemic behavior → new player decisions.

---

## Aesthetic Direction

Not prescriptive — students choose their own visual direction — but the course leans toward:

- Atmospheric, mood-driven environments over photorealism
- Environmental storytelling (the world communicates through space, objects, light)
- Feedback as design: every player action produces visible, audible, or systemic response
- Coherence between visual tone and mechanical behavior (a tense world *feels* tense in its systems, not just its lighting)

---

## What This Is Not

- Not a graphics course (though aesthetics matter and are discussed)
- Not a pure programming course (though C# competence is built)
- Not a game design theory course (though design principles are embedded)
- Not a linear adventure or walking simulator

It is a **systems design and architecture course** that uses game development as its medium, immersive sim thinking as its design frame, and a living, reactive world as the proving ground for whether the architecture actually works.

---

*This document defines the philosophical direction. See `project_design.md` for the specific example project concept and system breakdown. See `notes.md` for course structure, session anatomy, and topic sequencing.*
