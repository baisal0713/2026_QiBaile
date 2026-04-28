# Lecture 3: Predator, Prey & Balance

## Overview

**Theme:** From chain reactions to living ecosystems — creatures that sense, pursue, flee, consume, and self-regulate. Then: the player enters the world and changes it by being there.

**Duration:** ~2.5 hours

**Starting point:** Students have the Lecture 2 scene — Flora (timer-based), Fauna (energy lifecycle, NavMesh wander), Replicating Crystal. Creatures live, die, and spawn the next creature in a chain. There is no real ecosystem yet — just a cascade.

**By the end:** A self-balancing three-species ecosystem with visual energy feedback, a player avatar whose presence affects creature behavior, and an environmental effect where creatures reshape the world around them.

---

## What's Already Built

Almost everything needed for this lecture exists in the toolkit. The work is wiring, configuring, and understanding — not writing code.

| Component | What it does | Students used it? |
|-----------|-------------|-------------------|
| `FaunaController` | Flee threats, seek food, wander when idle. Replicates at energy threshold. | No — new this lecture |
| `FloraController` | Spawns plant children as energy grows. Replicates at max energy. | No — new this lecture |
| `Consumer` | Eats nearest detected target within radius. Adds energy to lifecycle. | No — new this lecture |
| `ProximitySensor` | Detects objects by tag within radius (OverlapSphere). | No — new this lecture |
| `LifecycleView` | Emission color + light intensity scale with energy. Pulse on gain. | No — new this lecture |
| `EnergyProvider` | Adds energy per second (sunlight, nutrients). | No — new this lecture |
| `Lifecycle` | Energy decay, death on zero. | Yes — from Lecture 2 |
| `LifecycleData` | SO: starting energy, max, decay rate. | Yes — from Lecture 2 |
| `NavMeshMotor` | Movement wrapper for NavMeshAgent. | Yes — from Lecture 2 |
| `NavMeshWander` | Random NavMesh destination when idle. | Yes — from Lecture 2 |
| `Spawner` | Instantiate prefabs in area. | Yes — from Lecture 2 |
| `Timer` | Ticks at interval, fires events. | Yes — from Lecture 2 |
| `MaterialColor` | Animate material color. | No — new this lecture |
| `MaterialEmissionIntensity` | Animate emission glow. | No — new this lecture |

---

## Artist References (~10 min)

Open with 2–3 references. Frame: *"Last week your creatures lived and died on a clock. This week they live and die because of each other."*

Suggested references (pick what resonates):

- **Ian Cheng — *Emissaries* trilogy** — AI creatures with drives and relationships that evolve without the artist's hand. Nobody controls the outcome. The system *is* the artwork.
- **Theo Jansen — *Strandbeests*** — Creatures shaped by wind, sand, water. Physical constraints produce behavior that looks alive. Our digital version: energy constraints produce ecosystem behavior.
- **"How Wolves Change Rivers" (YouTube, 4 min)** — Wolf reintroduction to Yellowstone changed deer behavior, which changed vegetation, which changed erosion, which literally changed the course of rivers. *One species reshaping the physical world.* This is exactly what we'll build at the end.

Key message: **Simple creatures with simple needs, at scale, reshape their world.**

---

## Step 1: Flora Gets a Real Life (~15 min)

**Goal:** Replace Flora's timer-based death with an energy-based lifecycle. Flora now lives on "sunlight" (EnergyProvider) and can grow and replicate.

**Concept:** Flora in Lecture 2 was a countdown. Now it's a living thing — it receives energy from the environment, grows, and when it has enough energy, reproduces. This is the foundation everything else depends on.

### Setup

1. Open the Lecture 2 ecosystem scene (or start fresh with terrain + NavMesh)
2. Open the Flora prefab

### Remove timer-based life
- Remove `Timer` component
- Remove `Destroy` component
- Keep the mesh, collider, and material

### Add energy-based life
- Add `Lifecycle` component
- Create new `LifecycleData` SO: call it **Flora Data**
  - Starting energy: **50**
  - Max energy: **100**
  - Decay rate: **3**
- Assign Flora Data to Lifecycle
- Enable `destroyOnDeath`

### Add sunlight (energy input)
- Add `EnergyProvider` component
  - Assign Lifecycle reference
  - Energy per second: **5** (net gain = 5 - 3 = 2 energy/sec)
- Frame this: *"This is sunlight. Energy comes in from the world. As long as income > decay, the plant grows."*

