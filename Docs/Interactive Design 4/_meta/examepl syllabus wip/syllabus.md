# Multimedia Design 4 — Interaction Design for Artists

## Syllabus

---

### What this course is about

You already know how to build environments in Unity. You can light a scene, place objects, set up a first-person controller. This course asks a different question: **what does the person experiencing your work actually *do*, and what does that doing *mean*?**

Most art — painting, sculpture, film, installation — asks the audience to look. This course is about designing what happens when the audience *acts*. We treat interaction itself as the creative material: not a technical layer on top of visuals, but the primary medium of expression.

By the end of the course, you will have designed and built a personal interactive work where the participant's actions produce meaning that could not exist without those actions.

---

### How the course works

**16 sessions, 2.5 hours each.**

Each session follows the same rhythm:

- We look at real interactive artworks and installations, and break down how they work — not technically, but as designed experiences of agency.
- We learn a new interaction technique through a guided example project in Unity, building on the interaction framework.
- You apply what you've learned to your own personal project, with individual mentorship.
- We share and discuss: *what did you do? What did that feel like?*

**Your personal project starts from session 1** — not after "learning the tools." The project will change shape many times. That's the process.

---

### The progression

The course moves through increasing levels of interaction complexity:

**Sessions 1–4** build the foundation. We review the trigger-action pattern, then move into interactions that have *phases*, that *remember* what you've done, and that make *movement itself* meaningful.

**Sessions 5–8** go deeper. Interactions that branch based on your choices. Physics that feels intentional, not default. Characters and entities that respond with memory. Feedback loops where your actions change the world and the changed world changes what you do next.

**Sessions 9–11** bring everything together. Multiple systems talking to each other. Installation practice. And a group critique of your working prototype.

**Sessions 12–16** are production. Polishing, testing, iterating, and presenting your final work.

---

### Session by session

---

**Session 1 — What Is Interactive Art?**

The course thesis: agency as art. What makes an interactive work different from a film, a painting, or a static installation? We introduce the key question you'll return to all semester: *"Could this be a video? If yes, it's not yet interaction design."*

We review the interaction framework — triggers, actions, events — and build a simple responsive scene as a refresher. The focus isn't the tool; it's the lens.

*Reference artworks:*
- *Passage* (Jason Rohrer) — a 5-minute game about an entire life
- *September 12th* (Gonzalo Frasca) — a political argument made entirely through interaction
- *Boundary Functions* (Scott Snibbe) — a work that only exists when people are in the room

> *The in-class example project for each session will be chosen and designed separately. The references listed here are candidates for analysis and inspiration.*

---

**Session 2 — The Experience Goes Somewhere**

A single reaction is a toy. A *sequence* of reactions is an experience. This session is about interactions that unfold over time — things that unlock, stages that progress, a world that transforms step by step. We work with object manipulation (spawning, transforming, destroying) and environment shifts (light, fog, atmosphere changing in phases).

*Reference artworks:*
- *The Unfinished Swan* (Giant Sparrow) — each chapter reveals the world in a new way through a single verb
- *Gris* (Nomada Studio) — colors return one by one, transforming the landscape as emotional recovery
- *Night Walk* (Moment Factory) — a forest path that lights up zone by zone as you walk

---

**Session 3 — The World Remembers**

The most powerful moment in interaction: doing the same thing twice and getting a different result. The world now has memory. It knows what you've done, how many times you've done it, and it responds accordingly. We introduce state — variables, conditions, accumulation — and sensory feedback that changes with the world's memory.

*Reference artworks:*
- *Wooden Mirror* (Daniel Rozin) — 830 tiles whose state is driven by camera input, updating in real time
- *Reactive Table* (teamLab) — flowers grow where you've touched, accumulate, and decay. The surface remembers.
- *Walden, a game* (Tracy Fullerton) — the world's beauty tracks your attention. Rush and it fades. Slow down and it blooms.

---

**Session 4 — Movement as Expression**

