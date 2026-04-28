# Course References — Interactive Art, Installations & Art Games

> Curated reference list for **Multimedia Design 4: Interaction Design for Artists**
> Organized by the course's 7 interaction areas, plus cross-cutting works and "agency as art" exemplars.

---

## 1. CORE OBJECT MANIPULATION
*Transforms, spawning, resetting state*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **Wooden Mirror** | Daniel Rozin | 1999 | Stand in front of 830 motorized wooden tiles — each rotates to reflect your image as a low-res wooden portrait. Step away and all tiles reset to neutral. |
| **Drawing Operations** | Sougwen Chung | 2015+ | Draw collaboratively with a robotic arm that mirrors, transforms, and diverges from your strokes. Your marks are duplicated and mutated in real time. |
| **Reactive Table** | teamLab | 2014+ | Place objects or touch a digital surface — flowers, water, creatures spawn, bloom, and react to object position. Moving objects transforms the digital ecosystem. |
| **Rain Room** | Random International | 2012 | Walk through falling rain. Sensors track your body and stop rain above you — your position "deletes" water in your local area. |
| **Articulated Cloud** | Ned Kahn | 2004 | Thousands of hinged aluminum panels on a facade move in wind. Simple per-object rotation creates emergent wave patterns. |
| **Text Rain** | Camille Utterback & Romy Achituv | 1999 | Letters from a poem fall on-screen like rain. Your body silhouette catches, holds, and plays with falling letters — reading becomes a physical act. |

**Unity mapping:** Transform, Instantiate/Destroy, OnTriggerEnter, proximity detection, physics materials

---

## 2. UI-BASED INTERACTION
*Menus, simulated inputs, cross-platform input design*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **Please Empty Your Pockets** | Rafael Lozano-Hemmer | 2010 | Place personal objects on a conveyor scanner (like airport security). The system photographs, archives, and displays them alongside thousands of past visitors' objects. The familiar institutional interface IS the art. |
| **Listening Post** | Mark Hansen & Ben Rubin | 2001 | 231 small screens display text fragments harvested live from internet chatrooms. A read-only data dashboard as emotional portrait of collective speech. |
| **Pong Mechanik** | Niklas Roy | 2010 | Play Pong with comically over-engineered physical hand-cranks, motors, and pulleys. The absurd interface makes the point: how you receive input changes everything. |
| **Bientot** | Samuel Bianchini | 2007 | Gallery visitors send SMS votes from their phones — results update live on a large LED display. Cross-platform input: personal device to public screen. |
| **Her Story** | Sam Barlow | 2015 | Search a police database by typing keywords. The "game" is a search interface — you piece together a murder mystery through database queries. The UI IS the mechanic. |

**Unity mapping:** UI Canvas, TextMeshPro, Input System, cross-device networking, simulated interfaces

---

