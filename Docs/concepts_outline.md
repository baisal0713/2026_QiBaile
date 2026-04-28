# Course Concepts — Teaching Outline

> A theoretical map of everything covered so far, in the order that makes sense
> to teach. Each section: what it is, why it exists, the canonical doc, and a
> live example in this project.

**Throughline (one sentence):**
*From a sensor-output atom, to composed interactive worlds, to a shipped experience.*

The course climbs that ladder. Each concept below answers a problem the previous
one created. Don't introduce a concept until students feel the pain it solves.

---

## 1. Workflow — spec-driven development with AI

**The idea.** We write a *specification* before code. The spec describes WHAT
the interaction does — fields, behavior, edge cases, what's out of scope. AI
implements from the spec. We review, iterate, refine.

**Why.** The spec is the design surface. Code is the consequence. Keeping these
separate makes the design legible to non-coders and lets us swap the
implementation freely.

**Key practice:** "Implement only what is specified. If unclear, ask." This
header at the top of every spec is non-negotiable — without it, AI fills gaps
with assumptions.

**Templates / docs:**
- `Docs/Templates/SpecTemplate.txt`
- `Docs/Specs/TeleportSpec.txt` (canonical filled-out spec)

---

## 2. The Interaction Atom

**The idea.** Every interaction is a relationship between an input and an output:

> **Input (Signal) → Relationship → Output**

- **Input** — what the system reads about the participant (continuous or binary signal).
- **Relationship** — bound (output follows input) or unbound (output runs free after a trigger).
- **Output** — what changes in the world.
- **Shape** — every relationship has a curve, a range, and an envelope (attack/release).

**Why.** This is the unit of design. Once students see the atom, they stop
asking "how do I make this thing react?" and start asking "what is the
input, what is the relationship, what is the output?"

**Docs:**
- `Docs/Interactive Design 4/Interaction Model/transformation-model-v2.md`
- `Docs/Interactive Design 4/Interaction Model/primitives.md` (catalog of inputs / relationships / outputs)

---

## 3. One atom in code — Controller + Profile (standalone)

**The idea.** A Controller is one atom in Unity: it owns the input, the
relationship, and the output. A Profile (ScriptableObject) holds the tuning —
curve, range, envelope, target values. The Profile is a recipe; the Controller
is the cook.

**This is the default shape.** Most interactions are a single standalone
Controller + Profile. Don't reach for anything bigger until you have to.

**Templates:**
- `Docs/Templates/ControllerTemplate.txt`
- `Docs/Templates/ProfileTemplate.txt`

**Live examples:**
- `StillnessDimController.cs` (bound + binary, drives lighting directly)
- `GazeDrainController.cs` (bound + continuous)
- `Room1EntryController.cs` (unbound — fires a designed sequence)

---

## 4. When atoms share an output — Manager + Profile Override

**The problem.** Two or more Controllers want to drive the *same* output (e.g.
several interactions all want to dim the global lighting). They fight; last
write wins; state drifts.

**The solution.** A Manager: a single author of that shared output, holding
its current state ("the space remembers"). Controllers stop owning the output
and start *requesting* state changes from the Manager.

**The override.** Each Controller may carry its own Profile and pass it to the
Manager. The Manager uses that Profile for that one transition. This is how
Controllers keep ownership of *their* tuning even though they no longer own the
output.

**Pedagogy.** Introduce the Manager *only* when students hit this problem. The
trigger is felt, not announced.

**Template:**
- `Docs/Templates/ManagerTemplate.txt` (includes "When to introduce a Manager")

**Live examples:**
- `LightManager.cs` + `LightManagerProfile.cs`
- `StillnessDimControllerV2.cs` (calls Manager, no override)
- `Teleport.cs` (calls Manager with an override Profile)
- Compare V1 ↔ V2 of `StillnessDimController` to *see* a Controller graduate.

---

## 5. When atoms share a value — ScriptableObject Variables

**The problem.** Multiple unrelated systems read or write the same value
(player energy, time of day, whether the player has the key).

**The solution.** A `FloatVariable` / `IntVariable` / `BoolVariable` SO. One
writer sets `Value`; many readers observe it or subscribe to `OnChanged`.
Decoupled, designer-wireable, observable in the asset's own inspector.

**When NOT to use this.** For *local* state that lives on one component
(`isTeleporting`, `currentState`). Local state stays as a private field with
`[ReadOnly, SerializeField]` for debug visibility. Don't invent shared state
that isn't there.

**Files:**
- `Assets/Scripts/Core/FloatVariable.cs`
- `Assets/Scripts/Core/IntVariable.cs`
- `Assets/Scripts/Core/BoolVariable.cs`

---

## 6. When atoms need to broadcast — GameEvent / GameEventListener