You already have a first-person controller. This session asks: what does the movement *mean*? Walking speed, camera behavior, spatial constraints, and where you can or can't go are design decisions, not defaults. We tune movement for expression and connect it to world-state — a character that slows as the world decays, a camera that tightens in confined spaces, areas that open only when conditions are met.

*Reference artworks:*
- *Dear Esther* (The Chinese Room) — the decision to remove every verb except "walk" IS the artistic statement
- *Journey* (thatgamecompany) — movement constraints create emotional arcs. An anonymous stranger joins, but you can only chirp.
- *Flower* (thatgamecompany) — the character is wind. Movement and environmental transformation are the same action.

---

**Session 5 — Choices That Matter**

The participant makes a choice. The world forks. Some things can't be undone. Two people experiencing the same work have different experiences. We introduce branching — divergent paths created by accumulated state — and world-space UI: interfaces that exist inside the 3D world and carry meaning through their form, not just their function.

*Reference artworks:*
- *Papers, Please* (Lucas Pope) — stamp APPROVED or DENIED. Each stamp is irreversible. The desk interface is the moral engine.
- *Kentucky Route Zero* (Cardboard Computer) — dialogue choices define who the characters are, not where the plot goes
- *The Stanley Parable* (Galactic Cafe) — obey or disobey a narrator. The game forks on compliance vs. defiance.

---

**Session 6 — Physics as Expression**

Physics isn't about realism — it's about feel. Weight, bounciness, friction, and force are expressive parameters. A heavy world feels different from a floaty one. The gap between what you intend and what happens — that's where comedy, frustration, and meaning live. We tune physics for expression, not simulation.

*Reference artworks:*
- *Tumble Room* (William Forsythe) — walk through hundreds of suspended balloons. Your body is a force in a physics field.
- *Katamari Damacy* (Keita Takahashi) — deliberately clumsy rolling, accumulation from paperclips to planets
- *Getting Over It* (Bennett Foddy) — one tool, one physics system. The frustration IS the design.

---

**Session 7 — Characters and Conversation**

An NPC is any entity that responds to you with apparent intention. It doesn't have to be human — a forest can be an NPC, a narrator can be an NPC, the room itself can behave like a character. We build entities with state and memory: characters that remember what you've done and treat you differently because of it. We introduce dialogue systems and simple behavioral AI.

*Reference artworks:*
- *Florence* (Mountains) — relationship moments expressed as micro-interactions. Speech bubbles as puzzles that get easier with comfort.
- *The Stanley Parable* (Galactic Cafe) — the narrator reacts to your compliance or rebellion. Agency as negotiation.
- *Eliza* (Zachtronics) — read the AI's script to patients, or go off-script. The gap between machine words and human judgment.

---

**Session 8 — Feedback Loops**

The most powerful interactions are circular, not linear. You act, the world changes, the changed world alters what you can or want to do, and the cycle continues. Positive loops escalate. Negative loops resist. A loop can be a metaphor: "the more you take, the less there is" IS a statement about extraction. We build interactions that sustain themselves — that breathe.

*Reference artworks:*
- *September 12th* (Frasca) — fire missiles, create mourners, mourners become terrorists, more targets appear. The loop IS the political argument.
- *Outer Wilds* (Mobius Digital) — a solar system on a 22-minute timer. You die, restart, but the only thing that persists is what you know.
- *Flower* (thatgamecompany) — bloom flowers, the world turns green, more flowers appear, more to bloom. A restoration loop.

---

**Session 9 — Everything Talks to Everything**

Real interactive works are ecosystems. Physics affects NPCs. NPCs affect the environment. The environment affects feedback. Feedback affects how you move. When multiple systems are connected, moments emerge that the designer didn't script — and those moments are often the most powerful. We integrate, connect, and design for emergence.

This session also includes your **project concept lock-in**: you present your direction, get group feedback, and commit to a scope.