## 3. CHARACTER CONTROL
*First-person movement, walkability*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **Dear Esther** | The Chinese Room | 2012 | Walk through a Hebridean island. No combat, no puzzles, no fail state. Just WASD + mouse-look. Letter fragments narrate as you move. Movement through space IS the interaction. |
| **Osmose** | Char Davies | 1995 | Wear a VR headset and breath-tracking vest. Breathe in to float up, breathe out to sink. Lean to move laterally. Your respiratory system IS the controller. |
| **Everything** | David OReilly | 2017 | Be any object in the universe — atom to galaxy, bear to blade of grass. Movement changes completely depending on what you are. Scale, speed, and physics define subjective experience. |
| **Walden, a game** | Tracy Fullerton / USC | 2017 | Live as Thoreau at Walden Pond. Walk slowly and attentively — the world is colorful. Rush and the world grays out. Movement speed IS the artistic statement. |
| **Journey** | thatgamecompany | 2012 | Walk through a desert toward a mountain. A wordless anonymous stranger may join you — you can only chirp. The constraints on movement and communication ARE the design. |
| **Flower** | thatgamecompany | 2009 | Control the wind with gyroscope tilt, guiding petals across landscapes. Pass over flowers to bloom them and transform the world from gray to vibrant. The character IS an invisible force. |
| **In the Eyes of the Animal** | Marshmallow Laser Feast | 2015 | VR in a forest: experience the woodland as a dragonfly, owl, or frog. Each creature has different movement, scale, speed, and sensory perception. |
| **Proteus** | Ed Key & David Kanaga | 2013 | Explore a procedurally generated island. No objectives. Walking near objects triggers musical sounds — the landscape is a musical instrument played by walking. |
| **The Unfinished Swan** | Giant Sparrow | 2012 | Throw black paint into a completely white void to reveal geometry. Later chapters: throw water to grow vines, throw light to banish darkness. The same verb (throw) produces completely different spatial experiences. |
| **Manifold Garden** | William Chyr | 2019 | Navigate impossible Escher-like architecture by rotating gravity — walk on any surface. Spatial perception IS the challenge. What looks like a gap in 2D is a bridge in 3D. |
| **Firewatch** | Campo Santo | 2016 | Navigate Wyoming wilderness using a real map and compass (no minimap). Choose dialogue over a walkie-talkie with someone you never see. Spatial awareness and remote voice as paired mechanics. |
| **Sable** | Shedworks | 2021 | Ride a hoverbike across open desert, climb structures, glide with a cloak. No combat — exploration, climbing, and cultural discovery. Movement systems (hover, climb, glide) create different emotional textures. |
| **Neva** | Replika Studios | 2024 | Run and fight alongside a wolf companion whose size and behavior change over the game. The relationship shifts from protector to protected — expressed through movement mechanics, not cutscenes. |
| **Celeste** | Extremely OK Games | 2018 | Precision platforming — dashing, climbing, wall-jumping — up a mountain. The difficulty IS the narrative: the mountain-as-depression metaphor only works because climbing is genuinely hard. |

**Unity mapping:** CharacterController, first-person camera rig, custom input axes, movement-speed-to-feedback coupling

---

## 4. PHYSICS INTERACTIONS
*Forces, collisions, constraints*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **Tumble Room** | William Forsythe | 2002 | Walk through hundreds of suspended white balloons. Your body displaces them — they drift, collide, settle. You are a force acting on a field of lightweight physics objects. |
| **Swarm Study** | Random International | 2010+ | Hundreds of illuminated elements flock like birds — attracted to, repelled by, or orbiting around your body. Flocking algorithms as aesthetic physics. |
| **Line Wobbler** | Robin Baumgarten | 2015 | A 1D dungeon crawler on an LED strip. The controller is a door-stopper spring — wobble it to move. The spring's physical oscillation and damping ARE the input. |
| **Particle Falls** | Andrea Polli | 2010 | A building-scale projection of particles falling like a waterfall, driven by real-time air quality data. Gesture to "blow" particles. Physics simulation as data visualization. |
| **Cradle** | Semiconductor | 2012 | Stand inside a sphere of speakers. CERN particle physics data is translated into vibrations you feel on your body. Invisible forces made perceptible. |
| **Noby Noby Boy** | Keita Takahashi | 2009 | Stretch, eat, and ragdoll as an absurd worm-creature. Pure physics-toy interaction — no goals, just the pleasure of elastic, bouncy, floppy object behavior. |
| **Katamari Damacy** | Keita Takahashi | 2004 | Roll a sticky ball that picks up everything it touches, growing from paperclips to buildings to continents. The deliberately clumsy twin-stick controls create physical comedy. Scale progression through a single unchanging mechanic. |
| **Getting Over It** | Bennett Foddy | 2017 | Climb an impossible mountain using only a sledgehammer. One wrong move sends you tumbling to the start. The physics ARE the philosophy — frustration and persistence as designed experience. |
| **Octodad: Dadliest Catch** | Young Horses | 2014 | Control an octopus disguised as a human dad using terrible ragdoll physics. The gap between intention and execution IS the game — a physical metaphor for impostor syndrome made interactive. |
| **World of Goo** | 2D Boy | 2008 | Drag and connect goo balls to build wobbly bridges and towers. The physics feel — wobble, flex, collapse — is the core pleasure. Construction-as-puzzle where tactile satisfaction drives everything. |
| **Donut County** | Ben Esposito | 2018 | Control a hole in the ground that grows as it swallows objects. Move the hole under things to consume them — starting small, growing to swallow buildings. Subtraction instead of addition. |

