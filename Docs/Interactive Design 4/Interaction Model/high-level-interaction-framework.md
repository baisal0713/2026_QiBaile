# Interaction Framework — Design Document

> A low-code, AI-assisted interaction framework for Unity.
> Designed for art/design students building installation-compatible interactive experiences.

---

## Design Goals

- Students work **in the inspector**, not in code. Wiring interactions = dragging, dropping, configuring.
- Supports the full spine: from simple reactions (L0) to interconnected systems (L5).
- Readable — a student (or instructor) can open a scene and *see* how the interaction works by inspecting GameObjects and assets.
- Extensible — advanced students or the instructor can write new triggers/actions in C# when needed. AI assistants (Copilot, ChatGPT, Claude) can generate new components that plug into the framework.
- Installation-ready — robust, no editor dependencies at runtime.

---

## Architecture Overview

**Hybrid approach**: Components on GameObjects for visible, scene-placed elements (triggers, actions). ScriptableObjects for invisible, shared, project-level elements (state variables, global events).

```
┌─────────────────────────────────────────────────┐
│                   SCENE                          │
│                                                  │
│   [GameObject]          [GameObject]             │
│   ├─ Trigger            ├─ Action                │
│   │  (conditions)       │  (set variables)       │
│   │  (UnityEvent) ──────│                        │
│   │                     ├─ Action                │
│   │                     │  (raise global event)  │
│                                                  │
└──────────────┬──────────────────┬────────────────┘
               │                  │
               ▼                  ▼
┌──────────────────────────────────────────────────┐
│              PROJECT ASSETS                       │
│                                                   │
│   [Variable: doorUnlocked (bool)]                │
│   [Variable: npcCount (int)]                     │
│   [Variable: tensionLevel (float)]               │
│   [GlobalEvent: onPlayerEnteredZone]             │
│   [GlobalEvent: onAllNPCsGone]                   │
│                                                   │
└──────────────────────────────────────────────────┘
```

---

## Core Pieces

### 1. Variables (ScriptableObjects)

Shared state that any component in any scene can read or write.

**Types**: `BoolVariable`, `IntVariable`, `FloatVariable`, `StringVariable`

Each variable asset:
- Has a current runtime value (resets on play)
- Has an optional default value
- Raises a `changed` event when modified (so triggers can listen)
- Is visible in the inspector — students can watch values change live during play

**Usage**: Create a `BoolVariable` asset called `doorUnlocked`. An Action sets it to true. A Trigger elsewhere checks it as a condition. No direct reference between the two GameObjects needed.

### 2. Global Events (ScriptableObjects)

Decoupled messaging. An event asset that anything can raise and anything can listen to.

**Structure**: `GameEvent` ScriptableObject + `GameEventListener` MonoBehaviour

- An Action raises a `GameEvent` (e.g., `onKeyPickedUp`)
- Any `GameEventListener` in the scene that references that event fires its UnityEvent response
- Optional: events can carry a payload (int, float, GameObject reference) for parameterized communication

**Usage**: An NPC's Action raises `onPlayerApproached`. Three different GameEventListeners in the scene respond — one changes lighting, one triggers a sound, one updates a counter variable. No direct wiring between them.

### 3. Triggers (MonoBehaviours on GameObjects)

Scene-placed components that detect something and fire a response.

**Built-in trigger types**:

| Trigger | Fires when... |
|---------|---------------|
| `ProximityTrigger` | Player enters/exits a collider zone |
| `InteractionTrigger` | Player presses input while in range / looking at object |
| `TimerTrigger` | A duration elapses (one-shot or repeating) |
| `VariableTrigger` | A Variable asset changes or meets a condition |
| `EventTrigger` | A GlobalEvent is raised (essentially a GameEventListener with conditions) |
| `InputTrigger` | A specific input action occurs (abstracted — keyboard, controller, MIDI, etc.) |
| `GazeTrigger` | Player looks at something for a duration |
| `PhysicsTrigger` | A physics event occurs (collision, force threshold) |

