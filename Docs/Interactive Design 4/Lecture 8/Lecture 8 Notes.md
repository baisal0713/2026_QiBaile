# Lecture 8 Guide — Intention and Memory

**Date target:** TBD
**Status:** Draft plan
**Block:** P3 closer / P4 opener — the bridge

---

## The one sentence

> "Now you choose to act, and the space starts to remember what you chose. Today the room gets a goal — and a memory."

## The arc

One coherent scene all session: the **Descent Loop**. A small set of rooms — entry → corridor with stairs → inner room — wired so that descending the stairs teleports you back to the start of the same corridor. Each descent the corridor shifts: light profile, fog, a wall stain, eventually a word fading in. A pickup at the inner room sets a flag. The exit door reads the flag. The participant has a goal ("find what's missing, bring it back") and the space accumulates evidence of their passage.

Same scene grows from "the corridor remembers how many times you've walked it" to "the door knows what you've done." Two new pieces of state, both small, both visible. Same architecture from L7 — controllers route through managers, managers carry state — applied for the first time to a *designed* moment.

This session is also the natural pivot to personal projects: in the closer, students move from the demo scene to applying the same pattern in their own work.

## Two new ideas introduced

1. **State as a small, named ScriptableObject** — `LoopMemory` carrying `descentCount` (int) and `objectTaken` (bool). One asset, two fields, read and written directly by the controllers that need it. Not a state machine class, not a manager-of-managers — just shared variables with a name.
2. **Active interaction (Pickup)** — first input that requires deliberate intent (button press inside a TriggerSensor zone). The transition from "the room reads my body" to "the room responds to my decisions." First flag-writing interaction in the course.

Plus the worked example that ties them together: **content swaps gated on state**. A profile swap, a GameObject toggle, a material change — all driven by the values in `LoopMemory`. Same atoms, different feel, based on what the participant has done.

---

## What was cut (and why)

- **PostProcessManager.** Symmetric with `LightManager`, tempting, but it's a third system in one session — exactly the trap the L6/L7 critiques flagged. Defer to L9.
- **Re-doing the gaze build with a spec.** L7's gaze landed enough as a classification artifact. Reuse the existing `RaycastSensor` + `Focusable` + `FogFocusController` — don't rebuild.
- **A real state-machine class.** The two-flag SO is enough state for the design we're teaching. Anything more architectural belongs to a different course.
- **Multiple new sensor types.** Pickup is the only new input modality this session.

---

## Non-negotiables (debts from prior critiques)

1. **Live Git demo, terminal, in the first 15 minutes.** Five consecutive critiques. Three commands narrated: `git status`, `git add .`, `git commit -m "working state"`. Then later in the session: modify, `git diff`, `git restore .` to revert. Sixty to ninety seconds. If this doesn't happen here, retire the verbal Git recommendation entirely.
2. **Manager/Controller boundary on a slide.** Three lines: *Controller = owns one interaction, decides when to fire it. Manager = owns a shared output, exposes operations on it. Controllers call managers, never the reverse.* Then re-classify L7's components aloud (LightManager, StillnessDimV2, Teleport, LightOscillator). Two minutes.
3. **Rapid-fire matrix opener.** Six familiar examples (teleport, tile-rotation, stillness dim, gaze fog, column proximity, pickup). Students call types under mild pressure. Three to five minutes. Before any building.
4. **Single AI tool recommendation.** "Install OpenCode. We use it for the next two lectures." Stated once, no menu of alternatives.
5. **Commit live at least three times during the session.** Before Milestone 1 (already done in step 1). After Milestone 1 works. After Milestone 2 works. Before any AI generation.
6. **Homework as a deliverable with a forcing function.** Pair-review on entry next session. Specific ask, small enough it cannot be skipped.

---

## Timeline