**Unity mapping:** Rigidbody, AddForce, Physics Materials, SpringJoint, flocking algorithms, particle systems

---

## 5. NPC / NARRATIVE INTERACTION
*Characters, dialogue, behavioral responses*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **Facade** | Mateas & Stern | 2005 | Visit a couple for drinks. Type natural language to navigate their crumbling marriage. NPCs respond emotionally, argue, and can throw you out. |
| **Kentucky Route Zero** | Cardboard Computer | 2013–2020 | Choose dialogue options — but choices don't branch the plot, they define who the characters ARE. Dialogue as identity construction. |
| **Papers, Please** | Lucas Pope | 2013 | Operate a border checkpoint. Examine documents, stamp APPROVED or DENIED. Balance survival against morality. The bureaucratic interface generates moral weight. |
| **Florence** | Mountains / Annapurna | 2018 | Interact through micro-mechanics: piece together speech bubbles to form conversation, brush teeth together, unpack boxes. Each relationship moment is a unique small interaction. |
| **Baba Yaga** | Baobab Studios | 2020 | VR encounter with a sentient forest. Trees and creatures respond to your gaze and hands — the forest NPCs shift between welcoming and threatening based on behavior. "NPC" = the environment itself. |
| **Do Not Touch** | Studio Moniker | 2013 | An interactive video asks you NOT to touch things. Your cursor is recorded. You see the aggregated behavior of thousands of past viewers. The "NPC" is the ghost of the crowd. |
| **The Stanley Parable** | Galactic Cafe | 2013 | Walk through an office. A narrator tells you what to do. Obey or disobey — every choice leads to endings that comment on the nature of choice itself. |
| **Eliza** | Zachtronics | 2019 | Work as a human proxy for an AI therapy chatbot. Read scripted lines to patients, or go off-script. The tension between scripted NPC dialogue and human judgment IS the experience. |
| **Disco Elysium** | ZA/UM | 2019 | Your own psyche is split into 24 competing "skills" that interject during conversations. The most important "NPCs" are parts of your own mind. Internal conflict as dialogue system. |
| **Oxenfree** | Night School Studio | 2016 | Walk with teens while real-time speech bubbles offer dialogue choices. Characters talk over each other — you can interrupt, stay silent, or miss your window. Timing transforms dialogue. |
| **Event[0]** | Ocelot Society | 2016 | Type natural language into terminals to communicate with Kaizen, an AI space station. Negotiate, persuade, or manipulate — Kaizen remembers everything and holds grudges. |
| **Unpacking** | Witch Beam | 2021 | Unpack boxes and place belongings into rooms across life stages. You infer an entire life story from objects and where you put them. Object placement as wordless storytelling. |
| **Immortality** | Sam Barlow / Half Mermaid | 2022 | Scrub through film footage, clicking on objects/actors within frames to match-cut to related footage. Navigate a vast film archive through visual association — thinking in images, not words. |
| **Signs of the Sojourner** | Echodog Games | 2020 | Have conversations by playing cards with matching edge-symbols. Your deck changes over time, representing how travel changes your communication style. Dialogue abstracted into pattern-matching. |

**Unity mapping:** Dialogue systems (Ink, Yarn Spinner), behavior trees, emotional state machines, NPC memory/relationship tracking

---