**The problem.** Something happens (player damaged, dynamo charged) and several
unrelated systems should react (VFX, audio, UI). The emitter shouldn't know
who's listening.

**The solution.** A `GameEvent` SO is a named broadcast channel. Any script
calls `Raise()`; any number of `GameEventListener` components on any
GameObjects respond via inspector-wired `UnityEvent`s. Emitter and listeners
never reference each other.

**SO Variables vs. GameEvents:** Variables share *state*; Events share
*signals*. Different concerns.

**Files:**
- `Assets/Scripts/Core/GameEvent.cs`
- `Assets/Scripts/Core/GameEventListener.cs`

---

## 7. Time and progression — lightweight state machines

**The problem.** Reactive interactions answer "what should happen now?". A
state machine answers "what should happen *next*?" — when behavior depends on
which phase of the experience the participant is in.

**The pattern.** Enum of states + a `switch` in `Update` + `EnterState` /
`ExitState` for transitions. Where state machines live in this project:
- Player phases (Wandering → Empowered → Ghost → Overloaded)
- Entity AI (Idle → Patrol → Chase → Attack → Flee)
- World progression (Phase 1 → 2 → 3)

**Doc:**
- `Docs/architecture_guide.md` §"Sequencing — Execution and Time"

---

## 8. Project conventions (the meta layer)

These are not concepts of their own; they are the *style* that every Controller,
Manager, and Profile follows. Teach once, expect everywhere.

- **`[ContextMenu]` on parameterless test verbs.** Right-click → invoke without
  Play-mode wiring.
- **`[ReadOnly, SerializeField]` for runtime state** that mutates AND isn't
  otherwise visible (don't mirror a Light's intensity — it already shows on the
  Light component). For *local* state, not for SO Variables.
- **Two flavors of events**, picked deliberately:
  - `UnityEvent` for inspector wiring (designers drag responses without code).
  - C# `event` for code wiring (other scripts subscribe programmatically).
  Use what the interaction actually needs — don't add events nobody listens to.

**Templates** carry these as a "Conventions" block at the bottom of each.

---

## 9. Shipping — from interactive piece to running installation

**The shift.** Up to here we built an interaction. Now we build an *experience*
that someone can launch and walk away from.

- **Start menu / main menu.** Entry point. Branding, calibration, instructions.
- **Platform decision.** PC desktop, VR (Quest, PCVR), large-screen kiosk,
  multi-platform. Each has different input assumptions, performance budgets,
  and presentation conventions.
- **External sensors.** Depth cameras, MIDI controllers, OSC, Arduino. The
  input layer of the Interaction Atom now extends beyond the keyboard.
- **Build target.** Player settings, scenes-in-build list, XR plugin
  configuration if applicable, packaging.
- **Run-context concerns.** Auto-start on boot, exit handling, error recovery,
  diagnostics for someone who isn't you.

**Pedagogical note.** Shipping reveals the difference between *playing in the
editor* and *running in the world*. Many design choices that felt fine in the
editor break here (lifecycles, teardown, scene reload). It is its own skill.

---

## What we have NOT covered (boundaries)

- Networking / multi-user shared experiences.
- Save/load systems beyond "the SO retains its runtime value if you turn
  off resetOnEnable."
- Asset pipelines (importers, addressables, streaming).
- Full URP / shader authoring (we *use* URP shaders; we don't write our own).
- Audio middleware (Wwise, FMOD).
- Localization.

These are real, but downstream of the throughline.

---

## Where to look

- **Architecture, the long form:** `Docs/architecture_guide.md`
- **Interaction model, theory:** `Docs/Interactive Design 4/Interaction Model/transformation-model-v2.md`
- **Inputs / outputs / relationships catalog:** `Docs/Interactive Design 4/Interaction Model/primitives.md`
- **Templates to start from:** `Docs/Templates/`
- **Live working examples:** `Assets/Scripts/Backrooms/` and `Assets/Scripts/Core/`
- **Filled-out specs to imitate:** `Docs/Specs/`

---

## How the concepts compose (one diagram, mental model)

```
┌─────────────────────────────────────────────────────────┐
│                      EXPERIENCE                         │
│              (state machine, scenes, time)              │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │             INTERACTIONS (atoms)                │   │
│   │                                                 │   │
│   │   Controller + Profile (standalone)             │   │
│   │     ↓                                           │   │
│   │     when shared output → Manager + override     │   │
│   │     when shared value  → SO Variable            │   │
│   │     when shared signal → GameEvent              │   │
│   └─────────────────────────────────────────────────┘   │
│                                                         │
│   spec-driven workflow surrounds all of the above       │
│   project conventions thread through all of the above   │
└─────────────────────────────────────────────────────────┘
                            ↓
                       Shipping
              (menu, platform, sensors, build)
```

A student who understands this diagram understands the course.
