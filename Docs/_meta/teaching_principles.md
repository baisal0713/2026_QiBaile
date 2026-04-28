#Teaching Principles & Pedagogical Design

## Working Document — March 2026

*Extracted from course design notes. These principles govern how the course is conducted, how students are supported, and how the learning experience is structured — distinct from what is taught (see `philosophy_and_principles.md`) and how sessions are organized (see `notes.md`).*

---

## 1. Instruction as a Design Problem

Teaching craft deserves the same rigor as the architecture being taught. Enunciation, pacing, repetition, and physical presence in the room are not incidental — they are design variables that determine whether information lands.

**Conduct principles:**
- Enunciate. Talk slowly. Take your time.
- Repeat key ideas — redundancy is a feature, not a flaw.
- Visit students personally during workshop time. Circulate. Don't anchor to the podium.
- Use countdown timers with visible topic labels — students should always know what phase they're in and how long it lasts.
- Record lessons (OBS, mixed between new recordings and pause-and-review segments). Create separate videos for separate topics — never a single monolithic recording.

**Tooling:**
- Notion for titles, tracking, and page structure.
- OBS for lesson recordings.
- A visible timer tool (OnTime or equivalent) to block out lectures and signal transitions.

The principle: *if you wouldn't ship spaghetti code, don't ship spaghetti instruction.*

---

## 2. Observation Before Intervention — Student Tracking as Research

You cannot improve what you don't observe systematically. Track every student's engagement and performance across the semester. Assign internal scores. Factor your own performance — if you had an off day and engagement dropped, that's data about you, not just about them.

This is not surveillance. It is the same empirical sensibility you'd apply to playtesting a game: observe behavior, identify patterns, adjust the design.