## 6. ENVIRONMENT MANIPULATION
*Light, weather, ambiance, world-state changes*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **The Weather Project** | Olafur Eliasson | 2003 | An artificial sun and mist fill Tate Modern's Turbine Hall. Visitors lie on the floor, see themselves in a mirrored ceiling. Light, fog, and color temperature as emotional architecture. |
| **Pulse Room** | Rafael Lozano-Hemmer | 2006 | Grip a heart-rate sensor. Your heartbeat becomes a flashing lightbulb that joins 300 others — each pulsing with a past visitor's recorded heartbeat. You literally change the room's light. |
| **Horizon** | United Visual Artists (UVA) | 2019 | Move through a dark space with horizontal light lines. Your path shifts the lines — a flat plain becomes a storm, a sunset, a mountain range. Minimal elements, vast world-state changes. |
| **Night Walk with Brilliant Lanterns** | Moment Factory | Various | Walk an outdoor nighttime path. Stepping on areas triggers light blooms, fog, animal sounds, ambient music shifts. The forest "reacts" to walkers. |
| **Submergence** | Squidsoup | 2014+ | Walk through thousands of suspended LED lights that respond to movement, creating an ocean-like immersive environment. A forest of light that reacts to your passage. |
| **Symbiotic Seeing** | Olafur Eliasson | 2020+ | Enter a room of dense fog with a single light source. Your shadow mingles with strangers' shadows. Individual and collective identity blur through atmospheric manipulation. |
| **Seasons / From Here to Ear** | Celeste Boursier-Mougenot | 2010s | Live finches play electric guitars by landing on strings. The sonic environment is shaped by birds' behavior. The "user" is non-human. |
| **Gris** | Nomada Studio | 2018 | Run through a watercolor world drained of color. As you progress, colors return (red, green, blue), each unlocking new abilities and transforming the landscape. Color-as-emotion, environment-as-inner-state. |
| **Okami** | Clover Studio | 2006 | Pause to paint brushstrokes on a canvas overlay — circles create bombs, slashes cut, lines make wind. The world transforms from cursed wasteland to lush color as you restore areas. Player-as-artist literalized. |
| **Chicory: A Colorful Tale** | Greg Lobanov / Finji | 2021 | Wield a giant paintbrush to paint the entire game world — every surface, NPC, object. Your paint stays permanently. Environmental transformation as personal expression. |
| **Outer Wilds** | Mobius Digital | 2019 | Explore a solar system in a 22-minute time loop. Planets actively change (sand flows, a planet collapses into a black hole). The only thing that persists is what you KNOW. Knowledge as the only form of progress. |
| **Cloud Gardens** | Noio | 2021 | Place junk objects in abandoned dioramas, then grow plants on them. Balance decay and growth, creating overgrown post-human landscapes. Construction-as-gardening. |

**Unity mapping:** Light.intensity, fog volumes, skybox, ambient audio, trigger volumes, world-state variables, Audio Mixer snapshots

---

## 7. SENSORY FEEDBACK
*Sound cues, visual effects, haptics tied to player actions*

| Project | Artist / Studio | Year | What the participant DOES |
|---------|----------------|------|--------------------------|
| **Messa di Voce** | Golan Levin & Zachary Lieberman | 2003 | Vocalize into microphones — your voice is visualized as graphic forms in real time. Whispers produce delicate lines, shouts produce explosions. You "play" the visuals like an instrument. |
| **The Treachery of Sanctuary** | Chris Milk | 2012 | Three panels respond to your silhouette. Panel 1: shadow dissolves into birds. Panel 2: birds attack you. Panel 3: your arms become wings — flap and fly. Feedback escalation across three stages. |
| **Sonic Runway** | Rob Jensen & Warren Trezevant | 2016 | A 100m corridor of LED arches. Clap or shout — your sound becomes rings of light traveling at the speed of sound. Voice made visible. |
| **Future You / BEING** | Universal Everything | 2023+ | A camera captures your body. An avatar of evolving abstract materials (smoke, crystals, fire, liquid) mirrors your movements on a large screen. You become a unique digital creature. |
| **Scramble Suit** | Harvey Moon & Kyle McDonald | 2013 | Your face on a screen, but face-tracking swaps your features with fragments from other faces. Every micro-expression produces uncanny, identity-destabilizing visual feedback. |
| **Body Paint** | Memo Akten & Davide Quayola | 2013+ | Dance in front of a screen. Your movements generate real-time abstract paintings — your body becomes a brush. |
| **Tele-Present Wind** | David Bowen | 2011 | A rooftop wind sensor drives an array of thin stalks inside a gallery. Remote weather translated into immediate kinetic and auditory feedback. 1:1 data-to-motion mapping. |
| **Rez / Rez Infinite** | Tetsuya Mizuguchi / Enhance | 2001/2016 | Shoot targets in a wireframe world — every hit triggers musical notes and visual pulses. Your gameplay literally composes the soundtrack. Synesthesia as core mechanic. |
| **Tetris Effect** | Tetsuya Mizuguchi / Enhance | 2018 | Play Tetris while every rotation, drop, and line-clear triggers musical and visual responses. Backgrounds pulse and evolve based on performance. Familiar mechanics, transcendent feedback. |
| **Thumper** | Drool | 2016 | Guide a chrome beetle down a track at extreme speed, pressing in time with music to survive. The audiovisual assault is terrifying — synesthetic feedback as dread, not joy. |
| **Panoramical** | Fernando Ramallo & David Kanaga | 2015 | Adjust sliders that simultaneously control a 3D landscape's geometry, color, weather, AND music. You are DJ, landscape architect, and painter at once. The most literal "agency as art" game. |
| **KIDS** | Michael Frei & Mario von Rickenbach | 2019 | Click and drag to influence crowds of simple humanoid figures — pushing them into holes, making them clap, separating individuals. Minimal interaction, powerful social metaphors about conformity and exclusion. |
| **Sayonara Wild Hearts** | Simogo | 2019 | Race through pop-music-video levels on motorcycles and in mech suits, dodging and collecting in time with synth-pop. Each level's mechanics serve the song's rhythm. A pop album as a game. |
| **140** | Jeppe Carlsen | 2013 | Minimalist platformer where everything pulses in sync with electronic music. Platforms, obstacles, and your shape transform on the beat. Zero visual ornamentation — everything communicates timing. |

