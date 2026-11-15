# Work that is dull, heavy or dangerous
### Factories and construction

Factories and building sites were the first places robots went to work, and they are still where most robots are. The questions here are practical: what can run with nobody present, what a machine can sense when the lights are off, and how people and heavy equipment can share a site safely.

## Make an ordinary factory task less difficult
**Evidence: company announcement and investment.** Nidus announced $30 million in funding in November 2026 to develop AI-enabled robotics for existing manufacturing workflows, beginning with wire harnesses. Flexible wires are a revealing challenge: they bend, move and do not behave like rigid blocks. [Nidus announcement](https://www.prnewswire.com/news-releases/nidus-raises-30m-to-deploy-embodied-intelligence-in-americas-defense-factories-302934756.html)

**Ask:** Why might a repetitive task still be difficult to automate? What would the robot have to sense instead of assume? Nidus's defense focus also provides a concrete opening for the [dual-use discussion](../discuss/questions-and-shared-standards.md).

A wire harness makes an excellent lesson in the gap between repetition and simplicity. Humans adapt to flexible objects almost without noticing; a robot must sense and manage those variations. Solving an unglamorous task can unlock meaningful industrial value.


## When the lights go out: how does a robot know?

What if a factory could keep working after everyone went home? And if a robot can work without room lights, could it help when a firefighter cannot see? Brad's question connects two very different environments through one powerful idea: a machine does not have to sense the world exactly as we do.

### A real example, not a science-fiction factory

FANUC's case study of KAD Models describes a prototype shop where people prepare and prove machining jobs during the day, then automated cells tend CNC machines overnight. Robots move prepared fixtures through a queue; completed parts await the team in the morning. The linked case study includes a video credited to Trinity Robotics Automation. This is a concrete lights-out production process, not a claim that the whole business operates without people.

Here, lights-out primarily means unattended operation for a period, not proof that every bulb is off. A robot following a well-defined path with parts held in known positions may not need to identify every object visually. A vision-guided process may still use carefully controlled lighting. The interesting question is what preparation, sensing and exception handling let the work continue safely.

**Your move:** List everything a person does in that shop during the day that lets the night shift run alone. Then pick the step you think is hardest to automate and say why. Your answer points at work that is still waiting for someone to do it.

### No room lights does not mean no sensing

An ordinary visible-light camera needs light, which can come from a lamp on the robot rather than the ceiling. Lidar supplies its own laser pulses to measure distance. Radar uses radio waves. Thermal cameras detect infrared radiation rather than requiring visible illumination. Force and contact sensors can add another kind of information: what happens when the machine touches an object. These are complementary tools, not interchangeable superpowers.

SICK's lidar guide explains how returns from particles can differ from returns from solid objects; its radar materials describe detection in rain, fog and dust. Those capabilities invite useful comparisons, but a dark factory is not a burning building. Heat, smoke, water, debris and contaminated sensors change the problem. FLIR's examples show that thermal imaging can reveal scenes obscured by smoke but does not simply look through walls or ordinary window glass. NIST research also found that elevated camera temperature can reduce thermal resolution.

**Your move:** Choose two sensors from this section and design a test that makes them disagree: smoke, steam, a mirror, a hot wall. A robot you would trust in a bad place is one whose designers went looking for that disagreement first.

### From the supermarket aisle to a hazardous room

Brad's supermarket experience makes the everyday version easy to picture: imagine a grocery robot trying to identify a package, judge distance to a shelf and grasp something fragile. A camera might help read the label, a depth sensor locate the object and force feedback help control the grip. That is a design analogy, not a description of one particular store's system. The machine combines evidence because no single measurement answers every question.

Now ask the harder rescue question. Could a robot combine thermal imagery, distance measurements and environmental sensors to help an operator find a person, locate a hazard or decide where not to send a crew? A warm shape is not automatically a person, a clear image does not prove breathable air, and seeing a route does not prove the structure will hold. Useful detection must include uncertainty and a safe response when the evidence is weak.

### A challenge for a curious engineering team

Build a safe tabletop demonstration, not a fire experiment: change the lighting, rearrange objects and compare what different sensors can still tell you. Which failures can another sensor catch? When should the robot stop and ask for help? Then study how professionals test equipment for actual hazardous environments. The breakthrough is not merely seeing in the dark. It is knowing enough to act usefully, and knowing when you do not.

### Easy for people, hard for machines, and the reverse
**Deployed equipment, current research and one long-standing observation**

Taping a shipping box shut is awkward for a person and trivial for a machine. A case sealer does it with belts, guides and a taping head, the same motion repeated without tiring. It is automation, though hardly a robot: it senses little and decides nothing. Ask the same warehouse to pack a mixed order into that box and the picture reverses. Amazon says its touch-sensing robot, Vulcan, can handle about three quarters of the item types it meets and asks a person for help when it is stuck. The roboticist Hans Moravec described the pattern in his 1988 book *Mind Children*: the reasoning people find hard is comparatively easy for a computer, and the perception and movement a one-year-old manages without effort is very hard. [Signode: case sealers](https://www.signode.com/products/case-packaging/case-sealers-box-tapers/) · [Amazon: the Vulcan robot](https://aboutamazon.com/news/operations/amazon-vulcan-robot-pick-stow-touch) · [Amazon researchers' preprint on robotic stowing](https://arxiv.org/abs/2505.04572) · [Ken Goldberg: why don't we have better robots yet?](https://www.ted.com/talks/ken_goldberg_why_don_t_we_have_better_robots_yet)

**Your move:** Sort the jobs on your own robot into two lists: the same motion every time, and something different every time. Which list took most of your season? The second list is where most of the unsolved work in robotics still sits.

### The dark factory, as claimed and as visited
**Company claims and independent reporting**

FANUC says its factories in Japan run long stretches of unmanned machining, with robots helping to build robots. Xiaomi's chief executive has described a phone factory in Beijing where every key process is automated and a phone comes off the line about every three seconds. That account comes from the company, and this collection found no independent visit to the plant. When AFP reporters toured other Chinese factories in 2025, an executive dismissed the phrase "dark factory" as a surface description, and a manager told them, "Many decisions require human judgement." Many dark-factory clips online carry no source at all. [FANUC: its factories](https://fanuc.co.jp/en/profile/production) · [New Atlas: Xiaomi's factory, from company statements](https://newatlas.com/robotics/xiaomi-dark-robotic-factory/) · [AFP: inside China's automating factories](https://www.thejakartapost.com/business/2025/12/14/chinas-smaller-manufacturers-look-to-catch-the-automation-wave)

**Your move:** A company's video and a reporter's visit are different kinds of evidence. For any impressive factory clip, ask who filmed it, who chose what to show, and what a person on site has to do when something jams. Then look for the people in the frame.

### Watch and explore

- [FANUC: KAD Models lights-out machining, with video](https://www.fanucamerica.com/case-studies/high-mix-low-volume-prototype-shop-achieves-lights-out-manufacturing-with-robotic-automation)
  - Watch the robot tend machining equipment, then look for the human preparation that makes unattended production possible.
- [SICK: how lidar measures distance](https://sickag.github.io/sick_lidar_developer_guide/lidar-basics/)
  - Diagrams explain laser pulses and multiple echoes. Darkness and airborne particles are different engineering problems.
- [SICK: radar in harsh environments](https://www.sick.com/au/en/rms2000-2d-radar-sensor-reliably-detect-objects-and-movements-in-a-harsh-operating-environment/w/press-2024-rms2000)
  - A manufacturer example of sensing beyond visible light. Compare the intended environment with a fire scene rather than assuming they are equivalent.
- [FLIR: what thermal imaging can and cannot see through](https://www.flir.com/discover/home-outdoor/can-thermal-imaging-see-through-walls/)
  - Visual comparisons show why smoke, glass and walls do not present the same challenge to thermal and ordinary cameras.
- [NIST: testing thermal cameras for first responders](https://www.nist.gov/publications/first-responder-thermal-imaging-cameras-development-performance-metrics-and-test)
  - Research shows why the camera's own operating temperature matters, not just the heat in its picture.

## Construction: precision without a humanoid

### Mortenson and autonomous heavy equipment
**Use on selected renewable-energy projects**

**Mortenson** is a Minneapolis-based builder that began in 1954 as a small family-owned company and now works across the country on stadiums and arenas, hospitals, data centers, and wind and solar projects. [About Mortenson](https://www.mortenson.com/about)

The company describes its partnership with **Built Robotics** to use autonomous heavy equipment on selected renewable-energy projects. The machine does not need to imitate a person. It needs to perform a defined construction task reliably within a larger worksite operation. [Mortenson partnership](https://www.mortenson.com/industries/civil/built-robotics-partnership)

**Ask:** Which repetitive tasks are suitable for automation? How are work areas controlled, exceptions handled and responsibilities divided between people and machines? A productive machine is only useful if the whole site can work safely around it.

### Turning a model into marks on a floor
**Supplier-documented construction use**

Dusty Robotics describes Mortenson using robotic layout on two data-center projects. The task translates digital building information into physical layout that different trades can use. This is a bridge between software and the built world, rather than a robot that builds a building by itself. [Dusty: Mortenson case study](https://www.dustyrobotics.com/customers/mortenson)

**Try:** Draw a room plan, then ask how a robot would establish its position and transfer that plan onto the real floor. What happens when the floor is obstructed or the digital plan changes? The most valuable innovation may be reducing rework and coordination mistakes.
