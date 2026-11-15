# A ball in the air: why throwing is a serious problem
### Reach, physics and repeatability

A robot that throws a basketball can look like a party trick. It is one of the harder things to ask of a machine: speed, angle and spin all have to be right at one instant, and nothing can be corrected once the ball has left. Researchers work on the same problem a competition team does, and its uses reach well past a gym.

## Throwing extends a robot's reach
**Research**

A robot that can throw can deliver to places its arm cannot touch, and faster than it can carry. Princeton and Google's TossingBot paired a physics model with a learned correction for everything the model misses, and threw unfamiliar objects into bins beyond its reach at more than 500 picks an hour with 85% accuracy. Another team taught a 12-ton material-handling machine to throw to targets outside its normal reach. Neither is in routine commercial use yet. [TossingBot project](https://tossingbot.cs.princeton.edu/) · [TossingBot paper](https://arxiv.org/abs/1903.11239) · [Throwing with a 12-ton machine](https://arxiv.org/abs/2405.19001)

**Your move:** Eighty-five percent is about one miss in seven. For what jobs is that already good enough, and for what jobs would one miss in a thousand still be too many?

## The physics your shooter already obeys
**Explainer and simulation**

NASA's guide derives the lift on a spinning ball, the reason backspin changes a shot. North Carolina State engineers simulated hundreds of thousands of free throws and found the best results near a 52-degree launch with about three revolutions per second of backspin, aimed just inside the back of the rim. Their numbers assume a release seven feet off the floor. Your robot is a different height at a different distance, so the method transfers and the answer does not. [NASA: lift of a spinning ball](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/ideal-lift-of-a-spinning-ball/) · [NC State: the physics of the free throw](https://engr.ncsu.edu/news/2009/11/06/nothing-but-net-the-physics-of-free-throw-shooting/)

**Your move:** Measure where your shots actually land, hundreds of them, and plot the spread. Which matters more for your machine: getting the average on target, or shrinking the spread? They are different engineering problems.

## Two thousand in a row
**Demonstration**

Toyota's basketball robot made 2,020 consecutive free throws in 2019, and a later version sank a shot from 24.55 metres in 2024. Toyota has not published how. [Toyota: CUE basketball robot](https://global.toyota/en/mobility/frontier-research/41965744.html)

**Timing with company:** A throw is one machine getting one instant right. For many machines holding their timing together, and beside people, watch the synchronized humanoid performance in [Listen and watch](listen-and-watch.md), then ask which is harder to repeat a thousand times.

**Your move:** A team that can put a ball through a hoop from across a gym has solved release speed, angle, spin and repeatability under changing conditions. Name three places where someone needs exactly that: a line to a person in the water, a part across a gap, seed onto a slope. Then ask what each one needs that a basketball court never asked of you.