**Unity mapping:** AudioSource.GetSpectrumData, FFT analysis, particle systems, shader parameters, haptic feedback, real-time motion capture

---

## CROSS-CUTTING WORKS
*Projects spanning multiple interaction areas — especially rich teaching references*

| Project | Artist / Studio | Year | Areas | Key insight |
|---------|----------------|------|-------|-------------|
| **Journey** | thatgamecompany | 2012 | 3, 5, 6, 7 | Wordless multiplayer with a stranger. What you CAN'T do matters as much as what you can. |
| **Flower** | thatgamecompany | 2009 | 3, 4, 6, 7 | Character = invisible wind. Physics, environment, and feedback unified. |
| **teamLab Borderless** | teamLab | 2018/2024 | 1, 6, 7 | 10,000sqm of overlapping responsive systems. No fixed exhibitions — works flow between rooms. |
| **Shadow Monsters** | Philip Worthington | 2004 | 1, 5, 7 | Hand shadows get augmented with digital teeth, eyes, fur. Your body is the object, the monster is the NPC, the augmentation is the feedback. |
| **Passage** | Jason Rohrer | 2007 | 3, 5, 6 | A 5-minute game about a life. Walk left to right, maybe take a companion (who makes you wider and slower). Age, die. 100x16 pixels, total emotional devastation. |
| **We Live in an Ocean of Air** | Marshmallow Laser Feast | 2019+ | 3, 6, 7 | Shared VR — see a giant sequoia, watch your own breath visualized as particles absorbed by the tree. Multiple visitors see each other's breath. |
| **Evolver** | Marshmallow Laser Feast | 2023 | 3, 6, 7 | VR mapped to your heartbeat, breathing, and body heat. Journey through your own body — blood cells to neural pathways. Biometric data as navigation. |
| **Learning to See** | Memo Akten | 2017+ | 1, 7 | Camera captures objects/your body; a neural network "hallucinates" them as ocean waves, fire, flowers in real time. AI pareidolia as creative act. |

---

## "AGENCY AS ART" EXEMPLARS
*Works that pass the Nouliness test — meaning is produced THROUGH the participant's action, not delivered on top of it*