### Add FloraController
- Add `FloraController` component
  - Assign `Lifecycle`
  - Create a child GameObject: **"Plant Spawner"** with `Spawner` (prefab = Flora, count = 1, area size = small ~(3,0,3))
  - Assign to `plantSpawner`
  - Create another child: **"Replication Spawner"** with `Spawner` (prefab = Flora, count = 2, area size = (5,0,5))
  - Assign to `replicationSpawner`
  - Energy per plant: **25**
  - Replication energy: **90**

### Tag it
- Set Flora's tag to **"Flora"** (create tag if needed)

### Test
- Place a few Flora in the scene. They should grow, spawn small plants, eventually replicate.
- *"Without anything eating them, Flora takes over. Sound familiar?"* (callback to Lecture 2's exponential crash)

---

## Step 2: Fauna Becomes a Herbivore (~20 min)

**Goal:** Fauna can now sense Flora, chase it, eat it, and gain energy. This is the first real ecosystem link.

**Concept:** Three new components turn a wandering creature into a herbivore: a sensor (eyes), a consumer (mouth), and a controller (brain). All already built — we just wire them.

### Setup
- Open the Fauna prefab

### Add sensing
- Add `ProximitySensor` component
  - Radius: **15**
  - Required tags: **["Flora"]**
  - Name it or note it as the **food sensor**
- *"This is the creature's awareness. It knows what Flora is nearby and how far away."*

### Add consumption
- Add `Consumer` component
  - Assign `Lifecycle`
  - Assign the food `ProximitySensor`
  - Consume radius: **2**
  - Energy gain: **30**
- *"When Flora is close enough, the creature eats it. Eating = energy."*

### Add the brain
- Add `FaunaController` component
  - Assign `Lifecycle`, `NavMeshMotor`, `NavMeshWander`
  - Assign food sensor (`foodSensor`)
  - Leave `threatSensor` empty for now
  - Leave `replicationSpawner` empty for now
  - Replication threshold: **0.8**
  - Replication cost: **0.5**

### Create Fauna LifecycleData
- New SO: **Fauna Data**
  - Starting energy: **60**
  - Max energy: **100**
  - Decay rate: **8** (higher than Flora — animals burn energy faster)

### Tag it
- Set tag to **"Fauna"**

### Test
- Spawn several Flora and a few Fauna.
- Watch: Fauna wanders → detects Flora → moves toward it → consumes it → energy goes up.
- *"Now there's a relationship. Fauna needs Flora. Without Flora, Fauna starves."*

### Observe the dynamics
- Too many Fauna? Flora disappears, then Fauna starves.
- Too much Flora? Fauna thrives, multiplies... then eats everything.
- *"We don't have balance yet. We need a predator."*

---

## Step 3: The Predator (~15 min)

**Goal:** A third species that hunts Fauna. Fauna now flees threats. The three-species loop is complete.

### Create Predator prefab
- Duplicate Fauna prefab, rename to **Predator**
- Give it a distinct look (different mesh, color, scale — larger)

### Configure sensors
- Change food sensor required tags to **["Fauna"]**  (predator eats fauna)
- Add a second `ProximitySensor`:
  - Radius: **20** (predators see further)
  - Required tags: leave empty or set to player tag later
  - This is the **threat sensor** — unused for now, ready for Step 6

### Configure Consumer
- Consume radius: **2.5**
- Energy gain: **50** (big meal)

### Configure FaunaController
- Assign food sensor (the one targeting Fauna)
- No threat sensor yet
- Flee distance: **15**
- Replication threshold: **0.8**
- Replication cost: **0.5**

### Create Predator LifecycleData
- New SO: **Predator Data**
  - Starting energy: **80**
  - Max energy: **120**
  - Decay rate: **6** (slower metabolism — can survive longer between meals)

### Tag it
- Set tag to **"Predator"**

### Go back to Fauna — add threat awareness
- Open Fauna prefab
- Add a second `ProximitySensor`:
  - Radius: **12**
  - Required tags: **["Predator"]**
- Assign this as `threatSensor` on FaunaController
- Set flee distance: **10**

### Test
- Spawn: many Flora, several Fauna, 1–2 Predators
- Watch the priority system: Fauna flees predator (top priority) > seeks food > wanders
- *"Fauna now has a dilemma: eat or run. That tension is what makes it feel alive."*

---

## Step 4: Visual Feedback (~15 min)

**Goal:** Make energy visible. Creatures glow when healthy, dim when starving. Pulse when they eat.

**Concept:** The ecosystem is running but students can't *see* the energy. This step makes the invisible visible — crucial for both aesthetics and tuning.

### Add LifecycleView to all three species

For each prefab (Flora, Fauna, Predator):

- Add `LifecycleView` component
  - Assign `Lifecycle`
  - Assign `Renderer` (the mesh renderer)
  - Choose a distinct `emissionColor` per species (green / orange / red)
  - Max emission intensity: **3–5** (experiment)
  - Optional: add a child `Point Light`, assign to `pointLight`
  - Max light range: **5–8**
  - Pulse scale: **1.15**
  - Pulse duration: **0.2**

### Optional: MaterialColor for state changes
- Add `MaterialColor` to Fauna/Predator
- Wire Consumer's `consumedEvent` → `MaterialColor.Animate` with a brief flash color
- *"A little flash when they eat. Feedback that something happened."*

### Test
- The scene should now visually pulse with life — bright healthy creatures, dimming starving ones
- *"Now you can read the ecosystem. Bright = thriving. Dark = dying. You can feel the balance."*

### Experiment with PlantGrow on Flora
- If not already present, add `PlantGrow` to Flora
- Plants animate from zero to full size on spawn
- Gives a sense of organic growth

---

## Step 5: Balance & Tuning (~25 min) **[IMPORTANT — give this time]**

**Goal:** Students tune their ecosystem until all three species coexist. This is the creative design space.

**Concept:** Everything up to now was assembly. This is where design happens. The same components, with different numbers, produce wildly different worlds — extinction, explosion, fragile equilibrium, oscillating cycles.

### The tuning variables

Walk through each lever and what it controls:

| Parameter | Where | What it affects |
|-----------|-------|----------------|
| Decay rate | LifecycleData | How fast creatures starve — sets the "clock" |
| Energy gain | Consumer | How much eating helps — sets value of food |
| Sensor radius | ProximitySensor | How far creatures see — affects chase/flee success |
| Speed | NavMeshAgent | Who catches whom |
| Replication threshold | FaunaController | When population grows — higher = slower growth |
| Replication cost | FaunaController | Energy split on reproduction — higher = weaker offspring |
| EnergyProvider rate | EnergyProvider (Flora) | How fast the base of the food chain grows |
| Spawner count & area | Spawner | How many offspring, how spread out |
| Flora energyPerPlant | FloraController | How often Flora drops new plants |

### Spawner timing for population seeding

Show how to use `Timer` + `Spawner` for continuous population input:

- Create an empty **"Flora Spawner"** GameObject
- Add `Timer`: duration = **8**, ticks = **0** (infinite), autoStart = true
- Add `Spawner`: prefab = Flora, count = 1–2, area size = large (covers terrain)
- Wire `Timer.OnTick` → `Spawner.Spawn`
- *"This is rain. Sunlight. The environment itself restocking the base of the food chain."*

Do the same for Fauna and Predator with longer intervals:
- Fauna spawner timer: **15–20 sec**
- Predator spawner timer: **30–45 sec**

*"These timers are your ecosystem's life support. Tune them to control the baseline — how fast each population recovers from crashes."*

### The challenge

> **"Make all three species coexist for 2 minutes."**

Give students 10–15 minutes of hands-on tuning. Walk around, observe, help.

### Common failure modes to discuss

- **Flora extinct → everything dies.** Base of food chain too weak. Increase EnergyProvider rate or spawner frequency.
- **Predator extinct → Fauna explodes → Flora extinct.** Predator can't catch Fauna (too slow? sensor too small?). Or Predator decay too high.
- **Fauna extinct → Predator starves.** Fauna too slow, too little energy gain, or Predator too efficient.
- **Wild oscillations.** Normal! This is Lotka-Volterra. Name it: *"This is a real ecological model. Populations oscillate. The question is: do they oscillate to extinction or to stability?"*

### Key insight
*"Balance isn't a number. It's a relationship between numbers. Change one and you have to feel out the rest."*

---

## Step 6: The Player Enters (~20 min)

**Goal:** A first-person player avatar enters the ecosystem. Creatures react to the player's presence. The player doesn't "control" the ecosystem — they disturb it.

**Concept:** Until now students have been observers watching from the Scene view. Now they step inside. The shift from god-view to ground-level, first-person perspective changes everything about how the ecosystem feels — even if the systems are identical.

### Setup the player

- Add a first-person controller (use Unity's starter asset or a simple capsule + camera + basic movement script)
- Tag the player as **"Player"**
- Place in the ecosystem scene

### Fauna flees the player

- Open Fauna prefab
- On the threat sensor (`ProximitySensor`), add **"Player"** to required tags (so it now detects both Predator and Player)
- That's it. FaunaController already handles fleeing from threats.

### Test
- Walk toward Fauna. They scatter.
- *"You haven't touched anything. You haven't pressed a button. But your presence changed the ecosystem. Fauna fled, stopped eating, lost energy. You are a force in this world."*

### Predator flees the player (optional variation)
- Same technique: add "Player" to Predator's threat sensor
- Now the player's presence pushes predators away, giving Fauna relief
- *"You're a super-predator. Everything runs. What happens to the balance?"*

### Discuss
- *"You're not controlling. You're inhabiting. The question isn't 'what can I do?' — it's 'what does my presence do?'"*
- Connect to Wolves/Rivers: *"The wolves didn't decide to change the rivers. They just existed, and the system reorganized around them."*

---

## Step 7: Creatures Change the World (~15 min)

**Goal:** Creature presence or behavior produces a visible change in the environment — terrain, lighting, vegetation, atmosphere. The ecosystem isn't just *in* the world; it *reshapes* the world.

**Concept:** This is the "wolves change rivers" moment. A simple mechanism where creatures affect their surroundings — not through a menu or UI, but as a side effect of existing. The specifics are flexible; the principle is what matters.

### The idea

Creatures don't just live in the environment — their presence transforms it. This could be:

- **Flora changes the ground** — where plants grow, the terrain color/texture shifts (grass spreads, ground greens)
- **Predator presence changes the atmosphere** — fog thickens, light dims, post-processing shifts where predators roam
- **Fauna trails mark the land** — paths of trampled ground where herds have traveled
- **Player presence blooms the world** — flowers/light/color follows the player, fading behind them
- **Overpopulation degrades** — too many creatures in one area dims/corrupts the environment

### Implementation approach (keep it simple)

This is intentionally open — define the specific effect based on what feels right for the class. Some simple technical approaches:

- **Area-of-effect material change:** A script on creatures that raycasts down and modifies terrain material/color in a radius below them. Lightweight, visual, immediate.
- **Trigger zone + post-processing:** Creatures carry a trigger zone; when enough creatures occupy an area, a local post-processing volume shifts (saturation, fog, color grading).
- **Shader parameter driven by density:** Count creatures in an area, feed that count to a global shader variable that tints the terrain.
- **Particle/VFX trail:** Creatures leave particle trails that accumulate and change the visual character of the ground.

### The teaching point

*"In interactive art, the world isn't a stage. It's a material. Your creatures don't perform on the terrain — they sculpt it."*

*"This is what separates an interactive work from an animation. The world you see at minute 5 is different from minute 1, and it's different because of what lived and died there."*

---

## Homework

### Required
- Complete the three-species ecosystem with visual feedback and spawner-based balance
- Tune until all three coexist for at least 2 minutes
- Add player presence with at least one creature type reacting (flee)

### Stretch
- Replace abstract shapes with authored visuals (plants, animals, environment)
- Add the environmental effect (creatures change the world)
- Add a fourth species or environmental modifier (day/night cycle that changes Flora's EnergyProvider rate? seasonal energy shifts?)
- Experiment with `GazeSensor` — creatures react differently when the player *looks* at them vs. just being near

---

## Session Notes for Instructor

### Pacing
- Steps 1–3 are the mechanical core (~50 min). Move steadily but don't rush Step 2 — it's where the ecosystem concept clicks.
- Step 4 is quick and rewarding (~15 min). Good energy boost mid-session.
- Step 5 is the most important pedagogically (~25 min). Resist the urge to cut it short. This is where students become designers, not assemblers.
- Steps 6–7 are the payoff (~35 min). If time is tight, Step 7 can become homework. Step 6 (player) should stay in class — the perspective shift is powerful when experienced together.

### Common issues to anticipate
- **NavMesh not baked** — if students start fresh, remind them to bake NavMesh Surface
- **Tags not created** — Flora, Fauna, Predator, Player tags must be created in Tag Manager
- **Sensor detecting self** — if a creature's sensor picks up its own collider, add it to a different layer or adjust the layer mask
- **Consumer eating through walls** — consume radius should be small (~1.5–2.5); if issues persist, add a raycast check
- **Everything dies instantly** — usually decay rate too high relative to energy gain. Start with low decay, increase gradually.
- **Nothing dies** — energy gain from Consumer too high, or EnergyProvider too generous. Lower income first.

### Key callbacks to prior lectures
- Lecture 1: Grammar (parts, rules, loops, emergent properties) — this ecosystem is all four
- Lecture 1: Sense > Think > Act loop — now concrete in FaunaController
- Lecture 2: Energy as intermediate variable — now flowing through the whole food chain
- Lecture 2: Exponential growth crash — solved by predation and resource competition

### Forward threads for Lecture 4
- Deeper player interaction (not just presence — actions, tools, influence)
- Narrative/progression layered onto ecosystem (what happens when something goes extinct?)
- Sound and ambient feedback responding to ecosystem state
- The personal project: what kind of world do *you* want to build?
