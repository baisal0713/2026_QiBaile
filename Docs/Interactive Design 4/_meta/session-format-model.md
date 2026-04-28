# Session Format Model — Interaction Design 4

> A precision planning tool for estimating lecture content capacity.
> Derived empirically from Lectures 1–4 (March 2026).
> Use this to plan what fits, not what you wish fit.

---

## The Constraint

**Total session: 150 minutes (2h 30m)**

Not all of that is usable for teaching new content. The session is divided into **fixed overhead** (unavoidable, predictable) and **milestone slots** (where the actual learning happens).

---

## Fixed Overhead: ~50 minutes

These activities appear in every session. They are not optional — they are structural. Budget them explicitly so they stop eating into milestone time as "invisible" costs.

| Activity | Budget | Hard Cap | Notes |
|----------|--------|----------|-------|
| Recap / closure of previous work | 8 min | 12 min | "Last time we built X. Today we build Y." No new vocabulary, no new video. If previous content wasn't covered, it goes in written notes — not here. |
| Artist references / framing | 10 min | 12 min | 2–3 references. This is a signature strength — keep it. But it's framing, not teaching. |
| Break | 12 min | 15 min | Place after the first milestone or after ~60 min. Students need it; you need the reset. |
| Transitions between segments | 15 min total | 18 min | ~3 min per transition × 5 transitions. Invisible in guides, real in sessions. Includes "OK, let's move on," questions between segments, regrouping attention. |
| Homework + closing | 5 min | 5 min | Concrete deliverable, stated once, clearly. |
| **Total fixed** | **~50 min** | **~62 min** | |

**Remaining for milestones: ~100 minutes** (88 if overhead runs long).

---

## The Milestone: The Atomic Unit of a Session

A milestone is one complete learning cycle: concept → demonstration → student practice → confirmation. Every session is composed of milestones. Everything else is connective tissue.

### Base Milestone (~35 min)

| Phase | Time | What happens |
|-------|------|-------------|
| **Concept introduction** | 5 min | Why this matters, what it enables, how it connects to what came before. Verbal, maybe whiteboard. No Unity yet. |
| **Instructor live demo** | 12 min | Build the thing in Unity while narrating. Students watch. One concept, one visible result. |
| **Student work period** | 12 min | Students replicate what you just showed. You circulate and troubleshoot. This is non-negotiable — every milestone needs hands-on time. |
| **Regroup** | 5 min | "Who has it working? What broke?" Address shared issues. Name what was learned. Bridge to next milestone. |

**Session capacity at 35 min/milestone: 2.8 → realistically 2–3 milestones.**

Three milestones (105 min) is possible only if overhead stays tight and at least one milestone is a lighter variant.

---

## Milestone Variants

Not all milestones are the same weight. Here are the four types observed across Lectures 1–4, with their actual time signatures.

### Type A: "Build New" — Full Introduction of a New Concept

*Used for: ProximitySensor in L4, Energy lifecycle in L2, FloraController in L3*

| Phase | Time |
|-------|------|
| Concept intro (why, what it enables) | 5 min |
| Instructor live demo (new component/pattern) | 12–15 min |
| Student work period | 12 min |
| Regroup + shared troubleshoot | 5 min |
| **Total** | **35–38 min** |

This is your workhorse. Most milestones are this type.

### Type B: "Spec-Driven AI Build" — Write Spec → Generate → Wire → Test

*Used for: Column Controller in L4. This is the new workflow you're teaching.*

| Phase | Time |
|-------|------|
| Concept intro (what the component should do) | 5 min |
| Collaborative spec writing (you + students) | 10 min |
| AI generation + integration (demo or students) | 12 min |
| Test + troubleshoot + constrain AI output | 8 min |
| **Total** | **35–40 min** |

**Important:** The first time students use this workflow in a session, budget the full 40 min. Subsequent spec-driven milestones in the same session can compress to ~30 min because the process is fresh. This was observable in L4: the first spec (column controller) took longer than adding layers to it.

### Type C: "Review-then-Upgrade" — Rebuild Known → Name Limitation → Introduce New

*Used for: Binary trigger → ProximitySensor in L4, Timer → Energy lifecycle in L2*