| Project | Artist / Studio | Year | Why it passes the test |
|---------|----------------|------|----------------------|
| **September 12th** | Gonzalo Frasca / Newsgaming | 2003 | Fire missiles at terrorists — but every explosion creates more terrorists from mourning civilians. The only way to win is to stop playing. The political argument IS the interaction. |
| **Papers, Please** | Lucas Pope | 2013 | Stamping DENIED on a refugee's passport while your child is sick at home produces moral weight that cannot exist without the player's hand on the stamp. |
| **The Stanley Parable** | Galactic Cafe | 2013 | A video of someone else playing is a fundamentally different work than playing it yourself. The meaning IS the experience of choosing. |
| **Boundary Functions** | Scott Snibbe | 1998 | Voronoi diagram of personal space — only works when 2+ people are in the room. Literally impossible to experience alone. Social geometry as content. |
| **Rain Room** | Random International | 2012 | The wonder can only exist when a body is present in the rain. No body, no art. |
| **Osmose** | Char Davies | 1995 | Breathing as navigation redefines "being in a space." Cannot be watched — must be breathed. |
| **Braid** | Jonathan Blow | 2008 | Time manipulation as metaphor for regret. The final level's revelation only works because YOU spent hours rewinding time. The twist is about your own behavior. |
| **Spec Ops: The Line** | Yager Development | 2012 | A military shooter that slowly indicts the player for choosing to keep playing. The horror is not what happens — it's that you chose to make it happen. |
| **Before Your Eyes** | GoodbyeWorld Games | 2021 | Relive a life's memories — but every blink (detected by webcam) advances the scene. You try to keep your eyes open to stay in happy moments, but your body inevitably betrays you. Biometric input as loss. |
| **That Dragon, Cancer** | Numinous Games | 2016 | Hold a crying baby who won't be soothed. Sit in a hospital room. Control is gradually taken away. The removal of agency IS the empathy mechanism — powerlessness as meaning. |
| **Baba Is You** | Hempuli (Arvi Teikari) | 2019 | Push word-blocks to rewrite the game's rules. "BABA IS YOU" → push "ROCK IS YOU" and now you control the rock. The rules are physical objects you manipulate. The most literal "player changes the system." |
| **Gorogoa** | Jason Roberts | 2017 | Manipulate a 2x2 grid of illustrated panels — zoom, overlay, split, recombine images to find hidden visual connections between scenes. Panel manipulation as visual storytelling that could not exist non-interactively. |
| **The Beginner's Guide** | Davey Wreden | 2015 | Walk through someone else's unfinished game levels while an unreliable narrator interprets them. You realize the interpretation may be invasive. A game about interpreting games — authorship and agency in question. |
| **Dys4ia** | Anna Anthropy | 2012 | Play abstract mini-games representing gender transition — fit a shape through a too-small gap, shield against words, navigate bureaucracy. Each lasts seconds. Autobiographical experience as interactive metaphor. |
| **Cart Life** | Richard Hofmeier | 2011 | Operate a street vendor cart — manage inventory, make change, serve customers under time pressure while navigating poverty. The business-sim grind IS the empathy engine. IGF Nuovo Award winner. |
| **Plug & Play** | Etter Studio | 2015 | Plug plug-shaped figures into socket-shaped figures, toggle switches, participate in absurdist vignettes. Minimal interaction, maximum implication — simultaneously mechanical, sexual, existential. |
| **The Graveyard** | Tale of Tales | 2008 | Walk an elderly woman slowly to a bench in a graveyard. She sits. A song plays. She walks back (or dies). Five minutes. The slowness and fragility ARE the content. |

---

## RECENT & CURRENT WORKS (2023–2026)