```
[0:00]  Show-and-tell (L7 homework controller)              10 min
[0:10]  Live Git demo + first commit                         5 min
[0:15]  Manager/controller definition + matrix rapid-fire    8 min
[0:23]  ── MILESTONE 1: descentCount + StairTeleport ──    35 min
        • Frame the loop: one corridor, traversed N times,
          but each pass is different. Show the smallest
          state demo by hand: an int on a SO, a counter
          increment, one observable change at count >= N.
          Live-coded with students, no AI. (10 min)
        • Wire StairTeleport (extends Teleport, increments
          descentCount on warp). Add one profile swap on
          the LightManager driven by the count. (12 min)
        • Student work: drop into their scene, walk the
          loop, see the lighting flip on threshold,
          commit before/after (10 min)
        • Regroup + git commit (3 min)
[0:58]  Break                                               12 min
[1:10]  ── MILESTONE 2: Pickup + objectTaken + exit ──     45 min
        • Concept: presence vs intention — the first
          deliberate action (5 min)
        • Spec-driven AI build: Pickup component (E inside
          TriggerSensor zone, hides the object, sets a
          flag on LoopMemory). Commit before generation.
          Commit after it works. (18 min)
        • Wire the exit door: BoolGate on objectTaken.
          Closed by default; opens once you've taken it. (5 min)
        • Student work: place a grabbable in their scene,
          flip a flag, gate one downstream behavior (15 min)
        • Regroup + git commit (2 min)
[1:55]  ── MILESTONE 3: Tune the loop (Type D) ──           20 min
        • Frame: same loop, your wrongness curve. Show two
          authored profile sets across descents. Students
          pick their threshold (3 vs 5 vs 7), pick their
          per-descent change (light, fog, column, gaze
          glow), and tune. (5 min frame, 12 min work)
        • Share: 1-2 students show their version (3 min)
[2:15]  Homework + final commit + forward thread             8 min
[2:23]  Buffer                                               7 min
                                              Total:  150 min
```

**Hands-off student time: ~37 min.** Above the 30% target. Three commits visible in the History. One pedagogical debt (Git) paid live.

---

## Milestone 1 — descentCount + StairTeleport

### Concept (10 min)

Open with the smallest possible state demo, by hand, no AI. On the whiteboard or in a fresh scene:

```csharp
[CreateAssetMenu]
public class LoopMemory : ScriptableObject
{
    public int descentCount;
    public bool objectTaken;
}
```

A ScriptableObject with two fields. Create the asset. Inspect it during play. Increment from a button. *That's state.* No singletons, no static, no DontDestroyOnLoad — just an asset that two scripts share.

Then the design move: name *what* state means here. *"Each time you walk down the stairs, this number goes up. The corridor reads it. Same architecture. New variable."*

### Demo (12 min)

Build `StairTeleport` — same structure as L7's `Teleport`, plus a reference to a `LoopMemory` and a `descentCount++` before the warp. Spec is one paragraph; if students wrote a teleport spec for L7 homework, this is editing two lines, not regenerating from scratch.

Add one consumer: a `LoopProfileSwitch` on the LightManager (or a tiny `OnCountThreshold` listener) that swaps the LightManagerProfile when `descentCount >= 2`. *"Pass 1 looks calm. Pass 2 looks wrong."*

Walk the loop. The lights flip on the second descent. The state is visible in the SO inspector during play. Commit.

### Student work (10 min)

Minimum: drop the StairTeleport at the end of their corridor, wire it to LoopMemory, watch the count tick, watch one downstream change.
Stretch: pick their own consumer — fog density, a column activating, a gaze stain appearing — driven by the count.

### Regroup + commit (3 min)

Who has the loop walking? Who has a change firing? Commit.

---

## Milestone 2 — Pickup + objectTaken + the exit

### Concept (5 min)

Up to now every input has been ambient: presence, stillness, gaze. The room reads the body. Pickup is different — it's a **decision**. Walk into the zone *and press the button*. The participant has chosen to act.

Frame the design move: *"Now the room can know not just what you did, but what you decided to do."* Pickup writes a flag. Something downstream reads it.

### Demo (18 min)

Spec-driven, OpenCode in front of the class. Spec lives next to LoopMemory, gets committed alongside the code. The shape:

```
Pickup
- input: TriggerSensor zone + KeyInput (E)
- effect: hide the object, set LoopMemory.objectTaken = true,
  fire UnityEvent for downstream feedback (sound, etc.)
- one-shot: never re-fires after objectTaken is true
```