| Phase | Time |
|-------|------|
| Quick rebuild recipe (students work independently, you circulate) | 7 min |
| Name the limitation (verbal, 2–3 sentences) | 3 min |
| New concept demo | 12 min |
| Student work on the new version | 10 min |
| Regroup | 3 min |
| **Total** | **35 min** |

**Warning from L4:** The "rebuild known" phase ballooned to 20+ minutes when guided step-by-step. The fix is to give students the recipe and let them do it independently: *"Set up a trigger sensor, tag Player, two material components for on/off. You've done this. Go."* If the review phase exceeds 10 min, you're re-teaching, not reviewing.

### Type D: "Tuning / Exploration" — Open-Ended Work With Parameters

*Used for: Ecosystem balancing in L3 (planned but under-delivered)*

| Phase | Time |
|-------|------|
| Frame the challenge (what to aim for, what the levers are) | 5 min |
| Extended student work period | 15–20 min |
| Share + discuss results (2–3 students show their scenes) | 5–10 min |
| **Total** | **25–35 min** |

This is the lightest milestone type and the most flexible. It works well as a session closer — students are tired of following instructions and want to play. It also produces the moments students remember: "I got all three species to coexist for two minutes."

---

## Session Templates

### Template 1: "Two Full + One Light" (Recommended Default)

The most reliable structure. Two substantial milestones plus one lighter exploration or extension.

```
[0:00]  Recap / closure                          8 min
[0:08]  Artist references / framing             10 min
[0:18]  ── Milestone 1 (Type A or C) ──        35 min
[0:53]  Transition                               3 min
[0:56]  Break                                   12 min
[1:08]  ── Milestone 2 (Type A or B) ──        38 min   ← hardest content here
[1:46]  Transition                               3 min
[1:49]  ── Milestone 3 (Type D) ──             25 min
[2:14]  Transition                               3 min
[2:17]  Homework + closing                       5 min
[2:22]  Buffer / overrun                         8 min
                                         Total: 150 min
```

**Content capacity: 2 new concepts + 1 exploration/tuning exercise.**

### Template 2: "Three Full" (Ambitious, Tight)

For sessions where all content is new and there's no tuning period. Requires zero tangents and tight overhead.

```
[0:00]  Recap (minimal)                          5 min
[0:05]  Artist references                       10 min
[0:15]  ── Milestone 1 (Type A) ──             35 min
[0:50]  Transition                               3 min
[0:53]  Break                                   12 min
[1:05]  ── Milestone 2 (Type A or B) ──        35 min   ← hardest content here
[1:40]  Transition                               3 min
[1:43]  ── Milestone 3 (Type A or B) ──        35 min
[2:18]  Transition                               2 min
[2:20]  Homework + closing                       5 min
[2:25]  No buffer
                                         Total: 150 min
```

**Content capacity: 3 new concepts, but no margin for error.** If any milestone overruns by 5 min, the third gets cut. Use only when all content is pre-tested and students are fluent with the tools.

### Template 3: "Upgrade + Deep Build" (Best for AI-Assisted Sessions)

For sessions where the first milestone is a review-then-upgrade and the second is a spec-driven AI build that needs breathing room.

```
[0:00]  Recap                                    8 min
[0:08]  Artist references                       10 min
[0:18]  ── Milestone 1 (Type C: review→upgrade) ── 35 min
[0:53]  Transition                               3 min
[0:56]  Break                                   12 min
[1:08]  ── Milestone 2 (Type B: spec-driven) ── 40 min  ← core session
[1:48]  Transition                               3 min
[1:51]  ── Extension: add layers to Milestone 2 ── 20 min
[2:11]  Transition                               2 min
[2:13]  Homework + closing                       5 min
[2:18]  Buffer                                  12 min
                                         Total: 150 min
```

**This is approximately what L4 actually did.** Milestone 1 was the trigger→proximity upgrade. Milestone 2 was the spec-driven column controller. The extension was adding light and audio layers to the same spec.

---

## The Low-Level Estimate: What Fits Inside One Milestone

You asked specifically about granularity down to the Column Controller level. Here's how to estimate whether a specific implementation fits inside a single milestone slot.

