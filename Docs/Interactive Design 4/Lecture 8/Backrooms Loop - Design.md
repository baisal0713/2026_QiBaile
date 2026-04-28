# Backrooms Loop — Design Document

A small, intentional traversal that teaches state. Worked example for Lectures 8 and 9. Starts as an architectural exercise (L8); finishes as a designed experience (L9).

---

## 1. Experience vision

You enter a quiet room. A pedestal in the centre is missing its object. A door at one end is shut. The other way is a corridor with stairs descending at its far end. You walk down the stairs and find yourself back at the start of the corridor — but the corridor is *slightly* different. You walk it again. Slightly different again. Somewhere down the loop you find the missing object on a pedestal in an inner room. You take it. You return. The original door is now a door.

Three to five passes. Two minutes of walking. One bool, one int, and a few profile swaps doing the work. The participant doesn't see the architecture — they see a room that grew a memory.

The register is the **uncanny familiar**: the same corridor, just-not-quite the same corridor. The horror is repetition with drift, not jump scares.

---

## 2. Design principles

1. **One small goal.** "Find what's missing, bring it back." The participant always knows what they want; the space is what changes.
2. **State is two variables.** `descentCount` and `objectTaken`. Anything that needs more state belongs in a different lesson.
3. **Same atoms, gated on state.** Every visible change in the loop is a profile swap, a GameObject toggle, or a material change driven by `LoopMemory`. No new controllers per descent — just new authoring.
4. **Architecture is invisible.** The participant never feels the teleport. The corridor is the corridor; the descents are descents.
5. **Loop releases through action, not time.** The exit unlocks because of a flag the participant set, not because enough seconds passed.

---

## 3. The participant's arc

| Pass | What they see | What changed under the hood |
|---|---|---|
| 1 | Quiet entry. Empty pedestal. Walled exit. Corridor with stairs. | Initial state. `descentCount = 0`. |
| Descend | Stairs. Brief dim. They appear at the corridor start. | `StairTeleport` increments to 1. |
| 2 | Same corridor, slightly dimmer. A stain on a wall they didn't notice before. | LightManager profile swapped to "Anxious". A wall stain object enabled by a count threshold. |
| Descend | Stairs again. Dim. They appear back at the start. | `descentCount = 2`. |
| 3 | A word emerges on the wall (emission ramp). A column they passed earlier is now humming. | New count thresholds firing. |
| Inner room | A pedestal with an object. They press E. The object is gone from the pedestal. The room exhales. | `Pickup` writes `objectTaken = true`. |
| Return | They walk back through the corridor. The original entry door — walled before — is now a door. | `BoolGate` on the exit reads `objectTaken`. |
| Exit | They walk out. Scene ends. | Done. |

The arc rhymes with the user's framing: *go to the end, then return; the space is different on the way back*. The descent is the way "to the end"; the pickup is the turning point; the return is the release.

---

## 4. State

One ScriptableObject, `LoopMemory.asset`:

| Field | Type | Written by | Read by |
|---|---|---|---|
| `descentCount` | int | `StairTeleport` (on warp) | `LoopProfileSwitch` (LightManager), wall-stain `CountActivator`, gaze-glow `CountActivator`, etc. |
| `objectTaken` | bool | `Pickup` (one-shot) | Exit door `BoolGate`, optional sub-bass at exit, optional inner-room ambience |

Reset on scene reload. No other state in the experience.

This is the simplest object that earns the word *state machine*. There are no transition tables, no enums, no states-as-classes. Just two named variables. The "machine" is the implicit set of `(descentCount, objectTaken)` combinations the participant moves through.

---

## 5. Input and output palette

### Inputs

| Input | Sensor | New for L8/L9? |
|---|---|---|
| Contact (stair descent) | TriggerSensor on the stairs | reused |
| Contact (exit door zone) | TriggerSensor at the door | reused |
| Pickup (E inside zone) | TriggerSensor + KeyInput | **new — L8** |
| Stillness, gaze, proximity | existing controllers | reused for atmospheric layers |

### Outputs

| Output | Channel | Driven by |
|---|---|---|
| Lighting (ambient/emission/skybox/directional) | LightManager (existing) | profile swap on descentCount threshold |
| Wall stain visibility | GameObject SetActive | `CountActivator` reading descentCount |
| Wall text emission | MaterialEmissionIntensity | `CountValueDriver` reading descentCount as a float ramp (L9) |
| Fog density | RenderSettings | `CountValueDriver` (L9, accumulated) |
| Mannequin visibility/teleport | existing ManequinController + count gate | L9 |
| Exit door state | GameObject SetActive / collider toggle | `BoolGate` reading objectTaken |
| Inner-room ambience | AudioSource crossfade | `BoolGate` reading objectTaken |

---

