# Lecture Planning: Lessons from Lectures 1–4

> Reference document for writing future lecture guides.
> Based on systematic comparison of guides vs. teacher summaries and critiques across four sessions.
> Last updated after Lecture 4 (31 March 2026).

---

## The Core Problem: Guides Plan 2–3x More Than Fits

Every guide so far has planned 7 steps for a ~2.5-hour session. Every session has completed 2–3 steps. This is not a pacing failure in delivery — it's a scoping failure in planning.

| Lecture | Guide Steps | Steps Completed | Cut Content |
|---------|------------|-----------------|-------------|
| 3 | 7 (Flora → Fauna → Predator → Visual → Balance → Player → World) | ~3.5 | Player enters, creatures reshape world |
| 4 | 7 (Scene → Presence → Spec → Gaze → Contact → Pickup → Free combo) | ~2 | Gaze, contact, pickup, atmosphere, free combo, reflection |

The pattern is consistent enough to be a planning rule:

**A single session holds 2–3 implementation milestones with student work time. Not 7. Not 5. Two to three.**

---

## Time Budget: Where the Hours Actually Go

Based on four sessions of observed timing:

| Activity | Typical Time | Notes |
|----------|-------------|-------|
| Opening / recap / closure of previous work | 5–15 min | Consistently overruns plan. Budget 10, cap at 15. |
| Artist references / framing | 8–12 min | This is a strength. Keep it. Budget 10. |
| Instructor demo of new concept | 10–15 min per concept | Includes live-build, narration, test. |
| Student work period | 10–15 min each | Genuine work, not token. Need minimum 2 per session. |
| Individual troubleshooting during work periods | Eats into work time | Unavoidable but reducible with prep (see below). |
| Transitions, questions, regrouping | 5 min between segments | Invisible in guides, real in sessions. |
| Break | 10–15 min | |
| Unplanned tangents / digressions | 10–20 min | The ProBuilder detour, the MCP mention, the extended audio review. |
| Homework + closing | 5 min | |

**Realistic session capacity: ~100–110 minutes of instruction + 30–40 min of student work + break.**

### The Milestone Template

Each implementation milestone needs:

| Phase | Time |
|-------|------|
| Concept introduction (why, what it enables) | 5 min |
| Instructor live demo | 10–15 min |
| Student work period | 10–15 min |
| Regroup, troubleshoot shared issues, name what was learned | 5 min |
| **Total per milestone** | **30–40 min** |

Three milestones = 90–120 min. One session. That's the budget.

---

## Structural Rules (Derived from Four Sessions)

### 1. Put the hardest new concept in the middle, not the end

Lectures 1–3 all buried the most important content at the end and rushed it. Lecture 4 fixed this — the proximity sensor and spec-driven workflow landed in the middle — and it was the best-structured session so far. Make this the default.

**Session shape:** Recap (short) → Reference/framing → Familiar-pattern baseline (brisk) → **New concept (center, full time)** → Extension or second concept → Homework.

### 2. Cap the recap at 5–10 minutes maximum

Lecture 4 spent ~10 minutes on ecosystem closure (trophic loops, Yellowstone video, three tuning levels). This was content that belonged in Lecture 3. The guide planned a clean thematic break; the session added unplanned closure.

**Rule:** If previous-lecture material wasn't covered, it goes in written notes or a short video — not in the next session's opening. The recap should be: "Last time we built X. Today we build Y. Let's go."

### 3. Do not teach content students cannot experience

Lecture 4 spent 10–15 minutes on 3D spatial audio configuration when most students had no speakers or headphones. The instructor acknowledged this and asked students to bring headphones next time — meaning the audio teaching was a preview they couldn't verify.

**Rule:** If a topic requires equipment students don't have, defer it to the session where they do. Mention it briefly ("we'll add audio next time when you have headphones"), but don't configure and demo something students can only watch.

### 4. Resolve tooling logistics before class, not during

Across Lectures 2–4, recurring time sinks:
- VS Code vs Visual Studio confusion (accepting AI suggestions)
- Copilot extension setup
- Disk space on classroom machines
- Missing speakers/headphones

Each individually small, cumulatively 15–20 min per session.

**Rule:** Send a 2-minute checklist the night before. Spend 60 seconds at session start confirming. Individual troubleshooting happens during work periods, not during instruction.

### 5. Tangents must earn their time by connecting to the session's theme

Good tangents (earned their time):
- Roosegaarde, Rain Room → directly set up presence-based interaction
- Expedition 33 anecdote → normalized simple implementation
- Yellowstone wolves → connected to ecosystem simulation

