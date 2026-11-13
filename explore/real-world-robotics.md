# Six examples that turn curiosity into engineering

Start with the human need. Then ask what the machine, the operator and the rest of the response system must do together.

## 1. Bring an AED before the ambulance

**If a drone can deliver dinner, could it deliver a chance to survive?** Imagine a cardiac arrest three blocks from a school. An automated external defibrillator (AED) is nearby, but inside a building. What if a 911 call could launch a dedicated AED drone while the dispatcher guides CPR and the ambulance is already on its way?

### Why this is personal for Brad

As a volunteer firefighter in suburban Minneapolis in the 1990s, Brad often helped with CPR while waiting for paramedics and their defibrillator. He remembers performing chest compressions or helping provide oxygen during many unsuccessful resuscitation attempts. He does not recall a survivor among the people he personally helped resuscitate. Those memories make the minutes before equipment arrives feel very different from numbers on a chart. They are why the possibility of faster AED delivery matters to him.

**CPR and defibrillation work together.** CPR helps keep blood flowing to the brain and heart. An AED analyzes the rhythm and advises or delivers a shock when appropriate; not every cardiac arrest has a shockable rhythm. Faster access matters, but it complements CPR and emergency medical care rather than replacing them. Follow 911 dispatcher and AED instructions, and do not interrupt CPR to go searching for a device when someone else can retrieve it.

**What a minute can mean:** The American Heart Association's 2025 guidelines cite a registry study of witnessed out-of-hospital arrests with an initial rhythm of ventricular fibrillation. Each additional minute to the first shock was associated with a **6% lower probability of survival to hospital discharge**. This is an observed relationship in that group, not six percentage points subtracted from every patient's chances each minute. [AHA 2025 guidelines, section 9.2](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support/)

### This part is already being tested

**Sweden:** In a study published in 2023, drones delivered AEDs before ambulances in 37 of the 55 cases with comparable arrival times, gaining a median 3 minutes and 14 seconds in those earlier deliveries. Bystanders attached the delivered AED before EMS arrival in six confirmed cardiac arrests. The important next step is not merely getting equipment to the address, but getting it into use.

**United States:** Duke Health reported in November 2025 that a clinical trial in Clemmons, North Carolina, was dispatching AED drones during real 911 calls, alongside EMS. A dispatcher coordinates with a drone pilot, the aircraft lowers the AED by winch, and the dispatcher guides a bystander in retrieving and using it. That is remarkably close to Brad's starting question, not a scenario that must wait until 2050.

### The next design challenge: a neighborhood response network

Brad's idea is to think beyond one aircraft: could schools, fire stations, police stations, pharmacies or rural community hubs host a network that brings AEDs to nearby homes and public places? Treat these as possible sites to evaluate, not instructions to remove the only AED a school needs.

- **Place it where minutes matter.** Map travel times, cardiac-arrest locations and communities poorly served by existing response.
- **Make it ready when the building is closed.** Consider dedicated outdoor equipment, batteries, maintenance and safe delivery in wind, rain and darkness.
- **Keep the whole response working.** Coordinate dispatch and flight permissions, retain on-site AED coverage, and design a handoff that does not pull the only rescuer away from CPR.
- **Measure useful help, not impressive flight.** How much sooner are the pads attached? Can a frightened bystander find and use the equipment?

### From equipment on a wall to a resource on a network

Brad's analogy is the parked car: what if an asset waiting in one place could serve someone who needs it elsewhere? Applied to emergency equipment, the goal is not to keep every AED busy. A device waiting for an emergency is doing its job. The opportunity is to connect that readiness to a larger neighborhood without leaving its home site unprotected.

**A building block already exists.** PulsePoint's National Emergency AED + Resource (NEAR) Registry connects resource locations with emergency communication centers and records access information. In participating communities, AED-needed alerts ask subscribed people to bring a registered device to a nearby emergency. These alerts use the AED's location, not the subscriber's personal location. That is a useful companion to the location-aware responder concept that inspired Brad, but it is not an automatic drone-launch service.

**The question worth building around.** Could a 911 system match a confirmed incident location with the fastest appropriate, ready resource, then coordinate a person or an authorized drone delivery? The nearest pin on a map may not be the fastest usable AED. The system would need to know whether the cabinet is accessible, the device and aircraft are ready, the route is safe, and someone can receive the package. A dispatcher-supervised network could automate the matching while keeping emergency judgment and fallback arrangements clear.

- **Technical readiness.** Design trustworthy status updates, secure dispatch commands, accurate delivery locations and a safe response to lost communications. Test the full chain from call to usable equipment, including failures, not just successful flights.
- **Access and operating responsibility.** Who can release the equipment, who receives it, and who replaces used pads or restores the kit afterward? Plan for locked buildings, nighttime access, languages, disability access and overlapping emergencies. A dedicated community delivery AED may be better than borrowing a school's only unit.
- **Policy and sustained funding.** Agree on ownership, medical oversight, aviation approvals, privacy, liability, staffing and maintenance before launch. Include communities with few resources, not only neighborhoods that can afford the hardware.

The same design question could extend to bleeding-control kits or other first-aid supplies. NEAR already lists bleeding-control kits, epinephrine and naloxone alongside AEDs; that does not establish that any particular item is approved for drone delivery or appropriate for every caller. Each proposed payload needs its own clinical purpose, storage requirements, trained support and delivery plan. The student challenge: choose one community, one emergency need and one measurable improvement, then build a small simulation before proposing a fleet.