## 6. Spaces

Three rooms, linear, plus one teleport that lies about being a descent.

```
[Entry Room] ──corridor──> [Inner Room with pedestal]
     │
     │ exit (walled until objectTaken)
     ▼
   [outside / scene end]

   At end of corridor: stairs descending.
   StairTeleport target = corridor start.
   This means corridor is traversed N times before
   the participant ever reaches the inner room.
```

**Trick:** the corridor end has stairs descending visually. The trigger at the bottom of the stairs (or under the floor at the bottom) teleports the participant back to the corridor start. They feel like they descended; architecturally they returned.

After K descents (configurable, default 3), the stair teleporter no longer fires — instead, the stairs lead to the **Inner Room** with the missing object. Implementation: a second `BoolGate` on the StairTeleport, gated on `descentCount >= K`. Above the threshold, descending finishes the loop instead of repeating it.

So the loop releases at two points:
- Descents past threshold → reach inner room with pedestal.
- Pickup → exit door opens on the return walk.

---

## 7. L8 vs L9 — what gets built when

### L8: the bones

- `LoopMemory` SO with `descentCount` and `objectTaken`
- `StairTeleport` (extends Teleport, increments count)
- One profile swap on LightManager driven by descentCount threshold
- `Pickup` component (button press inside trigger zone, writes objectTaken)
- `BoolGate` on the exit (one consumer)
- Pickup in inner room is reachable after the threshold; exit unlocks on objectTaken

L8 ships a *working loop* with one observable change per descent and one conditional exit. Crude but readable.

### L9: the texture

- `CountActivator` — toggle GameObjects at threshold (wall stains, mannequin)
- `CountValueDriver` — drive any float (emission intensity, fog density) as a continuous function of descentCount (this is **accumulation** — the L9 mapping)
- Wall text emission ramp across descents
- Fog density accumulating per descent
- Mannequin appearing in different positions per descent (existing `ManequinController` + position list)
- Inner-room ambient bed cross-fades on `objectTaken`
- Exit closing audio gets a sub-bass layer if `objectTaken && descentCount > N`

L9 turns the loop from a demo into a piece. Same architecture, richer authorship.

---

## 8. Architecture brief

The architecture is the one already taught — extended by exactly two ideas:

- **Sensors** emit signals. (existing)
- **Controllers** map signals to outputs via swappable Profiles. (existing)
- **Managers** arbitrate shared outputs. (existing — LightManager)
- **State** is a small ScriptableObject (`LoopMemory`), read and written directly by the controllers that need it. (**new — L8**)
- **State consumers** are tiny components (`BoolGate`, `CountActivator`, `CountValueDriver`) that read a value off the SO and produce one observable change. (**new — L8/L9**)

No flow manager. No director. No narrative tracker. The "state machine" is the set of `(int, bool)` combinations the participant moves through — implicit, never enumerated.

---

## 9. What students do with this

### In L8 (last 20 minutes — Tune the Loop)

1. Walk the loop with the shipped state and the shipped one-change-per-descent.
2. Pick their **threshold**: how many descents before the room shifts.
3. Pick their **channel**: which output reflects the shift.
4. Pick their **direction**: does it grow (more wrongness) or relax (less)?
5. Author a third LightManagerProfile if the two shipped ones don't fit their feel.

### In L9 (full session)

1. Layer two more channels — emission ramp, fog accumulation, mannequin position.
2. Add one `objectTaken`-gated change beyond the exit door (audio, ambience, or post-processing).
3. **Pivot to personal projects:** apply the same `LoopMemory`-style two-variable state to one moment in their own scene. Bring it back next session.

### What the assessment looks like

A student demonstrating this pattern in their own project, with one persistent flag and one downstream consumer, has crossed the line from "I can wire one interaction" to "I can build a small system that remembers." That's the P4 learning objective. Everything more sophisticated — branching, multi-flag conditions, irreversibility — sits on top of the same two-variable foundation.

---

## 10. Open questions / risks

- **Does the descent illusion hold?** If the corridor is too short or the stair geometry too obvious, the participant will read it as "I'm being teleported back," not "I descended." Mitigation: tune lighting at the bottom of the stairs to read as transition; consider a brief fade through LightManager.Dim during the warp.
- **Is the threshold readable?** Three descents may feel arbitrary. Consider making the per-descent change *cumulative* visually so the participant senses a curve, not a switch. (This is the L9 work.)
- **Does the goal land without text?** The empty pedestal is the silent prompt. If students don't read it, fall back to a short callout when looking at the empty pedestal ("missing"). Use the existing `Callout` component.
- **Pickup ergonomics.** First-person pickup in Unity is fiddly. Spec the simplest version: trigger zone + key press + hide object. No physics, no held-in-hand, no inventory.
