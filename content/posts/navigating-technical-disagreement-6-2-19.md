---
title: "Navigating Technical Disagreement"
date: 2019-06-02
---
In *Never Split the Difference: Negotiating As If Your Life Depended On It*, Chris Voss writes that getting someone to say "no" is the start of a productive negotiation. 
Pushing for a hard "yes" can alienate and annoy people. 
"No" allows us to find hidden points of contention, and clarify what we actually want. 
Hidden contention is also at the heart of many technical disagreements. 
Discovering it is a powerful technique for making disagreements productive. 
Getting to "no" can be effective here as well, but I prefer to find common ground. 
Finding common ground means getting engineers to agree on core principles and values. 
One technique for this that I’m fond of is figuring out where on the **ladder of values** I agree with someone. 
The ladder of values is a mental model for arguing about projects.
Each step on the ladder is the foundation for justifying the step below it. 
The steps of the ladder are implementation, requirement, outcome, and goal. 
Finding common ground on one rung of the ladder allows me to better argue my views on the one below it.

Implementation is "lowest" level at which to argue. 
It's saying "I don't like line 37 of the code", or "I don't think this design pattern is the right choice." 
This is the level at which we engineers seem to enjoy arguing. 
It's the level that's often seen—incorrectly, in my view—as the most "technical". 
It's important to recognize that arguing implementation implies a ranking about what's important in the code. 
The person you’re arguing with may disagree with that ranking. 
If you suspect differing opinions about what to optimize for, confirm that before continuing the discussion. 
Aligning on requirements transforms "the function at line 37 should be more performant" into "the function at line 37 is trading some performance for being more readable. We agreed that performance is more important”

![values-ladder](/static/values-ladder.png)

**Requirement** is where you rank architectural drivers such as readability, maintainability, and performance. I believe—in the absence of any hard data—that most technical disagreements boil down to requirements. Sentences like “do we agree that readability is more important than squeezing every inch of performance from this code?” go a long way in ensuring that you’re arguing the same thing. If you both agree, great, go back to implementation details. If you disagree, you might need to agree on what outcome you’re trying to achieve, or on how the requirements contribute to that outcome.

**Outcome** is where you discuss what the project is trying to accomplish. This level underpins the ranking order of architectural drivers. “This tool is fast enough for us to use interactively” is an outcome. Ranking performance over readability when making trade-offs might make sense in supporting it. Agreeing on what outcome we’re trying to achieve and figuring out how ranking requirements will get us there before discussing implementation has sorted roughly 95% of my technical disagreements. The last 5% have had to go up another level and argue about the goal of the project.

Arguing a **goal** is about whether the project is worth working on at all. If the conversation necessitates arguing goals, it’s not going to be technical for much longer: you’ll soon have to talk about business strategy. Sometimes the calculus on whether something is worth working on is straightforward. If the options are a shiny new project that will marginally improve developer productivity and an all-out yak shave that will ensure the health of your database, you should break out the shears. If the priorities are this straightforward and the other person is still arguing for the shiny project, it might be a sign that they’re overloaded on operations work. Other times prioritization can be difficult. Maybe someone disagrees with the direction of the team, or even the company. In this case, sometimes the best thing to do is acknowledge the fundamental disagreement and end the argument. Alignment is tricky, and the headspace of a technical disagreement isn’t going to help here. You can also try to get the other person to agree to discuss at lower levels with the hypothetical “if you did happen to agree with the goal of the project, what would you think?”. You should take these answers with a healthy amount of skepticism. Disagreeing with the goal of a project invariably colors your thinking about any potential implementation of it.

The next time you find yourself in an intense technical disagreement, see if you can get your colleagues to common ground on the values ladder. You might be surprised by how much common ground you find, and how effective it is when you disagree with this shared context in mind.