- [PulsePoint: NEAR emergency-resource registry](https://www.pulsepoint.org/near-registry)
  - Explore the existing information infrastructure for finding equipment, understanding access and notifying people. Ask what an authorized delivery layer would need to add.
- [PulsePoint: 911-initiated AED-needed alerts](https://www.pulsepoint.org/aed-needed-alerts)
  - See how responsible parties and approved subscribers can already help move a nearby AED toward an emergency.

A further question is whether a future mobile robot could assist when no capable bystander is present. That adds harder tasks: reaching the patient, gaining access to the chest, placing pads and supporting safe clinical decisions. The studies linked here use human bystanders, not autonomous robotic treatment. For a young engineer, the invitation is to choose one missing step and ask how it could become safer, simpler or faster.

**Explore the evidence**

- [Swedish AED drone study](https://pubmed.ncbi.nlm.nih.gov/38000871/)
  - A real-world study linking delivery times to bystander use. Look at the gap between arriving first and actually helping.
- [Duke's 911 drone trial](https://corporate.dukehealth.org/news/drones-now-deliver-aeds-during-real-911-calls-first-its-kind-us-study)
  - See how researchers and public-safety teams connect dispatchers, pilots, drones and people on the ground.
- [American Heart Association: AEDs and CPR](https://www.heart.org/en/news/2023/01/17/5-things-)
  - Understand why CPR and timely defibrillation belong in the same response, and how an AED guides its user.

## 2. Put a machine in the risky position
**Evidence: deployed firefighting equipment.** The Los Angeles Fire Department introduced the remotely operated Thermite RS3 to deliver water while keeping an operator farther from a hazardous position. It demonstrates that useful robotics does not require complete autonomy. [LAFD introduction and visuals](https://lafd.org/news/lafd-debuts-rs3-first-robotic-firefighting-vehicle-united-states)

**Ask:** Which task needs a person physically present, and which needs human judgment from a safer location?

The RS3 changes where a person needs to stand to apply judgment and useful force. It suggests a practical kind of progress: let the machine bear more exposure while trained responders stay involved in the decision. A remotely operated system can be a major advance without pretending to replace the crew.

## 3. Make an unfamiliar building understandable
**Evidence: development and testing.** Indoor-drone mapping work highlighted by NIST explores how images and maps can help incident commanders. The hard parts include narrow spaces, limited flight time and environments where GPS is unavailable. [NIST's mapping story](https://www.nist.gov/blogs/taking-measure/drones-disaster-zones-how-advanced-3d-mapping-technology-can-help-first)

**Ask:** What does a responder need on a map that a beautiful 3D model might not show?

A map becomes valuable when it reduces uncertainty at the moment a decision must be made. Think beyond impressive imagery to routes, obstacles, confidence and information a responder can actually absorb under pressure.

## 4. Sense the hazard without sending someone toward it
**Evidence: technology development.** NASA-supported Squishy Robotics developed drop-resistant sensor robots for hazardous environments. A device left near a hazard can provide a different view than a drone passing overhead. [NASA story and images](https://www.nasa.gov/technology/tech-transfer-spinoffs/nasa-developed-spherical-robots-to-the-rescue/)

**Ask:** Which measurements would change the decision to approach, evacuate or wait? How would uncertainty be displayed?

Squishy Robotics invites a different mental picture of a robot: not necessarily something that walks, but something that survives arrival and reports from a place people should not yet enter. A small package of trustworthy information can change a large decision about exposure and response.

## 5. Turn readings into an earlier warning
**Evidence: AI research.** NIST researchers have investigated machine-learning models that predict flashover using temperature information. This is an example of interpreting measurements, not simply adding another camera. [NIST research overview](https://www.nist.gov/news-events/news/2022/08/ai-may-come-rescue-future-firefighters)

**Ask:** How early must an alert arrive to be useful? What are the costs of missed warnings and frequent false alarms?

Flashover is a dangerous transition in a compartment fire, when conditions can escalate rapidly. The promise of prediction is time to recognize danger and act, rather than a more detailed account after the event. That makes the quality and timing of a warning as important as the intelligence of the model.

## 6. Make an ordinary factory task less difficult
**Evidence: company announcement and investment.** Nidus announced $30 million in funding in November 2026 to develop AI-enabled robotics for existing manufacturing workflows, beginning with wire harnesses. Flexible wires are a revealing challenge: they bend, move and do not behave like rigid blocks. [Nidus announcement](https://www.prnewswire.com/news-releases/nidus-raises-30m-to-deploy-embodied-intelligence-in-americas-defense-factories-302934756.html)

**Ask:** Why might a repetitive task still be difficult to automate? What would the robot have to sense instead of assume? Nidus's defense focus also provides a concrete opening for the [dual-use discussion](../discuss/questions-and-shared-standards.md).

A wire harness makes an excellent lesson in the gap between repetition and simplicity. Humans adapt to flexible objects almost without noticing; a robot must sense and manage those variations. Solving an unglamorous task can unlock meaningful industrial value.

## Test every idea against the real world

| Dimension | A better question |
|---|---|
| Time | How long from unpacking to useful information or action? |
| Reliability | What happens when a sensor disagrees or a radio link drops? |
| Access | Can it handle stairs, rubble, mud, water or confined spaces? |
| Human use | Can someone operate it with gloves, noise and divided attention? |
| Economics | Can the intended organization afford, maintain and train with it? |
| Value | What measurable risk, delay or burden does it reduce? |

AI may help with perception, planning and interpretation. Remote control may be better for some tasks. Choose the technology after defining success.