*Reference artworks:*
- *Journey* (thatgamecompany) — movement, environment, music, and social interaction, all interconnected
- *teamLab Borderless* — works flow between rooms. Touch affects flowers, flowers affect water, water affects creatures.
- *Rain World* (Videocult) — a full ecosystem that runs whether you're watching or not

---

**Session 10 — From Screen to Space**

Your work will exist in a physical context — a gallery, an installation, a room with a screen. The input device, the display setup, and the physical arrangement are all design decisions. We cover input abstraction (so your interaction isn't locked to a keyboard), standalone builds, and installation robustness: what happens when your piece needs to run unattended for days.

*Reference artworks:*
- *Rain Room* (Random International) — the input is your body. It must run 12 hours a day without failing.
- *Pulse Room* (Rafael Lozano-Hemmer) — the input is a heart-rate sensor. 300 lightbulbs must respond reliably.
- *Line Wobbler* (Robin Baumgarten) — the input is a door-stopper spring. The device and the work are inseparable.

---

**Session 11 — Prototype Review**

Everyone presents their working prototype. Not finished — playable. The group experiences each project hands-on and gives structured feedback:

- *What did you do?* (Describe actions, not visuals.)
- *What did that feel like?*
- *Could this be a video? What's irreducibly interactive?*
- *What one change would make the agency stronger?*

You leave with a clear plan: what to cut, what to keep, what to refine.

**Working prototype due.**

---

**Session 12 — Polish and Craft**

A short session on the details that make interaction feel alive — easing curves, sound design, particle tuning, the small things the participant feels even if they can't name them. Then: project work with individual mentorship.

---

**Session 13 — Testing and Iteration**

How to watch someone experience your work (silently), what to ask them afterward ("What did you do?" not "Did you like it?"), and how to change one thing at a time. Structured playtesting in pairs, then project work incorporating feedback.

---

**Session 14 — Open Studio**

Full session for project work. No new content. Instructor available for troubleshooting and mentorship. Collaboration encouraged.

---

**Session 15 — Pre-Final Critique**

Each student presents their near-final work. The group experiences it directly and gives feedback using everything we've learned:

- What agency does the participant inhabit?
- Does meaning come through the doing, or is it layered on top?
- What quality does the agency have — fluid, constrained, contemplative, agonizing, liberating?

Each student receives: one thing that works, one thing to change before next week.

---

**Session 16 — Final Presentations**

Present your finished work. Brief artist statement: what interaction did you design, and why? The group experiences each project. We close with a reflection on what we've collectively built — a small library of different modes of agency — and where to go from here.

**Final project due.**

---

### What you'll make

A personal interactive work built in Unity. It can be an installation, an experience, a game, a space — the form is open. What matters is:

- The participant's actions produce meaning that could not exist without those actions
- The interaction has depth — it's not a single reaction, but a designed experience that unfolds, remembers, responds, and evolves
- The technical execution supports the concept — polished enough that the technology disappears and the experience is what remains

---

### How each session is structured

| | Duration | |
|---|---|---|
| **Reference + discussion** | ~20 min | We analyze real interactive artworks: what does the participant do? What does that feel like? |
| **Technique + guided project** | ~40 min | We build together, learning a new interaction technique through the session's example project |
| **Personal project work** | ~50 min | You apply the technique to your own project, with individual mentorship |
| **Share + critique** | ~15 min | Quick round: what did you make? What did it feel like? |

---

### Key dates

| Session | Milestone |
|---------|-----------|
| 9 | Project concept locked in |
| 11 | Working prototype due |
| 16 | Final project due |

---

### Production values

These aren't grading criteria — they're working principles:

- **Don't be precious** — don't cling to the first idea
- **Experiment broadly** — make 10 things to find the 1 that works
- **Test relentlessly** — if no one has experienced your work besides you, it doesn't exist yet
- **Navigate constraints** — scope is a creative decision, not a limitation
- **Explore before committing** — your project will change shape. That's the process.
