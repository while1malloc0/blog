Like many software engineers in the industry, I don't have a Computer Science degree.
I spent my college years in music school, doing an undergraduate degree in jazz guitar performance and most of a graduate degree in music technology.
I've had the conversation about how music is like software a few times, and recently [this tweet](https://twitter.com/CatMcGeeCode/status/1272097365764300802?s=20) got me reflecting about the things I apply in my technology career that I learned in music school.
While I might not have gone on to be a professional musician, it turns out that music school taught me many things that I still find valuable today.

**Focus on the (important) fundamentals**
Few classes in the traditional music school curriculum are as polarizing as the pair of music theory and ear training.
In a music theory class, you study the structural underpinnings of what most people refer to as Classical Music[^1], and ear training is where you teach your brain to put names to the sounds that your ears hear.
I personally loved music theory and wasn't fond of ear training, and in hindsight I should have worked harder on the latter and less on the former.
Music theory tickled the same part of my brain that programming does because it's all about breaking down structures into understandable units, giving names to abstract concepts, categorization, and analysis.
In short, it's a puzzle, and it almost certainly didn't make me a better musician[^2].
At no point when creating improvised music do you have time to think "haha, I know, I'll use an altered dominant chord here, that'll be great," and if you do you're likely not listening to the people you're playing with very closely.
Instead, you hear a sound in your head, and at the best of times your brain knows exactly how to translate that into notes on your instrument.
As you probably guessed, the class that teaches that is the one that I wasn't particularly fond of.

There's a similar split in usefulness when dealing with the fundamentals of programming and Compute Science.
Is it important that the average programmer can rattle off the finer points of Von Neumman architecture?
Probably not.
But it's infinitely useful to be able to pattern match problems against known-good patterns for solving them.
If I can see that a problem models well as a finite state machine in a funny hat, then a good portion of solving the problem is already done for me.
The useful fundamentals are the ones that build your ability to pattern match a problem against a solution.

**Practice what you don't know**
There's a not-so-fine line between practicing and playing what you already know is going to sound good on your instrument.
The former involves meticulously working on making new musical concepts familiar, and the latter generally sounds good.
"Noodling" on one's instrument is fun, but it's not likely to make you much better[^3].
In contrast, practicing new songs, scales, etc. will almost certainly make you a better musician overall.
It will just as certainly sound terrible until you've worked on it for far longer than is likely comfortable.
A little-known fact about being a professional musician is that you spend most of it sounding terrible in private so that you sound good in public.

There's a particular type of musician[^4] who spends all of their time running scales that they already know at faster and faster speeds.
When they play on stage you can tell what they've practiced, because their music consists of scales played really really fast.
There's a certain physicality to that that's impressive, but I've never particularly found it musically interesting.
Likewise, if I spend my career going company to company building the same application, I'm likely not to grow much as an engineer after a certain point.
It's totally reasonable to become a master at building a particular kind of thing, and I'd never begrudge anyone the economic security that can come with being able to build something that companies need really fast because you've done it a hundred times, but it's important to recognize that that's likely _not_ a path towards building one's technical chops.
If you want to get better, sometimes you have to do something new.

**Listen to others**
One of the things I look back on most fondly about music school is its culture of sharing influences.
A frequent topic of conversation is what you and your friends are listening to, and what ideas you're taking from them.
The best musicians I know take in a wide variety of influences and find things to appreciate about music they don't necessarily like.
Most programmers--myself included--could stand to do more of that.
Explore outside of your own ecosystem, and if you find yourself less-than-enamored with a language or tool, try to find some good ideas in it.

**Learn your history**
One thing that music school does better than CS programs is the study of the history of the field, full stop[^5].
Every music school student is required to take a certain number of music history courses, and composition students--the Enterprise Architects of the music world--generally have a pretty firm understanding of when they're being imitative vs innovative.
And even in the most basic history classes--the kind that non-majors take when they think it's going to be an easy elective, not realizing that the tests are basically a game of music trivia where you've just heard all of the songs for the first time this week--there's at least an attempt to contextualize innovation even if it sounds old to us now.

I took a history of opera class as a sophomore, and at no point was Verdi referred to as "legacy" or "deprecated"[^6].
Contrast that with how history is viewed in tech, if it's learned at all.
Chapters in a history book written by the comments sections of popular tech industry sites would contain passages like "HTTP was originally developed by Tim Berners Lee at CERN in 1989, but no one uses that anymore because Google came out with gRPC and it's much more performant."
Taking the time to learn and contextualize the history of programming languages and tools will almost always make you better at assessing new technologies and techniques.