Generate. Wire to a pedestal in the inner room. Commit before generation, commit after it works.

Then the conditional payoff — a tiny new component or just a `BoolGate` on the exit door's collider/visual: enabled only if `objectTaken == true`. The door is a wall on pass 1; a door on pass N.

### Student work (15 min)

Place a grabbable in their scene. One flag. Gate one downstream behavior on that flag — anything: a door opening, a light changing color, a column activating, a fog profile swapping. Their choice.

### Regroup + commit (2 min)

Quick round: who has it firing? Commit.

---

## Milestone 3 — Tune the Loop

### Frame (5 min)

Same loop, same architecture. *Your* wrongness curve. Pick your threshold, pick your change, tune the timing. This is the design step — the engineering is done.

Concretely: students choose
- **Threshold**: how many descents before the room shifts (2? 5?)
- **Channel**: which output reflects the shift (light, fog, columns, gaze glow, mannequin visibility)
- **Direction**: does it grow (more wrongness) or relax (less)?

### Student work (12 min)

Open ended within those three knobs. Two pre-authored profile sets are available as starting points (Calm and Anxious from L7). Encourage authoring a third.

### Share (3 min)

One or two students show. Compare two students who picked different channels for the same threshold. *"Same code, same scene, different meaning."*

---

## Homework

> "Add one persistent state flag to your Backrooms scene. One interaction writes it. One other moment reads it and behaves differently. Bring the project, the spec file, and **one sentence** describing the moment the participant might realize *the room knew what I did*. First ten minutes of L9: pair-review."

The pair-review is the structural change. Three consecutive critiques have flagged that homework is named as missing without anything making it required. Pair-review on entry forces the work into the room.

---

## Forward thread at close

> "Next lesson: irreversibility. State you can't undo. Repeated contact wears something down. The room stops just remembering — it accumulates. And we move from the demo scene to your projects."

Cues L9's accumulated mappings (erosion, growth, threshold buildup) and the pivot to personal-project work.

---

## Pre-build checklist

Before class:

- [ ] **Descent Loop scene staged** — entry room with empty pedestal, corridor with stairs at the far end, inner room with the missing object on its pedestal, exit door (initially walled). Linear, walkable, instrumented with existing controllers but no state wiring yet.
- [ ] **`LoopMemory.cs`** — ScriptableObject with `descentCount` and `objectTaken`. Two `LoopMemory` assets pre-authored: `Loop_Default` and `Loop_Test` (so a profile swap can be demoed). Built in advance but introduced live as the smallest-possible-state demo.
- [ ] **`StairTeleport.cs`** — working reference on instructor's machine. Will be built live via the spec workflow but the reference de-risks the demo.
- [ ] **`Pickup.cs`** — working reference. Same — built live via spec, reference exists.
- [ ] **Two LightManagerProfiles authored per descent threshold** — `Light_Calm`, `Light_Anxious`. Difference is felt, not subtle.
- [ ] **Git repo initialized, first commit pushed** — don't spend class time on `git init`.
- [ ] **Matrix rapid-fire slides** — six examples, including L7's teleport and tile-rotation so students start on familiar ground.
- [ ] **Manager/Controller definition slide** — three lines, ready to point at L7's components.
- [ ] **OpenCode installed and tested** — single recommended tool, no menu.

---

## What the session should feel like

The room has a goal. The participant walks toward it, finds the object, comes back, and the space they walked through is no longer the space they walked through. Stitched together by two integers and a bool.

The architecture from L7 absorbs the new content with no churn: controllers still route through managers, managers still own state. The new piece is that *named* state — `descentCount`, `objectTaken` — is now part of the design vocabulary. Students leave knowing the difference between *the room reacts* and *the room remembers*.

Two ideas that outlive this lecture:

1. **State is small, named, and shared.** A two-field ScriptableObject is enough.
2. **The same atoms, gated on state, become a different experience.** Authorship lives in what you swap and when.

If Milestone 2 runs long, the spec-driven AI build for Pickup can collapse to a hand-written 30-line component. Cut content, not workflow — never the spec step.