### Count the "wiring steps"

A wiring step is one atomic action a student performs in Unity:

- Add a component to a GameObject
- Create a ScriptableObject / asset
- Assign a reference in the Inspector
- Set 2–3 parameter values
- Create a child GameObject
- Wire an event (drag function into UnityEvent)
- Create/assign a tag or layer
- Make/save a prefab

**Observed rate: ~1.5–2 minutes per wiring step during student work periods** (includes finding the right field, asking a neighbor, waiting for the instructor to pass by).

**Observed rate during instructor demo: ~1 minute per wiring step** (narration included).

### Example: Column Controller (L4, Type B milestone)

Demo phase wiring steps:
1. Create column object (cylinder + material) — 1 step
2. Add ProximitySensor, set radius, set tag — 1 step
3. Create docs folder, write spec file — 2 steps (this is writing, not wiring)
4. Open Copilot, paste spec as context — 1 step
5. Review generated code, accept, save — 1 step
6. Add generated script to column — 1 step
7. Assign references (sensor, renderer, light) — 1 step
8. Test — 1 step

**Demo: ~9 steps × 1 min = ~9 min** (actual was ~12 min with narration)

Student replication:
Same 8–9 steps × 1.75 min avg = ~16 min (actual was ~12–15 min with troubleshooting absorbed into the period)

**Total milestone: concept (5) + demo (12) + student (12) + regroup (5) = 34 min** ✓ matches observation.

### Example: Flora rebuild + FloraController (L3, Type A milestone)

Demo phase wiring steps:
1. Create Flora object, assign material — 1 step
2. Add Lifecycle component — 1 step
3. Create LifecycleData SO, set values — 2 steps
4. Assign data to Lifecycle — 1 step
5. Enable destroyOnDeath — 1 step
6. Add EnergyProvider, assign Lifecycle, set rate — 1 step
7. Add FloraController, assign Lifecycle — 1 step
8. Create child "Plant Spawner" with Spawner — 2 steps
9. Create child "Replication Spawner" with Spawner — 2 steps
10. Assign spawners to FloraController — 1 step
11. Set threshold values — 1 step
12. Create Flora tag — 1 step
13. Save as prefab — 1 step

**Demo: ~16 steps × 1 min = ~16 min** (observed: ran ~18–20 min, slightly over)

This is a heavy milestone — 16 wiring steps is at the upper bound. Anything above ~12 steps in the demo phase risks exceeding the 15 min demo budget.

### The Planning Rule

**Count your wiring steps. If the demo has >12 steps, split into two milestones.**

| Demo steps | Student steps (same) | Demo time | Student time | Total milestone |
|-----------|---------------------|-----------|-------------|----------------|
| 6–8 | 6–8 | 8 min | 10 min | ~28 min (light) |
| 9–12 | 9–12 | 12 min | 14 min | ~36 min (standard) |
| 13–16 | 13–16 | 16 min | 20 min | ~41 min (heavy — risks overrun) |
| 17+ | — | — | — | **Split it.** |

---

## Overhead Multipliers: The Hidden Time Costs

These are observed costs that guides consistently fail to budget:

| Cost | Per occurrence | Frequency | Session total |
|------|---------------|-----------|--------------|
| Student asks question during demo | 1–2 min | 3–5 per session | 5–8 min |
| Tangent/digression (even "good" ones) | 3–8 min | 1–2 per session | 5–12 min |
| Tool/setup issue during work period | 2–3 min per student | 2–4 students | 6–10 min |
| "Can you show that again?" moment | 2 min | 1–2 per session | 2–4 min |
| Unity crash / unexpected behavior | 3–5 min | 0–1 per session | 0–5 min |

**Expected overhead: 15–25 min per session, already included in the ~50 min fixed budget above.** But if you have a bad day (multiple crashes, a stubborn setup issue, an extended tangent), this can balloon to 35+ min, which eats a full milestone.

**Mitigation:** Pre-test every demo the morning of. Send a setup checklist the night before. Budget 2 tangents max and apply the 30-minute test: "Will students use this information in the next 30 minutes?"

---

## Retrospective Validation

How well does this model predict what actually happened in Lectures 1–4?

### Lecture 1