**There's no substitute for learning from an expert**
I was mostly a self taught guitar player until my first semester of music school, and I'm pretty sure that I improved more in those first few months than at any other point.
Experts who are good teachers will be able to watch you play and pick out the one thing that you need to do right now to improve, and then give you a bunch of other things to work on that will keep you improving for months.
You can teach yourself a lot of things, both in music and in programming, but there's no substitute for sitting down one on one with an expert and learning from them, even if you don't do it regularly.

If you have the chance to pair program with an expert, do it, and ask for feedback.
One of the best pairing experiences that I've ever had was with my former colleague [John Mileham](https://twitter.com/jmileham), who at the time was the head of architecture and interim lead of the security team at the company that we worked for.
He was working on some security code written in Go, and because I had a burgeoning interest in the language he was nice enough to invite me to pair on it together.
I was "driving", and after we implemented the feature I went through my normal process of interactively adding chunks to the git diff with `git add -p`.
After I added the second or third diff, he stopped me and said something to the effect of "Can I make an observation? You go way too fast when you code."
It was feedback that I'd never received before, and it was exactly what I needed to hear to get better.
I'd gotten to the point where I was a relatively competent programmer, but made mistakes often enough because I didn't slow down to consider code before committing it, and nobody had sat with me to watch me code so it just seemed like I was careless.
If I hadn't gotten that one on one time with an expert, I likely would have kept making the same mistakes.

**Teaching others makes you better**
One of the hardest things I've ever tried to do is teach the difference between major and minor to a child learning to play the guitar.
While programming as a career tends to be a fairly applied discipline, its foundations are largely mathematical, and that shows when you're able to explain things with relatively precise language without too many exceptions.
In contrast, major and minor are labels that were applied to patterns of sounds long after they were in common use, and as such basically every explanation has some sort of exception to it.
Major is happy, except that "happy" isn't really a universal reaction, and some "major modes" are more "floaty" or "bluesy," and the sound of a chord is all contextual anyway so major after minor might be interpreted as "triumphant" or "ironic" instead of happy, and so on.
Every explanation besides the technical one is squishy and filled with squishy exceptions, and the technical one is both likely to be uninteresting to a child--and most adults--and won't help them be a better musician.

Having to come up with these explanations gave me a much better understanding of the thing I was explaining, and the same is true of programming.
When you learn something, one of the barometers for how well you've learned it is how well you can teach it to others.
If you really want to learn something well, schedule a talk about it some number of weeks in the future.
It doesn't have to be a high-stakes speaking engagement; a lunch and learn with your team arguably works better.
During the course of practicing your talk, act out audience questions and regularly check in with yourself as to whether you're parroting phrases or really understand them.
By the time you give your talk, you'll either know the topic well, or be able to identify where you need more study.

**Know your audience**
Ask any working musician to play a "wedding gig," and they'll know exactly what you mean: show up early, dress nicely, play the hits at a reasonable volume, get paid and (hopefully) fed, and leave.
I'm sure there have been exceptions, but most of the time the jazz trio that plays during cocktail hour serves the same function as the nice tablecloths and fancy glassware: they're there to add ambiance and set a mood.
The musicians know this and know who their audience is, which is why they mostly don't show up in shorts and saddles doing their best Pharoah Sanders impression.

Like music, there's an element of craft and creativity to writing code.
And like musicians, programmers have a tendency to be drawn to certain coding styles and enjoy others less.
Where the latter could learn from the former is in keeping a user-first approach to the creativity that they're being paid for.
Even if they're making up a solo on the spot, a musician playing a wedding knows that they need to keep their choices conservative, because the thing they're making isn't about them.
Like Marty McFly trying to sneak in an Eddie Van Halen-esque tapping solo into the middle of _Earth Angel_, programmers sometimes lose sight of the goal and decide to do the fun thing instead of the thing that their users want.
There are times where innovative and delightfully weird technologies are a perfect fit, just like there concerts for innovative and delightfully weird music.
But at the end of the day, if you're getting paid then you should be doing what the audience wants.
That might mean cultivating a career such that what the audience wants is exactly what you want to do, but it's far more likely that that means that you have side projects in weird languages and a guitar in your basement for playing thrash metal on.