**Each trigger has**:
- **Conditions** (optional): a list of variable checks that must be true for the trigger to fire. E.g., "only fire if `doorUnlocked == true` AND `npcCount > 0`"
- **Response**: a UnityEvent that connects to Actions (drag-and-drop in inspector)
- **Settings**: configurable per type (radius, delay, repeat, cooldown, etc.)

### 4. Actions (MonoBehaviours on GameObjects)

Scene-placed components that *do* something when called (usually by a Trigger's UnityEvent).

**Built-in action types**:

| Action | Does... |
|--------|---------|
| `SetVariable` | Sets a Variable asset to a value (bool, int, float, string) |
| `ModifyVariable` | Increments/decrements a numeric variable |
| `RaiseEvent` | Raises a GlobalEvent |
| `ActivateObject` | Enables/disables a GameObject |
| `SpawnObject` | Instantiates a prefab at a position |
| `DestroyObject` | Destroys a GameObject (with optional delay/effect) |
| `MoveObject` | Translates/rotates/scales over time (tween) |
| `SetMaterial` | Swaps or lerps material/shader properties |
| `SetLight` | Changes light properties (color, intensity, range) over time |
| `SetEnvironment` | Changes fog, skybox, ambient, post-processing |
| `PlaySound` | Plays an audio clip (one-shot or looping, spatial or global) |
| `PlayVFX` | Triggers a particle system or VFX graph |
| `PlayAnimation` | Triggers an animation state or parameter |
| `CameraAction` | Switches Cinemachine virtual camera, triggers shake, changes FOV |
| `NPCAction` | Commands an NPC (go to, flee, follow, stop, play animation) |
| `UIAction` | Shows/hides/updates world-space UI elements |
| `SequenceAction` | Executes a list of actions in order, with optional delays between steps |
| `BranchAction` | Checks a condition and executes action A or action B |
| `DelayAction` | Waits, then fires a UnityEvent |

### 5. Conditions

A simple, reusable condition system used by Triggers (and BranchAction).

**Structure**: Each condition references a Variable asset and a comparison.

```
[Variable: npcCount] [GreaterThan] [0]
[Variable: doorUnlocked] [Equals] [true]
```

Multiple conditions on a trigger = AND logic (all must pass).
For OR logic: use multiple triggers, or a dedicated `ConditionGroup` component.

---

## How It Covers the Spine

### L0 — Reaction
`ProximityTrigger` → `PlaySound` action. One trigger, one action, no state.

### L1 — Sequence
`InteractionTrigger` → `SequenceAction` (step 1: `MoveObject` door, step 2: `ActivateObject` next room, step 3: `RaiseEvent` onDoorOpened). Or: first trigger's action enables a second trigger's GameObject.

### L2 — State
`ProximityTrigger` with condition `[timeOfDay > 0.5]` → `SetLight` to night settings.
Same trigger location, different behavior depending on variable state.
Actions use `SetVariable` / `ModifyVariable` to write state that other triggers read.

### L3 — Branching
`InteractionTrigger` → `BranchAction` checks `[npcTrust > 3]`: if true → NPC gives item; if false → NPC flees.
Or: accumulated `SetVariable` calls across the experience create divergent paths later.

### L4 — Feedback Loops
Player enters zone → `ModifyVariable` tensionLevel +1 → `VariableTrigger` on tensionLevel fires → `SetEnvironment` gets darker → `NPCAction` NPCs move faster → player's options narrow → player acts differently → loop continues.
The key: `VariableTrigger` listening to variable changes creates the circular flow.

### L5 — Interconnection
Multiple feedback loops running simultaneously, sharing variables.
NPC subsystem reads and writes `tensionLevel`. Environment subsystem reads and writes `lightLevel`. Sound subsystem reads both. Player actions feed into all of them.
`GlobalEvents` keep everything decoupled — no spaghetti references. Students can inspect any Variable asset to see the current state of the system.

---

## AI-Assisted Workflow

### For students:
- Use AI to **generate new Action or Trigger components** that plug into the framework. E.g., "Write me a Unity MonoBehaviour Action that slowly rotates an object toward the player" → AI produces a component with the right method signature that works with the framework.
- Use AI to **debug wiring** — "my trigger isn't firing, here's my setup" → AI can reason about conditions, variable states, event flow.
- Use AI to **prototype interaction logic** — describe the desired behavior in natural language, get back a suggested configuration (which triggers, which actions, which variables, how they wire).

### For the instructor:
- Use AI to **generate new framework components** as the course needs expand.
- Use AI to **generate tutorial content** — step-by-step instructions for each example project.
- Use AI to **create variations** of example projects for exercises.

### Guardrails:
- The framework is the foundation — AI extends it, doesn't replace it.
- Students should understand the trigger → condition → action → variable flow conceptually before using AI to generate components.
- AI-generated components should follow the framework's conventions (public methods callable via UnityEvent, Variable/Event references as serialized fields).

---

## Package Structure

```
InteractionFramework/
├── Runtime/
│   ├── Variables/
│   │   ├── BoolVariable.cs
│   │   ├── IntVariable.cs
│   │   ├── FloatVariable.cs
│   │   └── StringVariable.cs
│   ├── Events/
│   │   ├── GameEvent.cs
│   │   └── GameEventListener.cs
│   ├── Triggers/
│   │   ├── ProximityTrigger.cs
│   │   ├── InteractionTrigger.cs
│   │   ├── TimerTrigger.cs
│   │   ├── VariableTrigger.cs
│   │   ├── EventTrigger.cs
│   │   ├── InputTrigger.cs
│   │   ├── GazeTrigger.cs
│   │   └── PhysicsTrigger.cs
│   ├── Actions/
│   │   ├── SetVariable.cs
│   │   ├── ModifyVariable.cs
│   │   ├── RaiseEvent.cs
│   │   ├── ActivateObject.cs
│   │   ├── SpawnObject.cs
│   │   ├── DestroyObject.cs
│   │   ├── MoveObject.cs
│   │   ├── SetMaterial.cs
│   │   ├── SetLight.cs
│   │   ├── SetEnvironment.cs
│   │   ├── PlaySound.cs
│   │   ├── PlayVFX.cs
│   │   ├── PlayAnimation.cs
│   │   ├── CameraAction.cs
│   │   ├── NPCAction.cs
│   │   ├── UIAction.cs
│   │   ├── SequenceAction.cs
│   │   ├── BranchAction.cs
│   │   └── DelayAction.cs
│   └── Conditions/
│       ├── Condition.cs
│       └── ConditionGroup.cs
├── Editor/
│   ├── (custom inspectors, variable debugger, event flow visualizer)
│   └── ...
├── Samples~/
│   ├── 01_BasicReaction/
│   ├── 02_SequenceChain/
│   ├── 03_StatefulInteraction/
│   ├── 04_BranchingPaths/
│   ├── 05_FeedbackLoop/
│   └── 06_InterconnectedSystems/
└── Documentation~/
    └── ...
```

Samples map directly to the spine levels — each one a minimal, runnable demonstration of that complexity layer.

---

## Open Questions

- [ ] How much custom inspector work is needed to make this actually friendly? (drag-drop is fine, but condition lists and variable debugging might need polish)
- [ ] Should Variables reset on scene load or persist across scenes? (probably configurable per variable)
- [ ] Event payloads — keep it simple (no payload, just a signal) or support typed payloads from the start?
- [ ] Does the framework need a runtime debug view? (e.g., on-screen overlay showing variable states, event fires — useful for installation testing)
- [ ] How does input abstraction work concretely? InputTrigger wraps Unity's Input System — but mapping to MIDI/OSC needs an adapter layer.
- [ ] NPC subsystem — is `NPCAction` enough, or does the framework need a dedicated NPC behavior module?
