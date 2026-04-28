# Lecture 7 Guide — Managers, State, and Gaze

**Date target:** TBD
**Status:** Draft plan
**Block:** P3 — Active Interaction (first lecture of the block)

---

## The one sentence

> "As your scenes grow, interactions start fighting. Today we learn how to make them collaborate — by splitting *what* from *why*, and by letting the space remember its own state."

## The arc

One coherent scene all session. Same Backrooms room throughout. Three controllers get added to it, one at a time, all driving the same `LightManager`. That's "the single interaction for all these ideas" — one scene, many authors, one lighting state.

## Two new ideas introduced

1. **Manager / controller split** — the manager owns *what the lights do*; controllers own *why the state should change*. Separating detection from output.
2. **State — "the space remembers"** — the manager carries a `LightState` (Lit / Dim). It persists regardless of which controller caused the last transition. Controllers come and go; state stays.

Plus one new input modality: **gaze**.

---

## What was cut (and why)

- **Grab / pickup** → deferred to L8. Belongs to P3 Active Interaction proper. Gaze + grab in one lecture = the "three systems in one session" trap the L6 critique warned against.
- **Other AI tools (MCP, etc.)** → 30-second mention during the Git demo, not a budgeted topic.
- **VR conversion** → dropped entirely. Not relevant to the lesson's spine.

---

## Non-negotiables (debts from prior critiques)

1. **Git demo, live, in the first 15 minutes.** Four consecutive critiques have flagged this. `git add . / commit / diff / checkout --` — three commands, 5 minutes, narrated once. Then repeated after every milestone. If this doesn't happen in L7, the verbal Git recommendations have to stop entirely.
2. **Matrix rapid-fire, opening 5 minutes.** Flagged in L5 and L6, never exercised with students. 6–8 interaction examples on slides, students call out the category. Transforms the matrix from a diagram to a thinking tool.
3. **Commit live at least 3 times during the session.** Before Milestone 1's AI generation. After it works. Before Milestone 2.
4. **Homework as a deliverable with a one-sentence emotion statement.** Not "work on your scene" — a specific ask with a forcing function.

---

## Timeline

```
[0:00]  Student show-and-tell (L6 homework review)       10 min
[0:10]  Git live demo + first commit                      5 min
[0:15]  Frame the day + matrix rapid-fire (6-8 examples)  8 min
[0:23]  ── MILESTONE 1: Manager/Controller + State ──   45 min
        • Problem: show V1, ask "what if a second
          controller also wants to dim?" (5 min)
        • Demo V2: LightManager + Profile + state enum
          visible in inspector; profile swap (15 min)
        • Add autonomous LightOscillator — same manager,
          no player input, toggles Dim/Brighten on a
          timer (10 min). Payoff: two controllers, one
          state.
        • Student work: swap profiles, watch inspector
          state update, commit before/after (10 min)
        • Regroup + git commit (5 min)
[1:08]  Break                                            12 min
[1:20]  ── MILESTONE 2: Gaze as new input ──            40 min
        • Concept: new input modality, identical pattern.
          Show GazeSensor (5 min)
        • Demo: build GazeController that drives
          LightManager (or emission, student picks)
          (12 min)
        • Student work with 2-3 concrete briefs (18 min)
        • Share: 1-2 students show (5 min)
[2:00]  Homework + git final commit + forward thread     8 min
[2:08]  Buffer                                          22 min
                                              Total:  150 min
```

**Hands-off student time: ~28 min** (plus sharing). On target for the 30% hands-off goal the critiques have been pushing for.

---

## Milestone 1 — Manager / Controller Split + State

### Concept (5 min)

Open V1 `StillnessDimController` in front of students. It does three things:
- Detects stillness (input)
- Tweens values (transformation)
- Writes to RenderSettings and materials (output)

Ask: *"If I want a second interaction that also dims the lights — say, gaze drain — what happens?"*

Answer: both controllers write to the same `RenderSettings.ambientIntensity`. Last one wins. They fight.

Name the problem: **coupling**. Each controller knows about specific outputs. If multiple controllers share outputs, they collide.

### Demo (15 min)

Introduce the split:
- **`LightManager`** — owns the outputs. One place where ambient, reflection, emission, skybox exposure, and directional light intensity are written.
- **`LightManagerProfile`** — owns the values and timing for the Lit and Dim states.
- **`StillnessDimControllerV2`** — owns *only* the detection. Calls `lightManager.Dim()` / `.Brighten()`.

Show the state enum in the inspector (`Current: Lit` / `Current: Dim`). As you walk / stop, students watch it flip. That's the "space remembers."