**What to track:**
- Weekly engagement and output quality
- Participation patterns (active, passive, declining, surging)
- Self-assessment accuracy (do they know what they're good at?)
- Project trajectory (early ambition vs. mid-course reality vs. final delivery)

**Research layer:**
- Study learning styles — not as a taxonomy to sort students into, but as a lens for understanding why certain students stall at certain points.
- Correlate your teaching quality with student outcomes honestly. Some dips are theirs; some are yours.

---

## 3. Student Archetypes and the Pain Points

Students fail in predictable patterns. Naming those patterns — making them visible from the start — is itself a pedagogical act. If students can recognize their own trajectory early, they can correct before it's too late.

### The Knowledgeable Dropout
Arrives with some prior skill. Thinks the course will be easy. Coasts through the first weeks. Hits the architectural complexity mid-course and realizes they're behind. Presents lackluster results because they never built the disciplined habits the course demands.

*Intervention:* Challenge them early. The first assignments should have enough depth that prior knowledge provides a head start, not a free pass. Make architecture the differentiator — knowing C# basics isn't enough.

### The Low-Self-Esteem Student
Believes they can't do art, or programming, or design — picks one dimension to declare impossible and withdraws from it. Sometimes from the start, sometimes after the first difficult exercise. The withdrawal becomes self-fulfilling.

*Intervention:* The art/design/dev triangle (see below) is partly designed for this archetype. Legitimate focus is not avoidance. Help them distinguish between "I'm choosing to focus on design" and "I'm avoiding code because I'm afraid of it." The former is strategic; the latter is surrender wearing strategy's clothes.

### The Overambitious Generalist
Wants to do everything — beautiful art, deep mechanics, elegant design. Refuses to scope. Ends up with a project that's mediocre across all three dimensions because they spread themselves too thin.

*Intervention:* The scoping exercises and documentation milestones exist partly to make this visible early. A project that tries to be excellent at everything will be excellent at nothing under tight temporal constraints.

**General principle:** Present these archetypes on day one. Not as warnings, but as maps. Say: *here are the paths students have taken in the past, here's how each one tends to go, here's what you can do if you recognize yourself in one of them.* Self-knowledge is a prerequisite for producing a satisfying project.

---

## 4. The Argument for Regular Practice

For each hour in the classroom, approximately 2.5 hours of practice at home. This ratio is not arbitrary — it reflects the nature of the material. Unity development is a skill that lives in the hands. You cannot learn it by watching; you learn it by doing, failing, and doing again.

Present this argument through the student archetypes: show how each archetype's trajectory changes depending on whether they practice regularly or not. The knowledgeable dropout who practices stays sharp. The low-self-esteem student who practices discovers they're more capable than they thought. The overambitious generalist who practices learns what's actually feasible.

The additional learning materials matter here — programming games for learning code, curated art and design resources. Give them a rich tapestry of ways to practice outside the classroom. Not homework, but *resources.* The difference is agency: homework is assigned, resources are offered.

---

## 5. Libraries Before Projects

The course doesn't teach projects. It teaches libraries. Projects emerge from libraries.

If students complete all technical exercises across all sessions, they accumulate a **pattern library** — a collection of working, reusable systems (health, detection, spawning, state machines, etc.) that they understand because they built them.

If students complete all design exercises, they accumulate a **design pattern library** — a collection of interaction patterns, feedback techniques, and systemic design approaches they can deploy intentionally.

The project is what happens when you combine elements from both libraries in service of a coherent vision. Without the libraries, the project is improvisation. With them, it's composition.

This reframes the course's arc: the first half builds the libraries; the second half builds from them.

---

## 6. The Starter Prototype as Habitat

Students need a living, explorable project from day one — not an empty scene, not a disconnected tutorial asset. Something they *inhabit* for the first part of the course. A house.

Historical precedents: Unity's 3D Game Kit was close — a full project with drag-and-drop systems and an event architecture — but it was uneditable, a black box. The ball-mechanics prototype was too abstract, too disconnected from what a real game feels like.

**The ideal starter prototype must be three things simultaneously:**
1. **Functional** — a complete playing loop that demonstrates everything (visual design, interaction patterns, event system, core architecture).
2. **Comprehensible** — students can open any system and understand what it does and why it's structured the way it is.
3. **Modifiable** — students can change, extend, and break things. The principles behind each system are exposed, not hidden.

The prototype is the course's textbook — but one you can take apart and rebuild.

---

## 7. Two Databases Per Topic

Every technique page in the course materials should contain two parallel exercise tracks:

**Generic Implementation Database** — the technique in isolation. How does a state machine work? Build one. How does an event channel work? Wire one. These are scales and arpeggios — context-free, focused on the mechanism itself.

**Project Steps Database** — the technique in context. Now use that state machine to drive NPC behavior in the example project. Wire that event channel to connect the detection system to the AI. These exercises demonstrate *why* the technique exists and *how* it serves a design goal.

This dual structure mirrors the session's Phase 3 (system tutorial) and Phase 4 (variation and extension), but it persists as a page-level organizational principle in Notion. Every topic page a student revisits should offer both the isolated technique and its applied form.

**Layering:** Use Part 1, Part 2, etc. for progressive depth within each technique. Part 1 might be the basic state machine; Part 2 adds hierarchical states; Part 3 introduces concurrent state machines. Students advance through layers at their own pace.

---

## 8. The Art / Design / Development Triangle

Students can — and should — choose a focus for their project:

**Design-heavy:** Focuses on the game loop, systemic interactions, and player experience. Simple or abstract visuals. The quality lives in how the systems feel and how they interact.

**Art-heavy:** Focuses on visual quality, atmosphere, environmental storytelling, and feedback polish. Simple mechanics. The quality lives in how the world looks, sounds, and communicates.

**Development-heavy:** Focuses on personal reimplementation of mechanics, advanced systems, or architectural experimentation. May not be visually polished. The quality lives in the code, the structure, the technical ambition.

**The rule:** Choose one focus. Know your strengths — and know your weaknesses. A multi-focus project is viable only for students who are genuinely confident across dimensions. For everyone else, trying to excel at everything under tight temporal constraints produces mediocrity across the board.

This is a production principle, not just advice. It determines what "a good project" looks like for each student and how the instructor evaluates the final work.

---

## 9. Computational Thinking Before Syntax

Introduce abstraction before implementation. The raw sequence:

1. **Computational thinking** — see phenomena as algorithms composed of variables (discrete parts) and control statements. Abstract problems, no code. Simple problems first.
2. **C# fundamentals** — now the syntax. Variables, functions, classes, components. The language as a tool for expressing the thinking from step 1.
3. **Synthesis** — merge the two. Walk through examples that move from logical structure to C# implementation. Then run this forward through the rest of the course.

The principle: *logic before language.* Students who understand the algorithm can learn any syntax. Students who memorize syntax without understanding the algorithm are stuck.

This suggests the C# warm-ups in the session anatomy should begin not with "here's a variable" but with "here's a problem — how would you break it into parts?"

---

## 10. Documentation as a Gate

Three assignments structure the course:
1. **Basics of Unity + VR + Event System** — demonstrating technical competence.
2. **Final project documentation** — the production plan, written *before* heavy implementation begins.
3. **Final project (exam)** — the polished vertical slice, presented.

The documentation assignment is a gate, not a deliverable. It forces students to think about their project before building it. The principle: *it is pointless to develop anything this complex without putting thought into it beforehand.*

This is where the gap between vision and execution first becomes visible. Students envision their ideal project; the documentation forces them to confront scope, feasibility, and the distance between ambition and reality. During production, that distance becomes viscerally felt — and this is a deliberate, humbling lesson the course is designed to produce.

---

## 11. Levels of Development as Conscious Practice

There are different levels at which code can exist — a script, a system, a module, a full game — and different levels of polish appropriate to different stages of production. Prototyping code is not production code. Production code is not ship-ready code.

Students should be *aware of what level they're operating at* and choose it deliberately:
- **Prototyping:** Fast, messy, disposable. The goal is to test an idea, not to build a foundation.
- **Implementation:** Structured, following the course architecture. Reusable systems, clean interfaces, separated data.
- **Polish:** Refinement, edge cases, feedback, resilience. The last mile.

Writing prototype-quality code during the polish phase is a mistake. Writing polish-quality code during the prototype phase is a waste. The discipline is knowing which mode you're in.

---

## 12. Cross-Platform Thinking as Architectural Constraint

The course assumes PC/Mac as the baseline. Beyond that: WebGL, mobile (Android easily, iOS with caveats), and VR (Oculus). Students choose one primary platform for the exam.

But cross-platform awareness is not about shipping to four platforms. It's about making architectural choices — input abstraction, interaction patterns, UI approach — that don't trap you. If your interaction system is hardwired to mouse clicks, porting to VR means rewriting it. If it's abstracted into spatial interactions with swappable input providers, porting is configuration, not reconstruction.

For each platform, create a simple comparative analysis: what changes in controls, visuals, UI, and performance? Students should study these differences explicitly, not discover them in panic during the final week.

---

## 13. Don't Panic — The Opening Posture

The course is hard. Say so on day one. But frame it:
- You can focus on art, design, or development — you don't have to be good at everything.
- Self-knowledge is the prerequisite: know your strengths, know your weaknesses, play to the former, acknowledge the latter.
- The course gives condensed information on multiple topics. It is up to you what you absorb deeply and what you absorb in outline.
- Regular practice is the single strongest predictor of success. The archetypes show why.

The tone is honest without being discouraging. The message: *this will be difficult, and here is exactly how to navigate it.*

---

*This document defines the pedagogical principles. See `philosophy_and_principles.md` for the design and architectural philosophy. See `notes.md` for course structure, session anatomy, and topic sequencing. See `project_design.md` for the example project concept.*