**Planned:** Framework + Game of Life + Cellular Automata demo + 6-step free-agent build
**Model prediction:** Framework (not a milestone — it's a 20-min lecture block) + references (Game of Life, 15 min) + ~2.5 milestones = the cellular automata demo + 2–3 build steps.
**Actual:** Framework ran 45 min (over budget), Game of Life exploration 15 min, cellular automata demo 15 min, build completed ~4 of 6 steps before time ran out.
**Diagnosis:** The framework section was treated as a milestone-sized block but had no student work period, so it consumed milestone time without producing hands-on learning. If compressed to 20 min, one more build step would have fit.

### Lecture 2

**Planned:** Artist references + AI setup + 6 build steps
**Model prediction:** References (10 min) + AI setup logistics (20 min — this is overhead, not a milestone) + ~2.5 milestones = ~3–4 build steps.
**Actual:** References ~10 min, AI setup ~25 min, completed steps 1–5 well, step 6 rushed.
**Diagnosis:** The AI setup was unbudgeted overhead (~25 min) that displaced one milestone. If pre-loaded as homework, the session would have comfortably held all 6 steps as 2 milestones (steps 1–3 as one light milestone, steps 4–6 as one standard).

### Lecture 3

**Planned (Guide):** 7 steps — Flora → Fauna → Predator → Visual → Balance → Player → World
**Model prediction:** 7 steps = at minimum 4 milestones = needs two sessions. One session holds ~3 milestones = steps 1–4 at best.
**Actual:** Completed ~3.5 steps (Flora rebuild, FloraController, partial FaunaController, partial Predator). ProBuilder detour ate 10 min.
**Diagnosis:** Model accurately predicts the session would reach step 3–4. The guide was scoped for two sessions of content.

### Lecture 4

**Planned (Guide):** 7 steps — Scene → Presence → Spec → Gaze → Contact → Pickup → Free combo
**Model prediction:** 7 steps = ~4 milestones minimum = needs two sessions. One session holds ~2.5 milestones = steps 1–3 (scene + presence + spec workflow).
**Actual:** Completed ~2 milestones (trigger→proximity upgrade + spec-driven column controller with extensions). Gaze, contact, pickup all deferred.
**Diagnosis:** Model accurately predicts the session. The guide was again scoped for two sessions. The audio section (~15 min on unteachable content) displaced half a milestone.

### Model Accuracy

The model correctly predicts the outcome of all four sessions. The consistent error in planning is treating steps as 10–15 minute tasks when they are actually 30–40 minute milestones.

---

## Quick-Reference Planning Card

```
SESSION = 150 min
  Fixed overhead ................ 50 min
  Available for milestones ..... 100 min

MILESTONE = 35 min (±5)
  Concept ....   5 min
  Demo .......  12 min  (≤12 wiring steps)
  Student ....  12 min
  Regroup ....   5 min

CAPACITY = 2–3 milestones per session
  Safe:      2 full + 1 light
  Ambitious: 3 full (zero margin)

WIRING STEP = 1.5–2 min (student) / 1 min (instructor)
  ≤12 steps = fits one milestone
  13–16 = heavy, risk overrun
  17+ = must split

STRUCTURE
  Hardest concept → middle of session
  Review content → brisk, independent, ≤10 min
  Tangents → max 2, must pass 30-min test
  Recap → 8 min, cap at 12
```

---

## Using This Model to Plan a Lecture

1. **List everything you want to teach.** Don't filter yet.
2. **Group into milestones.** Each milestone = one concept that produces one visible result. Count the wiring steps for each.
3. **Count milestones.** If >3, you're planning two sessions. Accept this now, not at minute 120.
4. **Assign types** (A/B/C/D) and sum the time estimates.
5. **Add fixed overhead** (50 min).
6. **Check total against 150 min.** If over, cut the last milestone and make it homework.
7. **Place the hardest milestone in the middle** (position 2 of 3, or position 2 of 2).
8. **Write the timeline** with specific minute marks, like the templates above.
9. **Run the wiring-step count** for each milestone's demo phase. If any demo exceeds 12 steps, split it.
10. **Verify against the checklist** from `lecture-planning-lessons.md`.