Bad tangents (didn't earn their time):
- MCP server mention → students can't use it yet, connected to nothing they were doing
- ProBuilder detour (Lecture 3) → 10 min on a cosmetic issue

**Test:** "Will students use or reference this information in the next 30 minutes?" If no, it's a tangent. Give it 30 seconds and a pointer, or cut it.

### 6. When rebuilding a known pattern as a stepping stone, make it brisk

Lecture 4 spent 20+ minutes having students set up trigger sensors and material swaps — a pattern the instructor explicitly called "last year's paradigm." The point was to contrast it with the new proximity-based approach, which is sound pedagogy. But the "before" phase dragged.

**Rule:** If students have done it before, give them the recipe and 5–7 minutes to do it independently. "Set up a trigger sensor on the column, tag 'Player', two material components for on/off. You've done this. Go." Then reconvene, name the limitation, upgrade.

---

## Recurring Pedagogical Debts (Unpaid as of Lecture 4)

These have been flagged in critiques but not yet addressed in class:

| Debt | First Flagged | Status |
|------|--------------|--------|
| Live Git demonstration (commit before AI changes, revert on failure) | Lecture 3 critique | Verbally recommended twice, never demonstrated |
| AI failure recovery workflow (what to do when generated code doesn't compile) | Lecture 4 critique | Instructor troubleshot individually but never modeled for the class |
| VS Code standardization across all machines | Lecture 2 | Still causing friction in Lecture 4 |
| Homework with observable success criteria | Lecture 3 critique | Improved in Lecture 4 but still lacks defined deliverables |

**Suggestion:** Pick one debt to pay at the start of each session. Lecture 5 opening: 90-second live Git demo before the first AI-assisted change. Lecture 6: deliberately provoke an AI generation failure and model the recovery.

---

## Content Spillover: What Lecture 4 Owes Lecture 5+

The Lecture 4 guide planned four interaction types. One was implemented. The remaining three are now deferred:

| Interaction Type | Guide Step | Status | Realistic Session Need |
|------------------|-----------|--------|----------------------|
| Presence → Light/Emission/Sound | Steps 1–2 | Done (continuous proximity + spec-driven controller) | — |
| Gaze → Surface | Step 3 | Not started. GazeSensor exists in toolkit but students haven't used it. | 1 full milestone (~35 min) |
| Contact → Sound | Step 4 | Not started. TriggerSensor reviewed briefly (binary trigger demo). SoundPlayer not built. | 1 full milestone (~35 min) |
| Pickup → Atmosphere | Step 5 | Not started. Pickup, AtmosphereControl, CrystalRoomEffect all unbuilt. | 1.5–2 milestones (~50–60 min) |

**Realistic distribution:**
- Lecture 5: Gaze + Contact (two milestones, one session)
- Lecture 6: Pickup + Atmosphere + free combination (two milestones, one session)

Or compress gaze/contact into one milestone if students use the spec-driven workflow independently, and use the freed time for the audio work that was deferred from Lecture 4 (students will have headphones).

---

## Guide-Writing Checklist

Before finalizing a lecture guide, verify:

- [ ] **Step count is 3 or fewer implementation milestones** (not counting recap, references, homework)
- [ ] **Each milestone has an explicit student work period** (10–15 min, not "if time allows")
- [ ] **The hardest new concept is in the middle** of the session, not the end
- [ ] **Recap is budgeted at 5–10 min max**, with no new vocabulary or video
- [ ] **No content requires equipment students don't have**
- [ ] **Tooling prerequisites are listed** as a pre-session checklist, not in-session setup
- [ ] **Time estimate totals ~100 min of instruction** (the other ~50 min is transitions, questions, troubleshooting, break)
- [ ] **Homework has a defined deliverable** (not just "explore" or "experiment")
- [ ] **One pedagogical debt from the list above** is scheduled for payment
- [ ] **Every tangent/reference passes the 30-minute test**: will students use this information in the next half hour?

---

## What's Working — Keep Doing This

Not everything needs fixing. These patterns are consistently effective and should be preserved:

- **Artist references before implementation.** Anchoring technical work in cultural examples is a signature strength. 2–3 references, ~10 min, every session.
- **Contrast-then-upgrade.** Show the old/simple way, name its limitation, then introduce the new way. Used for replication strategies (L3) and binary-to-continuous interaction (L4). Works every time.
- **Live-build from scratch.** Rebuilding scenes and setups in front of students (rather than opening pre-made ones) models authorship. Keep this for new concepts; skip it for review.
- **Spec-driven AI workflow.** This is genuinely valuable and differentiating. The pipeline (write spec → feed to AI → constrain → iterate) deserves continued investment.
- **The "glue" vocabulary.** Distinguishing reusable modules from project-specific controllers/glue gives students a mental model for when to use generic components vs. write custom scripts.
- **Honest acknowledgment of limitations.** "This audio setup can't work without headphones, so trust me and try it at home" is better than pretending. But better still: defer the content to when the limitation is resolved.
