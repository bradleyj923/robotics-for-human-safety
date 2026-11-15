# Different environments. The same engineering questions.
### Space and connected care

A construction robot and a robot approaching an icy crevasse seem worlds apart. Both need to understand where they are, cope with an imperfect environment and do something useful without causing harm. Looking across fields can reveal a solution already taking shape somewhere else.

## Space: where people cannot easily go

### A snake-inspired explorer
**Research and development**

NASA JPL's **EELS**, the Exobiology Extant Life Surveyor, takes inspiration from a snake. Its prototypes combine sensing with screw-like propulsion to explore difficult terrain. The vision includes investigating openings in icy worlds, while the engineering starts with tests here on Earth. It is a development project, not a launched mission. [JPL EELS project](https://www.jpl.nasa.gov/robotics-at-jpl/eels/) · [Watch EELS testing](https://www.jpl.nasa.gov/videos/testing-out-jpls-new-snake-robot/)

**Ask:** What body shape lets a machine enter a place people cannot? When would a flexible, segmented body be more useful than wheels or legs? Could the same idea help inspect a confined space on Earth?

### An asteroid sample, brought home
**Completed sample-return achievement**

NASA's **OSIRIS-REx** returned material from asteroid Bennu to Earth on September 24, 2023. That is a concrete example of a robotic spacecraft doing difficult physical work far from its operators: reaching a target, collecting a sample and delivering it for study. [NASA OSIRIS-REx mission](https://science.nasa.gov/mission/osiris-rex/)

What has to happen onboard when instructions cannot arrive instantly? What should be simulated before departure? What information must a machine send back so people can decide the next step?

### A rocket that was caught, and one that chose not to try
**Test flight**

On November 13, 2026, SpaceX launched its fifteenth Starship test flight and tried to bring both stages back to the two mechanical arms on the launch tower. The upper stage flew 14 orbits and was caught the next day, the first time a vehicle returning from orbit has been caught this way. The booster was not. Its own guidance software judged that it was out of position, called off the attempt without waiting for a person, and steered offshore, where it was lost. The first booster catch came in October 2024. [Spaceflight Now: the launch and the booster's abort](https://spaceflightnow.com/2026/11/13/live-coverage-starship-flight-15-attempts-to-recover-full-vehicle-in-double-launch-pad-catch/) · [CNBC: the upper-stage catch](https://www.cnbc.com/2026/11/14/spacex-plans-to-try-first-ever-catch-of-starship-rocket-from-orbit.html) · [SpaceX: the first booster catch, 2024](https://www.spacex.com/launches/starship-flight-5)

Engineers who do this work usually call it autonomous control, not robotics. A SpaceX landing engineer has explained why the vehicle has to decide alone: the path must be recomputed on board in a fraction of a second, and the first attempt has to work. His paper is about earlier landings on legs, not tower catches. [Lars Blackmore: autonomous precision landing of rockets](https://www.nationalacademies.org/read/23659/chapter/10)

**Your move:** The booster's best decision of the day was not to try. How would you design a machine to recognize that it is outside the conditions it can handle, and what should it do then? Where on your own robot is there no way to abort?

## Surgical robotics: control, distance and trust

### A surgeon at the controls
**Established clinical technology**

Intuitive describes its da Vinci systems as surgeon-controlled: the surgeon operates the camera and instruments through the system. That is different from a machine independently deciding how to perform an operation. [Intuitive: how da Vinci works](https://www.intuitive.com/en-us/patients/da-vinci-robotic-surgery/about-the-systems)

**Ask:** How can a machine extend a clinician's precision while preserving clear human control? Which information does the surgeon need, and how should the system communicate a problem?

### A long-distance research demonstration
**Animal research**

In 2024, ETH Zurich and the Chinese University of Hong Kong demonstrated magnetic endoscopy controlled from Zurich in an anesthetized pig in Hong Kong, about 9,300 kilometers away. ETH reports a delay of roughly 300 milliseconds. This was a research demonstration, not routine remote human care. [ETH: remote endoscopy](https://ethz.ch/en/news-and-events/eth-news/news/2024/08/press-release-operating-from-9300-km-away.html)

The collaboration is as interesting as the distance. It brings together expertise in different places to test a difficult problem. And a faster network is not the whole answer: control, visualization, local clinical capability and a response to interruption all matter.

**Discuss:** What should remain under local control? How would the system behave if the connection degraded? How should a remote expert and an on-site team share responsibility?

### What next-generation connectivity could add

The ITU's 2026 discussion of **IMT-2030**, the framework for 6G, includes reliability, low latency, AI and integrated sensing in developing technical requirements. Those goals make interesting research questions for robotics, but the ETH demonstration already worked without waiting for 6G. [ITU: the 6G framework](https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/)

Ask what performance a particular task actually requires, then test the entire system. A network label does not by itself establish that a clinical or safety-critical application is ready.

**Your move:** Pick one task you care about, such as steering a robot arm or stopping a moving machine. Work out the longest delay it can tolerate and what must happen when the link drops. If you can state that number and defend it, you are ahead of most product announcements.

## Look for the transferable idea

A construction layout robot teaches us about translating a model into reality. A space robot teaches us about delayed communication. A medical system teaches us about precise action near vulnerable tissue. A student does not have to master all three fields to notice that the questions overlap.

**Your move:** Take one thing your own team has already solved, such as aiming, gripping or knowing where the robot is on a field. Name two places outside competition where that same problem exists and someone is still struggling with it. That list is the start of a project.
