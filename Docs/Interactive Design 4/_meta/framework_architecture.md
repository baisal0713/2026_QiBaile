# Framework Architecture — Multimedia Design 4

## The Interaction Toolkit

*A collection of generic, reusable Unity modules for building interactive experiences. Designed to be AI-legible: every module is consistent, documented, and extensible so that students and AI assistants can replicate, reconfigure, recombine, and generate new modules fluently.*

---

## Design Priorities

In order of importance:

1. **AI-legible.** Every module follows the same conventions, is documented the same way, and exposes its interface the same way. An AI reading any module immediately understands the pattern and can generate new ones that fit.

2. **Generic and reusable.** Modules do one thing, reference nothing project-specific, and work in any scene. A `ProximityTrigger` is a ProximityTrigger whether it's in a horror game or an art installation.

3. **Inspector-first.** All configuration happens through serialized fields. Students never open a script. They attach, configure, wire.

4. **Easy to replicate.** A student can look at a working example, see which modules are on which GameObjects, see how they're wired, and rebuild it from scratch. The scene IS the documentation.

Architecture, design patterns, and code structure are not teaching goals for this course. They serve silently. The architecture exists so that modules are consistent enough for AI to work with and for the instructor to maintain.

---

## How Students Progress

```
REPLICATE → RECONFIGURE → RECOMBINE → GENERATE

1. Replicate    Copy the demo scene. Rebuild it step by step.
                "I can assemble this from the same parts."

2. Reconfigure  Change the parameters. Swap assets. See what changes.
                "I can make this my own by tuning it."

3. Recombine    Wire existing modules in new ways. Add modules
                from other demos. Layer systems together.
                "I can combine parts into something new."

4. Generate     Describe what's missing to AI. Get a new module
                that fits the pattern. Wire it in like any other.
                "I can extend the toolkit for my specific vision."
```

The framework supports all four stages. Stages 1–3 require zero code. Stage 4 requires clear communication with AI — which means understanding the module vocabulary, not the code.

---

## Architecture Overview

Every module in the toolkit belongs to one of three layers — **Data**, **Simulation**, or **Presentation**. This is the same separation used throughout the project: what things ARE, what things DO, and how things FEEL.

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERACTIVE SCENE                         │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │               PRESENTATION                              │ │
│  │  How the world RESPONDS — what the participant          │ │
│  │  sees, hears, feels. Never changes game state.          │ │
│  │                                                          │ │
│  │  Visual · Audio · Effects · Camera · UI                 │ │
│  └──────────────────────┬─────────────────────────────────┘ │
│                         │ reads from / triggered by          │
│  ┌──────────────────────▼─────────────────────────────────┐ │
│  │               SIMULATION                                │ │
│  │  What the world DOES — detection, decisions,            │ │
│  │  sequences, state changes, spawning, management.        │ │
│  │                                                          │ │
│  │  Triggers · Sequencing · State · Actions · Managers     │ │
│  └──────────────────────┬─────────────────────────────────┘ │
│                         │ reads from                         │
│  ┌──────────────────────▼─────────────────────────────────┐ │
│  │                    DATA                                 │ │
│  │  What things ARE — shared variables, event channels,    │ │
│  │  configuration. The single source of truth.             │ │
│  │                                                          │ │
│  │  Variables · Events · Configuration Assets              │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

The rules are simple:
- **Data** is read by everything, owned by no one. ScriptableObject assets in the Project window.
- **Simulation** reads from Data, maintains runtime state, makes decisions, acts on the world. Components on GameObjects.
- **Presentation** reads from Simulation and Data, produces everything the participant perceives. Never writes game state. Components on GameObjects.

Everything connects through two mechanisms:
- **UnityEvents** — drag a module's method into another module's response slot. Direct, visible in Inspector.
- **Data assets** — a module writes to a Variable; elsewhere, another module reacts when that Variable changes. Indirect, decoupled.

---

## Layer 1 — Data

ScriptableObject assets that live in the Project window. Created once, referenced by any module in any scene. Students create and configure these as assets — no code.

### Variables (Shared State)

A variable is a single value that any module can read or write. It's the world's memory.

| Type | Holds | Example Use |
|---|---|---|
| `BoolVariable` | true / false | `doorUnlocked`, `hasKey`, `lightsOn` |
| `IntVariable` | whole number | `npcCount`, `itemsCollected`, `visitCount` |
| `FloatVariable` | decimal number | `tensionLevel`, `timeOfDay`, `playerSpeed` |
| `StringVariable` | text | `currentPhase`, `playerName` |

Each variable:
- Has a **default value** (set in Inspector)
- Resets to default on play (configurable)
- Raises an **OnChanged** event when modified — other modules can listen
- Is watchable in the Inspector during play mode

**How students use it:** Right-click > Create > Data > Variables > Float Variable. Name it `tensionLevel`. Set default to 0. Now any trigger can modify it, any presentation module can read it, and any other trigger can react when it changes.

