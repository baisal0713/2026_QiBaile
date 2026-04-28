# Implementation Guide

## The Principle

Build small, verify constantly. Every implementation step must be **testable on its own** before the next step begins. If you can't see it working, you can't know it's working.

This is not just about avoiding bugs — it's about building confidence. A student (or an AI) who can verify each step never gets lost in a broken system with no idea where the problem is.

---

## The Rule

**Never implement more than one concern before testing.**

If a feature has Data, Simulation, and Presentation layers — implement and verify Data alone, then Simulation alone (reading from Data), then Presentation (reading from Simulation). Never jump to Presentation before Simulation is proven correct.

---

## How to Verify Without Presentation

The simulation layer doesn't know it's being rendered. That means it must be verifiable *without* any visual feedback. Three tools, in order of preference:

### 1. Inspector as Debugger (Primary)

Expose runtime state as readable fields in the Inspector. This is the fastest feedback loop — no code changes needed to observe.

```csharp
public class EntityAgent : MonoBehaviour
{
    [Header("Data")]
    [SerializeField] private EntityData entityData;

    [Header("Debug — Runtime State (Read Only)")]
    [SerializeField, Tooltip("Current energy level")]
    private float _currentEnergy;

    [SerializeField, Tooltip("Number of neighbors detected")]
    private int _neighborCount;

    [SerializeField, Tooltip("Current action being taken")]
    private string _currentAction;
}
```

Why this works: `[SerializeField]` on private fields makes them visible in the Inspector at runtime. Select the entity in the Hierarchy, watch the values change in Play Mode. No View component needed. No debug UI. The Inspector *is* the debugger.

For fields that should be visible but never edited at runtime, a simple `[Header("Debug")]` section communicates intent clearly. A read-only attribute is nice but not essential — the header is honest enough.

### 2. Debug.Log (Targeted)

For events and transitions — things that happen at a moment, not continuously. Log when state changes, not every frame.

```csharp
public void TakeDamage(float amount)
{
    if (_isDead) return;

    _currentHealth -= amount;
    Debug.Log($"{name} took {amount} damage. Health: {_currentHealth}/{data.MaxHealth}");

    if (_currentHealth <= 0f) Die();
}

private void Die()
{
    Debug.Log($"{name} died.");
    _isDead = true;
}
```

**Remove or wrap in `#if UNITY_EDITOR` before shipping.** Debug logs are verification tools, not permanent fixtures.

### 3. Gizmos (Spatial)

For spatial data — detection ranges, movement directions, sensor results. Drawn in the Scene view without affecting the Game view.

```csharp
private void OnDrawGizmosSelected()
{
    Gizmos.color = Color.yellow;
    Gizmos.DrawWireSphere(transform.position, entityData.senseRadius);

    if (_nearestTarget is not null)
    {
        Gizmos.color = Color.red;
        Gizmos.DrawLine(transform.position, _nearestTarget.position);
    }
}
```

---

## Step-by-Step Implementation Pattern

Every feature follows this sequence. Each step is a stopping point where you verify before continuing.

### Example: Entity System (Lecture 1)

**Step 1 — Data: Create EntityData ScriptableObject**
- Define fields: typeName, color, speed, senseRadius, energyDecayRate, etc.
- Create 2–3 assets in the editor with different values
- **Verify:** Select each asset, confirm values are visible and editable in Inspector

**Step 2 — Simulation (State): EntityAgent holds runtime state**
- Add EntityAgent MonoBehaviour to a prefab
- Assign EntityData reference
- Initialize `_currentEnergy` from `entityData.startingEnergy` in Awake
- Expose runtime fields with `[SerializeField]` under a Debug header
- **Verify:** Enter Play Mode, select the entity, watch `_currentEnergy` in Inspector. It should show the starting value. Nothing else happens yet — that's correct.

**Step 3 — Simulation (Lifecycle): Energy decay and death**
- Subtract `entityData.energyDecayRate * Time.deltaTime` in Update
- Destroy when energy ≤ 0
- **Verify:** Enter Play Mode, watch `_currentEnergy` tick down in Inspector. Entity destroys itself when it hits zero. Log the death. Confirm timing matches the decay rate. Still no visuals — just a default cube disappearing.

**Step 4 — Simulation (Sensing): Detect neighbors**
- Iterate entity registry, filter by distance
- Store `_neighborCount` and `_nearestTarget` as debug fields
- Draw Gizmo for sense radius and line to nearest
- **Verify:** Place multiple entities. Select one. Watch `_neighborCount` change as others enter/leave range. Gizmo shows the radius and target line in Scene view.

**Step 5 — Simulation (Thinking): Choose action**
- Look up interaction rules, determine best action
- Store `_currentAction` as a debug string ("MoveToward Blue", "Flee Red", "Wander")
- **Verify:** Watch `_currentAction` in Inspector. Confirm it changes based on what's nearby. Rules should match the EntityData configuration.

**Step 6 — Simulation (Acting): Move**
- Translate position based on chosen action
- **Verify:** Entities move in Scene view (even without proper visuals). Wander looks organic. Attract/repel directions are correct. Consume destroys the target and transfers energy (watch both Inspectors).

**Step 7 — Simulation (Reproduction): Spawn clones**
- When energy ≥ threshold, spawn clone at half energy
- **Verify:** Feed an entity (let it consume). Watch energy climb past threshold. A new entity appears. Both have half the energy. Log the event.

**At this point the entire simulation is working and verified — without writing a single line of visual code.**

**Step 8 — Presentation: EntityView**
- Read EntityAgent state, set color from EntityData, scale by energy
- **Verify:** Entities are now colored. Size reflects energy. The simulation behavior is unchanged — view is purely observational.

**Step 9 — Presentation: Player Spawner**
- Raycast placement, type selection
- **Verify:** Click to spawn. Correct type appears. Immediately participates in simulation.

---

## Why This Order Matters

```
Step 1–7: Simulation works. Verified via Inspector, logs, gizmos.
          If anything is wrong, the bug is in logic — not rendering.

Step 8–9: Presentation added on top.
          If visuals look wrong but Inspector values are correct,
          the bug is in the View — not the simulation.

          If you built everything at once, you wouldn't know where to look.
```

This is the same principle as the architecture itself (Data ≠ Logic ≠ View), applied to the implementation process. **Build in the same order you separated the concerns.**

---

## Practical Rules

1. **One concern per step.** Don't add movement and visuals in the same step. Don't add sensing and decision-making together.

2. **Every step has a verify action.** If you can't describe what you'll check in the Inspector / Console / Scene view, the step isn't well defined.

3. **Debug fields are first-class.** Don't treat Inspector-visible state as temporary hacks. They're your primary verification tool. Keep them organized under `[Header("Debug")]` sections.

4. **Events get logged.** Anything that fires once (death, reproduction, state transition, damage) should produce a log line during development. Continuous state (position, energy, neighbor count) goes in Inspector fields.

5. **Gizmos for spatial data.** Detection radii, movement vectors, target lines, sensor ranges. Use `OnDrawGizmosSelected` (only when selected) to avoid visual clutter.

6. **Remove debug scaffolding intentionally.** When a feature is stable, clean up debug logs and consider whether debug fields should stay (useful for students and designers) or go. Inspector-visible state often stays — it's documentation.

7. **Test at the boundaries.** After each step, test edge cases: What happens with zero energy? With no neighbors? With all entities of the same type? With one entity alone? Edge cases caught early are trivial to fix. Edge cases caught late are nightmares.