Swap profiles (calm / anxious). Same controllers, different feel. Reinforces the L6 lesson.

### Add a second controller (10 min)

Live-build `LightOscillator` via spec-driven AI workflow:
- No player input
- Timer
- Toggles `Dim()` and `Brighten()` on an interval

**Commit before generating.** Commit after it works.

Now two controllers drive the same manager. Stop the player, watch stillness dim it. Start the oscillator, watch it take over. Run both: **last call wins** — call out this limitation. It's a forward thread ("next lecture we'll talk about how to layer").

Classify in the matrix: oscillator is **Autonomous × Bound** (time → light). Matches catalog item #15 Breathing Light.

### Student work (10 min)

Minimum: wire V2 in their scene, swap profiles, verify state updates in the inspector.
Stretch: add their own controller (any input) that calls Dim/Brighten.

### Regroup + commit (5 min)

Who has it working? What broke? Commit.

---

## Milestone 2 — Gaze

### Concept (5 min)

Gaze is a new *input* — but the pattern is identical. Detection → `lightManager.Dim()` / output. The architecture from Milestone 1 absorbs a new input modality without changing.

Show `GazeSensor` (exists from L4). Raycast from camera forward, detects objects within a cone.

### Demo (12 min)

Build `GazeController`. Two options — pick one live:
- **Gaze → LightManager:** look at a specific object, call `Dim()`. Look away, `Brighten()`. Proves the architecture generalizes.
- **Gaze → emission:** look at a wall stain, emission ramps up (catalog #7 Gaze Glow). Different output, same pattern.

Profile-driven, same structure as L6. Spec-driven AI workflow. Commit before, commit after.

### Student work (18 min)

Three briefs on a slide (critique in L6 said: defined briefs produce work; open "design something" produces silence):

1. **"Gaze glow"** — look at a wall stain, emission ramps up; look away, fades. `GazeSensor` + material emission. *(Binary × Bound, catalog #7)*
2. **"Gaze dim"** — look at a specific object, `lightManager.Dim()`. Look away, `Brighten()`. Reuses everything from Milestone 1 with a different input.
3. **"Your own"** — students with their own idea, go.

Brief #2 is the clincher — it proves the architecture generalizes across inputs with zero new infrastructure.

### Share (5 min)

1–2 students show what they built. Compare solutions to the same brief. Discuss what feels different and why.

---

## Homework

> "Add one new controller to your Backrooms scene that drives the `LightManager`. Pick your input: stillness, gaze, trigger zone, anything. Write **one sentence** describing the emotion or sensation it creates. Bring the project and the sentence."

Constrained enough that everyone can do it. The sentence is the forcing function. Opens L8's show-and-tell.

---

## Forward thread at close

> "Next lesson: intention. Until now the room reads your body — presence, stillness, gaze. Next time we start grabbing, placing, pressing. The space stops waiting and starts responding to decisions."

That cues up the P3 Active Interaction block proper.

---

## Pre-build checklist

Before class:

- [ ] **`LightOscillator.cs`** — the autonomous controller (~30 lines, toggles Dim/Brighten on a timer). Will be built live via spec-driven workflow, but have a working reference on your machine.
- [ ] **`LightManagerProfile` assets** — two presets (e.g. "Calm", "Anxious") for the profile-swap demo. Lit/dim values, dim/brighten durations and curves differ meaningfully.
- [ ] **Scene staged with V1 still wired** — so you can show V1 vs V2 side by side in the problem setup. Duplicate the room if needed.
- [ ] **Git repo initialized** with a first commit. Don't spend class time on `git init`.
- [ ] **Matrix rapid-fire slides** — 6–8 interaction examples. At least one should be ambiguous (invites productive disagreement).
- [ ] **Gaze brief slide** — the three student briefs spelled out with enough detail that a stuck student has a clear target.
- [ ] **VS Code check** — recurring debt since L2. Confirm every student's machine is on the same setup before the session starts.

---

## What the session should feel like

One scene grows throughout. Starts with V1 — a single fat controller that does everything. Ends with three controllers sharing one manager, one `LightState`, one profile. The "before / after" of the day is visible: the room looks the same, but the underlying architecture is now extensible.

Two ideas that will outlive this lecture:
1. **Separate the detection from the output.** Every future interaction follows this pattern.
2. **State lives on the manager.** Controllers are authors of transitions; the manager is the memory.

Git paid, matrix exercised, students hands-on for ~30% of the session, one forward thread cleanly set up. If that lands, L7 is the template for the remaining lectures.