### Event Channels (Decoupled Broadcast)

An event channel is a named signal. Any module can raise it. Any module can listen. Neither side knows the other exists.

| Type | Carries | Example Use |
|---|---|---|
| `GameEvent` | nothing (pure signal) | `onPlayerEnteredZone`, `onDoorOpened` |

Each event:
- Is a ScriptableObject asset in the Project window
- Modules raise it by calling `Raise()` (wired via UnityEvent)
- Modules listen via a `GameEventListener` component (fires a UnityEvent response)

**How students use it:** Create `onKeyPickedUp` event asset. A trigger raises it when the key is grabbed. Three GameEventListeners elsewhere in the scene respond — one plays a sound, one opens a door, one updates a UI element. No direct wiring between any of them.

### Configuration Assets

Module-specific settings stored as ScriptableObjects. Same data-driven principle — change the asset, change the behavior, no code touched. Created per-module as needed:
- A lighting preset SO that a LightController reads from
- An NPC behavior profile SO that defines wander speed and flee distance
- A sequence definition SO that lists steps and timing

---

## Layer 2 — Simulation

Everything that makes the world tick — detection, decisions, timing, actions, spawning, scene management. This is the broadest layer. Modules are attached to GameObjects, configured in the Inspector.

### Triggers (Detection)

A trigger detects something and fires a response. It's the world's attention.

| Module | Detects... |
|---|---|
| `ProximityTrigger` | Player enters / exits a collider zone |
| `InputTrigger` | Player presses a button / key |
| `TimerTrigger` | A duration elapses (one-shot or repeating) |
| `VariableTrigger` | A variable meets a condition |
| `GazeTrigger` | Player looks at something for a duration |
| `PhysicsTrigger` | A collision or force event |

Every trigger has:
- Optional **conditions** (variable checks that gate firing)
- A **response** (UnityEvent — wired in Inspector)
- Per-type **settings** (radius, delay, cooldown, repeat, etc.)

**The pattern:** A trigger answers ONE question: "Did something happen?" It never decides what to do about it. The response is wired in the Inspector, pointing at other simulation or presentation modules.

### Sequencing (Temporality)

Modules that control WHEN things happen — ordering, delays, rhythm.

| Module | Does... |
|---|---|
| `SequenceRunner` | Executes a list of UnityEvent steps in order, with configurable delays between each |
| `DelayedAction` | Waits a duration, then fires a UnityEvent |

A `SequenceRunner` might: step 1 → dim lights, wait 2 seconds, step 2 → play sound, wait 1 second, step 3 → spawn NPC. It orchestrates the timing of other modules.

### State Logic (Decisions)

Modules that read and write the world's state — the thinking layer.

| Module | Does... |
|---|---|
| `SetVariable` | Sets a variable to a specific value |
| `ModifyVariable` | Increments / decrements a numeric variable |
| `BranchAction` | Checks a condition → fires response A or response B |

### Actions (World Manipulation)

Modules that change the scene — creating, destroying, moving between scenes.

| Module | Does... |
|---|---|
| `Spawner` | Instantiates a prefab at a location |
| `Destroyer` | Destroys a GameObject with optional delay |
| `SceneLoader` | Loads a scene (transition between spaces) |

### Managers (Orchestration)

Scene-level modules that coordinate larger systems. Project-specific, often AI-generated:
- `ProgressionManager` — manages phases / chapters of the experience
- Custom managers as needed for specific projects

---

## Layer 3 — Presentation

Modules that produce everything the participant perceives. They read from simulation and data. They never write game state. The world could run without them — they're the sensory surface.

### Visual

| Module | Does... |
|---|---|
| `MaterialChanger` | Lerps or swaps material properties (color, emission, texture) over time |
| `LightController` | Animates light color, intensity, range over time |
| `EnvironmentChanger` | Changes fog, skybox, ambient light, post-processing |
| `ObjectMover` | Tweens position / rotation / scale over time |
| `ObjectActivator` | Enables / disables GameObjects |

### Audio

| Module | Does... |
|---|---|
| `SoundPlayer` | Plays audio — one-shot or loop, spatial or global |

### Effects

| Module | Does... |
|---|---|
| `VFXPlayer` | Triggers a particle system or VFX Graph |
| `AnimationPlayer` | Triggers an Animator state or parameter |

### Camera

| Module | Does... |
|---|---|
| `CameraController` | Switches Cinemachine cameras, shake, FOV changes |

### UI

| Module | Does... |
|---|---|
| `WorldUI` | Shows / hides / updates world-space UI elements |

**The pattern:** Every presentation module exposes public methods (e.g., `Play()`, `Activate()`, `FadeTo(float)`) that other modules call via UnityEvent. Configuration (duration, easing, target values) lives in serialized fields or Data SOs.

---

## How It All Wires Together

A concrete example — a room that darkens when you enter and remembers your visit:

```
[ProximityTrigger]                    SIMULATION — detects
  Conditions: (none)
  On Enter → calls:
    [ModifyVariable]                  SIMULATION — state change
      Target: visitCount (+1)
    [SetVariable]                     SIMULATION — state change
      Target: playerInRoom (true)
    [SequenceRunner]                  SIMULATION — temporality
      Step 1: [LightController].FadeTo(0.2)    PRESENTATION
      Step 2: wait 1s
      Step 3: [SoundPlayer].Play()              PRESENTATION
      Step 4: [EnvironmentChanger].SetFog(0.8)  PRESENTATION

  On Exit → calls:
    [SetVariable]
      Target: playerInRoom (false)
    [LightController].FadeTo(1.0)

[VariableTrigger]                     SIMULATION — detects state change
  Watches: visitCount
  Condition: visitCount >= 3
  Response → [BranchAction]
    If hasKey == true → [ObjectActivator].Activate(exitDoor)
    If hasKey == false → [Spawner].Spawn(shadowCreature)
```

Everything visible in the Inspector. Everything configurable. No code written.

---

## How AI Extends the Toolkit

The module catalog above covers common needs. When a student needs something specific, they describe it to AI using the vocabulary:

> "I need a **presentation module** that slowly rotates an object to face the player. I want a serialized field for rotation speed and a public `Activate()` method I can call from a trigger."

> "I need a **simulation module** that fires when two variables are both true at the same time."

> "I need a **data asset** that defines a list of waypoints with wait times at each one, so an NPC mover can read from it."

AI generates a module that follows the same shape as every other module in the toolkit. The student wires it in the Inspector like anything else.

**Modules don't need to be perfectly generalizable.** A student building an installation about gravity doesn't need a universal physics module — they need a `GravityShifter` that does exactly what their project requires. AI generates that in seconds if the student can describe it clearly. The vocabulary IS the prompt engineering.

---

## Module Conventions (For AI Generation)

These conventions exist so AI (and students reading AI output) can work consistently. Every module follows the same shape:

```csharp
// ============================================
// Module Name
// ============================================
// PURPOSE: One sentence — what this module does.
// LAYER: Data / Simulation / Presentation
// USAGE: How to set it up in the Inspector.
// ============================================

using UnityEngine;
using UnityEngine.Events;

public class ModuleName : MonoBehaviour
{
    [Header("Configuration")]
    [SerializeField] private /* references to SOs or components */;

    [Header("Settings")]
    [SerializeField] private /* per-instance values */;

    [Header("Response")]
    [SerializeField] private UnityEvent onSomething;

    // --- Public interface (called via UnityEvent) ---

    public void DoTheThing() { /* ... */ }

    // --- Internal ---

    private void HandleInternal() { /* ... */ }
}

// ============================================
// SETUP
// ============================================
// Step-by-step Inspector setup instructions.
// ============================================
```

### The Rules

1. **Header comment block** at the top: PURPOSE, LAYER, USAGE. AI reads this to understand what the module does and where it fits.
2. **Setup block** at the bottom: step-by-step Inspector instructions. Students follow this when replicating. AI generates this for new modules.
3. **`[SerializeField]` for everything.** No public fields. No hardcoded values.
4. **`[Header]` groups** in the Inspector: Configuration, Settings, Response/Events.
5. **Public methods are the API.** Name them clearly: `Play()`, `Activate()`, `FadeTo()`, `SetValue()`. These are what other modules call via UnityEvent.
6. **One script, one job.** If a module does two things, it should be two modules.
7. **No cross-references between modules** except through Data assets (Variables, Events) or Inspector wiring (UnityEvent).

These conventions mean: any module a student opens looks the same. Any module AI generates looks the same. Any module from any demo can be dropped into any project.

---

## Package Structure

```
InteractionToolkit/
├── Runtime/
│   ├── Data/
│   │   ├── Variables/
│   │   └── Events/
│   ├── Simulation/
│   │   ├── Triggers/
│   │   ├── Sequencing/
│   │   ├── State/
│   │   └── Actions/
│   └── Presentation/
│       ├── Visual/
│       ├── Audio/
│       ├── Effects/
│       └── Camera/
├── Editor/
└── Samples~/
    ├── 01_ResponsiveWorld/
    ├── 02_Unfolding/
    ├── 03_Memory/
    ├── 04_Consequence/
    ├── 05_LivingSystems/
    └── 06_Ecology/
```

Each sample is a minimal, runnable scene that demonstrates a complexity level. Students replicate these, then diverge.

---

## What This Document Is For

This document exists for:
- **The instructor** — to maintain consistency when building or commissioning modules.
- **AI assistants** — to understand the pattern when generating new modules.
- **Advanced students** — who want to peek under the hood later in the course.

Students don't study this document. They learn the module vocabulary by building — replicating demo scenes, reconfiguring parameters, recombining modules, and eventually generating new ones with AI. The architecture is invisible. The modules are visible. The projects are the curriculum.
