# When an alarm is not a location
### A question that stayed with me

*Bradley Shogren's recollection, edited for this collection.*

In the 1990s, I wore a PASS device as a volunteer firefighter. If it was activated and the wearer stopped moving, it would sound a piercing alarm. The hope was that another firefighter could hear it and come to help.

Now imagine a large building. A responder is down on an upper floor, far from the rest of the crew. An alarm may be sounding, but where should help go? Which floor? Which side? Which corridor? A floor number alone is not much help when the floor spans a city block.

Around 2001–02, while exploring entrepreneurship ideas in business school, I wondered whether a wearable device could give colleagues that location. I discussed the technical difficulty with a friend and did not pursue it. I am not telling this story to blame the advice or claim that I could have solved the engineering. I am telling it because a useful question survived even when I stopped working on it.

**“We cannot do this reliably with this approach” is not the same as “We can never do this.”**

## What the engineering tells us

GPS already supported vertical positioning in 2001. The challenge was not a universal ban on measuring height. It was obtaining a reliable, precise location inside buildings, including the right floor. Satellite signals, steel and concrete, changing conditions and the practical needs of responders make that a different problem from locating a car outdoors. The [2001 GPS performance standard](https://www.navcen.uscg.gov/sites/default/files/pdf/gps/geninfo/2001SPSPerformanceStandardFINAL.pdf) included vertical performance; the [FAA explains three-dimensional GPS positioning](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gnss/gps/howitworks).

A [NIST-funded indoor-location project](https://www.nist.gov/ctl/pscr/infrastructure-free-localization-system-firefighters) combined ultra-wideband ranging, movement sensing, radios and pressure measurements. NIST's [2026 first-responder tracking overview](https://www.nist.gov/blogs/taking-measure/how-thousands-tiny-dots-can-save-first-responders-lives) describes continued progress and the difficulty of dependable tracking in complex buildings.

The interesting question becomes: **What measurements can compensate for one another when any single sensor is imperfect?**

## Add a robot to the question

Could a robot accompany a crew, map the route and help maintain a communications link? Could it carry or place localization beacons? Could it go first into an uncertain space and return information that changes the commander's decision?

These are design questions, not a single promised product. Try separating them:

1. **Alert:** detect that something may be wrong.
2. **Locate:** report a position and how uncertain it is.
3. **Navigate:** identify a usable route to that position.
4. **Assess:** determine what conditions the rescue team will face.
5. **Assist:** carry equipment, relay communication or perform a task.

## Remembering Phil

Phil Otis was my friend from high school. The [National Park Service memorial](https://www.nps.gov/mora/learn/news/in-memory.htm) records that Phil, a 22-year-old Student Conservation Association volunteer ranger, died while responding to an injured climber on Mount Rainier on August 12, 1995. Ranger Sean Ryan also died during that rescue.

Remembering them invites a forward-looking question: **Can we get information or equipment to a person in danger while reducing the risk to those coming to help?** A small aircraft, ground robot or combination might someday help with part of a mountain mission. The terrain, weather, payload, communications and actual rescue still have to be solved. The point is not to claim a machine would have changed that tragedy. It is to honor the purpose of rescue by continuing to improve the tools.

## Your turn

Think of a problem someone you know has experienced. What part is a physical limitation? What part is a limitation of today's equipment? What would you measure first? Who has firsthand knowledge that could change your design?

You do not have to begin with the answer. Begin with a reason to care, then keep asking better questions.