| Project | Artist / Studio | Year | Venue | What happens |
|---------|----------------|------|-------|-------------|
| **Unsupervised** | Refik Anadol | 2022–23 | MoMA, NYC | AI trained on MoMA's 130K artworks generates never-repeating compositions on a massive LED wall. Environmental data modulates output. |
| **Large Nature Model** | Refik Anadol | 2024 | Touring / RAMA | AI trained on planetary ecological datasets generates real-time environments. Environmental sensors modulate the "dreams." |
| **teamLab Borderless (reopened)** | teamLab | 2024 | Azabudai Hills, Tokyo | Entirely new works in new architecture. Touch, proximity, full-body navigation. |
| **Evolver** | Marshmallow Laser Feast | 2023–24 | Saatchi Gallery, London | VR + biometric sensors. Journey through your own body using your heartbeat and breath as input. |
| **Holly+** | Holly Herndon & Mat Dryhurst | 2024 | transmediale, Berlin | Upload your voice → AI re-sings it as Holly Herndon. Voice identity, consent, and AI authorship. |
| **Future You / BEING** | Universal Everything | 2023–24 | Touring | Camera captures you → abstract material avatar mirrors your movements in real time. |
| **Swarm Study XV** | Random International | 2024 | Various | Robotic light swarm on wall responds to viewer proximity. Emergence from simple rules. |
| **data-verse 3** | Ryoji Ikeda | 2023–24 | 180 The Strand, London | Lie on the floor in cascading data projections. Scientific datasets as overwhelming audiovisual immersion. |
| **Learning to See** | Memo Akten | 2023–24 | Various | Camera + neural network hallucinate your reality as oceans, fire, flowers. Live AI re-interpretation. |
| **Submergence** | Squidsoup | 2023–24 | Amos Rex, Helsinki + touring | Walk through thousands of suspended LEDs that respond to movement. |
| **Franchise Freedom** | Studio Drift | 2023–24 | Outdoor venues | Hundreds of autonomous drones mimic starling murmurations. Audience sound modulates swarm behavior. |
| **The Infinite Conversation** | Giacomo Miceli | 2023 | Online / festivals | AI generates an endless conversation between Werner Herzog and Slavoj Žižek. Visitors can steer topics. |

---

## REFERENCE ARTISTS & STUDIOS — Quick Index

| Name | Known for | Key works for this course |
|------|-----------|--------------------------|
| **teamLab** | Immersive digital environments, touch/proximity response | Borderless, Reactive Table |
| **Random International** | Responsive physical installations | Rain Room, Swarm Study |
| **Rafael Lozano-Hemmer** | Biometric and participatory installations | Pulse Room, Please Empty Your Pockets |
| **Olafur Eliasson** | Light, perception, atmospheric manipulation | The Weather Project, Symbiotic Seeing |
| **United Visual Artists (UVA)** | Light-based spatial installations | Horizon |
| **Marshmallow Laser Feast** | Multisensory VR, ecological immersion | Evolver, We Live in an Ocean of Air, In the Eyes of the Animal |
| **Universal Everything** | Real-time generative avatars | Future You, BEING |
| **Moment Factory** | Large-scale environment transformation | Night Walk series |
| **thatgamecompany** | Emotional games with minimal mechanics | Journey, Flower |
| **Golan Levin** | Audio-visual feedback, computational art | Messa di Voce |
| **Daniel Rozin** | Mechanical mirrors and responsive surfaces | Wooden Mirror |
| **Sougwen Chung** | Human-robot collaborative drawing | Drawing Operations |
| **Memo Akten** | AI perception, neural network art | Learning to See, Deep Meditations |
| **Refik Anadol** | AI-generated immersive data sculptures | Unsupervised, Large Nature Model |
| **Chris Milk** | Silhouette-based interactive narratives | The Treachery of Sanctuary |
| **Lucas Pope** | Meaningful bureaucratic mechanics | Papers, Please, Return of the Obra Dinn |
| **Cardboard Computer** | Dialogue as identity construction | Kentucky Route Zero |
| **David OReilly** | Non-anthropocentric simulation | Everything |
| **Char Davies** | Breath-based VR navigation | Osmose |
| **Gonzalo Frasca** | Procedural rhetoric, political games | September 12th |
| **Scott Snibbe** | Social/spatial interactive installations | Boundary Functions |
| **Holly Herndon** | AI voice, consent, and collaborative music | Holly+ |
| **Ryoji Ikeda** | Data as audiovisual material | data-verse, test pattern |

---

## UNITY SYSTEMS → REFERENCE PROJECTS

For teaching: which projects best demonstrate each Unity system?