**You're going to fail sometimes**
It's the day of the concert.
You've prepared, you know your parts inside and out, and you've rehearsed for hours upon hours.
You've got this.
You take a deep breath, get into your creative head-space, grab your instrument, head out on stage, and... proceed to play one of the absolute worst shows of your life.

It happens to everyone at some point: you do everything right, and still for whatever reason the cosmos has just decided that today will be the day that you learn that life isn't fair.
Maybe you flub one of your first few parts and it blows your confidence for the rest of the show.
Maybe you didn't get enough sleep the night before because you were too excited, and now your brain is tired and doesn't want to be creative.
Maybe you had way too much coffee that day and rush every note that you play.
For whatever reason, things went badly, and now you have to decide what to do about it.

This is one of the areas where I think that tech is a bit better at dealing with things, at least in a mechanical sense.
We have incident retrospectives, we publish stories about our failure, and some companies even practice failing so that they fail better when they fail for real.
But the thing that musicians tend to be a bit more realistic about in my experience is the emotional impact of failing.
Having a bad concert is one of the worst feelings I've ever had, and is one of the few jobs I've had that I still have occasional stress dreams about[^7].
And while most of us in tech know that we should be divorcing our self-worth from the code that we write, we're not always great about talking about the messy reality of that.
Yes, we make tools, and in a sense getting upset about them is like getting upset about a hammer.
But the thing that just brought down prod was _my_ hammer dammit, and I really put a lot of work into it hoping that everyone would like it, and I really hoped that everyone who used it would think that I'm a smart and capable engineer so that I'd be considered for the cool projects, and now everyone is scrambling and thinks I can't code, and god maybe I'm just not good at this or something...

Eventually, most of us fail often enough that we learn that it's just part of the job, but that first failure stays with you for a while.
And in both music and tech, the best thing you can do for someone in that situation is to normalize it.
If production is down, and you know that the thing that just brought it down was written or operated by a newer engineer, your first response should be to make a note to tell them all about the time that you brought down production as soon as things are sorted.
If you're reading this and haven't brought down production yet, I hate to tell you that it's overwhelmingly likely that you're going to.
When you do, know that every senior engineer on your team has likely been there at least once, and that a lot of them probably felt self doubt about it until someone told them not to.

In a way, this post is a retrospective on my failure at being a professional musician.
While I never consciously said "I'm not a professional musician anymore," there was a point at which I realized that the programming thing that I was doing to make money while working on my music was far more likely to be my actual career path, and that I actually enjoyed programming a lot in its own right.
It turned out to be the right decision for me.
I'm happier professionally as a programmer than I was as a musician, and I enjoy playing music more now that it's not tied to my economic security.
But when I decided to give up on the idea of making a living off of music, I couldn't help but feel like I was throwing so much time away.
I had spent nearly 7 years in school and dedicated countless hours to practicing and studying music.
I was wrong, and in retrospect that's the biggest thing I learned from my time in music school: sunk costs are a trap.
Maybe the thing you've invested so much time in really just needs that last 1% push that you keep telling yourself it needs.
But be open to the possibility that you need to try something else instead, and don't let the prospect of having spent time on something deter you.
That time wasn't wasted, because in the end you likely learned something.

[^1]: What to actually call it is a matter of fierce debate in some circles. I like Western European Classical music, but that's a mouthful, and is likely missing nuance.
[^2]: There's definitely benefit to learning music theory as a musician, but not if it's learned at the expense of ear training. Being able to write _about_ music only gets you so far in making it.
[^3]: I don't mean to disparage noodling, as it's basically all I do these days.
[^4]: A great many of them are guitar players.
[^5]: This is in no way meant to say that music school history curricula don't have a lot of issues. They're overwhelmingly myopic in their portrayal of music history as being a linear progression of Western European composers from 1685-1942, to the point that the study of other traditions' music history is usually  dismissively categorized as "Ethnomusicology," which is a separate discipline entirely. Popular music is often looked at with complete disdain. My thoughts on the matter are mostly rants, but if you want scholarly work, I'd recommend the writing of [Ethan Hein](http://www.ethanhein.com/wp/), a former classmate of my at NYU and a brilliant thinker in the music education space.
[^6]: Musicians do, however, have a cargo culting habit that gives tech a run for its money.
[^7]: The other is waiting tables. Be nice to your service staff, folks. Their job is likely more emotionally taxing than yours is.
