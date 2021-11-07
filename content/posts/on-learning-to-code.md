# Coding advice is writing advice, not math

Between review season, gearing up to teach a code camp, and having a few friends working on career transitions into engineering, I've been thinking a lot about learning to code recently.
It's been a while since I wrote my first "hello, world" and the longer my career goes the harder I find it to recall the feelings of confusion associated with learning to code.
That isn't to say that I'm not empathetic, just that it's harder and harder to conjour up precise memories of those feelings myself.
In much the same way that I don't remember what it's like to listen to music and not be able to dissect it critically due to my music school training, I don't remember what it feels like to be presented with a coding problem and have no idea where to start or what to do.
This isn't because I'm some brilliant programmer, just like my analytical abilities in music aren't because I'm some genius musician (trust me, I'm not), it's just that after enough years of doing something and being trained in certain analytical tools and ways of thinking, it becomes hard to remember what life was like before you had those tools.

What this means to me is that it would be disengenous for me to write a post about dealing with the feelings of confusion and frustration that normally happen when you're writing your very first programs.
Even though I want nothing more than reassure the people in my life who are learning to code that the feelings that they feel are normal and happen to most of us (they are and do), I don't personally remember them well enough to write about them in good faith. 
What I can write about, because it never really stops, is advice and the role it should play as you're building up your coding toolbox.

In learning to code, you'll encounter a lot of advice.
As a small, possibly representative example of the kinds of advice you encounter as a beginner or intermediate coder, I was presented with all of these opinions during the course of my first programming job:

- Write unit tests first; practice test driven design.
- Most tests are a waste of time, focus on writing integration tests.
- Object Oriented Design is the best paradigm for modeling the real world.
- Functional Programming leads to safer and easier-to-understand programs than Object Oriented Design.
- Frameworks are great. They boost productivity by taking care of the commidity aspects of coding for you.
- Frameworks are bloated and shouldn't be used in most cases.

The thing about all of these pieces of advice is that none of them are true.
None of them are false either.
That's because programming isn't math, and programming advice isn't mathematical.
The goal of programming isn't truth, it's functionality, and the goal of programming advice isn't to tell you what's true, it's to tell you what's useful in achieving functionality.
At best, most programming advice is a well-articulated opinion on a technique to use in some constrained use case.
Your job as the person learning to code is to figure out which techniques are useful _for you_.

Stephen Bachelor, in talking about his interpretation of early Buddhist cannon, makes the distinction between engaging with text as a scholar versus a practitioner.
A scholar seeks to know what is and isn't true.
The practitioner seeks to know what's useful to them in their practice.
Some research use cases aside, coding advice is best approached with the latter mindset.
Every bit of coding advice (including this one) should come with a warning label: "None of this is true, but some of it might be useful."

One of my favorite quotes on the topic of advice comes from the comic book writer [Kieron Gillen](https://twitter.com/kierongillen/status/949977810533343233?s=20):

> Some meta-writing-tip advice. When you read someone's writing tip and you agree with it, try and work out where and when it doesn't apply. When you read a tip and disagree, try and work out which situations it may be true or the creator's intent in saying it. For bonus marks, try and work out what your agreement or disagreement says about how you approach writing and what it says about you.

We can use this technique to critique programming advice as well.
To work through a few of the examples above:

- I agree that writing tests first is a good default most of the time.
In my experience, bolting the tests on afterwards is much harder, and writing for testability usually helps the modularity of code.
However, in languages with advanced type systems, driving the design of the program with types instead of tests can lead to just as much confidence in the design with less code.
Also, this advice never applies to prototype code.
- I disagree that most unit tests are a waste of time.
However, I agree that integration tests are extremely useful for catching broad classes of bugs, and if I only had to pick between unit and integration tests I'd likely pick the latter.
Also, you can seriously overdo unit testing, and with mocks it's pretty easy to write tests that don't actually verify anything.
For instance, testing that a subclass does, in fact, inherit from its parent class is likely not testing anything useful. 
As with all advice, there are times when that statement also doesn't apply.
- I'm not sure about best, but I personally find Object Oriented Design a lot easier to use when modeling real-world business processes than other paradigms.
However, not all programs model business processes, and OOD has a hard time escaping from bugs related to state.
You can talk about disciplined coding all you want, but at some point you're going to write a bug related to some sort of shared mutable state.
In some critical systems, functional programming can be a safer alternative since things like referrential transparency can help one reason about systems.
- I generally like frameworks and think they're good defaults for certain classes of programs.
However, there are very few frameworks that I'd call small, and if you're not going to use of most of the functionality that's provided, including a large framework is likely just increasing your startup time without much benefit.

Learning to code takes time, energy, and often quite a bit of frustration.
You'll hit walls, you'll write lots of bugs.
The tips presented here might help your outlook, but the most important characteristic is whether or not you stick with it.