| Unity System | Best reference projects |
|---|---|
| **Transform / Instantiate / Destroy** | Wooden Mirror, Drawing Operations, Reactive Table, Text Rain |
| **UI Canvas / TextMeshPro** | Listening Post, Please Empty Your Pockets, Her Story |
| **CharacterController / Camera** | Dear Esther, Everything, Osmose, Walden, Journey |
| **Rigidbody / Physics Materials** | Tumble Room, Swarm Study, Line Wobbler, Noby Noby Boy |
| **Dialogue (Ink / Yarn Spinner)** | Kentucky Route Zero, Facade, Eliza, Florence |
| **Lighting / Fog / Skybox / Post-processing** | Pulse Room, Horizon, Weather Project, Night Walk |
| **AudioSource / Particles / VFX Graph** | Messa di Voce, Sonic Runway, Treachery of Sanctuary, Rez |
| **Input System (custom controllers)** | Osmose, Line Wobbler, Pong Mechanik |
| **Trigger Volumes / Colliders** | Rain Room, Night Walk, Submergence |

---

## KEY GAME DESIGNERS & STUDIOS — Quick Index

| Name | Known for | Key works for this course |
|------|-----------|--------------------------|
| **Keita Takahashi** | Absurd physics joy, anti-design | Katamari Damacy, Noby Noby Boy, Wattam |
| **Jenova Chen / thatgamecompany** | Emotional minimalism, wordless multiplayer | Journey, Flower, Flow |
| **Sam Barlow** | Interface-as-narrative | Her Story, Immortality |
| **Bennett Foddy** | Frustration as philosophy | Getting Over It |
| **Jonathan Blow** | Agency as epistemology | Braid, The Witness |
| **Davey Wreden** | Meta-commentary on player agency | The Stanley Parable, The Beginner's Guide |
| **Tale of Tales** | "Games don't need to be fun" | The Graveyard, Sunset |
| **Molleindustria (Paolo Pedercini)** | Political games, procedural rhetoric | September 12th (Frasca), Phone Story, Unmanned |
| **Pippin Barr** | Games about games, performance of play | The Artist Is Present, It is as if you were doing work, v r series |
| **Robert Yang** | Bodies, intimacy, consent as mechanics | Hurt Me Plenty, Rinse and Repeat |
| **Nina Freeman** | Autobiographical digital intimacy | Cibele, Lost Memories Dot Net |
| **Anna Anthropy** | Personal experience as abstract interaction | Dys4ia |
| **Die Gute Fabrik** | Gentle interaction, social/nurture mechanics | Mutazione, Johann Sebastian Joust |
| **Tetsuya Mizuguchi / Enhance** | Synesthesia, audio-visual fusion | Rez, Tetris Effect |
| **David OReilly** | Non-anthropocentric simulation | Everything, Mountain |
| **Jason Roberts** | Visual logic, panel manipulation | Gorogoa |
| **Arvi Teikari (Hempuli)** | Rules as physical objects | Baba Is You |
| **Simogo** | Pop-music-as-game | Sayonara Wild Hearts, Device 6 |
| **Michael Frei & Mario von Rickenbach** | Minimal interaction, maximum implication | Plug & Play, KIDS |

---

## FIVE PRINCIPLES FROM THE REFERENCES

Patterns that emerge across the strongest works in this list:

**1. The verb IS the meaning.**
In Papers Please, Florence, Getting Over It, and Dys4ia, the interaction mechanic is inseparable from the theme. You cannot describe what these works "mean" without describing what the participant *does*.

**2. Constraint creates expression.**
Dear Esther removes all verbs except walk. Before Your Eyes uses involuntary blinking. That Dragon Cancer takes control away. Journey forbids speech. Reduction of agency can be as meaningful as expansion.

**3. Feel is content.**
The sand-sliding of Journey, the clumsy rolling of Katamari, the wobble of World of Goo — "game feel" is not surface polish. It IS the medium. The emotional register of a work is determined by how interaction feels, not what it achieves.

**4. Interfaces carry ideology.**
Papers Please's desk, Her Story's search bar, Phone Story's touchscreen — the interface itself is a statement about how we relate to systems, labor, and each other.

**5. The irreducibility test.**
If you could watch someone else and get the same experience, the agency isn't doing work. The works on this list produce meaning that requires the participant's choices, timing, physical gestures, and attention.

---

*Last updated: February 2026. Sources: Ars Electronica archives, MoMA exhibitions, Barbican digital programme, IndieCade/IGF/A MAZE selections, transmediale, SIGGRAPH Art Gallery, artist studio documentation.*
