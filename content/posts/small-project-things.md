---
title: (working) Seasoning Problems
date: 2021-11-07
status: unpublished
---

# Seasoning Problems

## Intro

I've been thinking a bit about the types of problems that sneak up on software projects as they evolve.
There seems to be a class of issue that is:

1. Not related to the project's core functionality
2. Sneaks up on even very good engineering teams, and
3. Is exponentially easier to solve before it's strictly necessary for a project.

In short, these are issues that are almost never going to be the most important thing to work on in a project, but are generally much more painful when implemented at a time of necessity instead of being baked in early.
I call these seasoning problems since, like seasoning food when cooking, it's much harder to do later in the process, and also not strictly necessary (at least for nourishment).

Here's a completely non-comprehensive list of some seasoning problems that have bitten me, and some potential solutions that you might want to consider before it's strictly necessary.

## Testing third-party integrations

No project can do everything, so almost every project of a particular size ends up depending on a third party API of some sort.
Sometimes it's an API that's internal to your company, sometimes it's a vendor API, but one way or another you'll probably end up needing to call someone's code that's not yours over a network.
Unit testing integration points with third-party code has a stock solution in the use of mocks, but things get more complicated when we want to run higher-level tests.
There's a few different paths we can take to make this scenario tractable before integration tests become hard to manage.
If you're lucky, your third-party dependency provides a testbed for you, like the one that Stripe does.
If you're less lucky, you might need to write a fake for your third-party dependency.
If your dependency uses an IDL such as OpenAPI or protobufs, it's pretty straightforward to generate a fake server.
If it doesn't, it's often still worth the effort to write a minimal fake, knowing that it'll probably break once in a while when your dependency updates their API.

## Providing first-party testing support

Related to the above, if your project becomes successful enough, others are going to want to depend on it.
In that case, it can be a good idea to provide a way for others to simulate your service in tests.
Like a third-party service, you might choose to provide a fake server that your dependents can run as a process alongside their integration tests, or have a test endpoint group.
Either way, you should keep your testbed up to date with your API.
Again, an IDL makes things easier here.


## Structured output in CLIs

Projects that get sufficiently large and aren't CLIs themselves often end up with a CLI tool attached to them.
This tool is usually written out of necessity and grows organically to make it easier to do certain administrative tasks.
In some cases, the ultimate goal of the tool is to make maintainers' lives easier, and in others the CLI becomes a way of interacting with your project that's provided to users.
In both cases, thinking about providing some sort of structured output will make everyone's life easier in the long run.
Like it or not (and plenty don't), 
JSON has become something of a standard transport language for not only the web, 
but the terminal as well.
Adding JSON formatting to your CLI's output will allow your users to parse it with tools like jq or fx and more easily programmatically interact with its output.
Some projects go even further and provide JSONPath or other filtering flags, meaning you not only get structured output, but a first-party way of interacting with it.
If JSON isn't your thing, that's fine, but you should think about how to output your text in such as way that your users can use it as input to other common CLI tools that doesn't involve writing an AWK script to clean your output.

## Test times

This one sneaks up on people a lot, and it tends to be a boiled frog situation.
You start in a pristine state where even your integration tests run in under two minutes.
Then, slowly, test times start creeping up.
You don't think much of it, it's only a minute or two.
Get a cup of coffee, and when you're back the tests have finished.
Unfortunately, this situation has a habit of biting teams who are trying to practice good code hygiene and maintain reasonable levels of test coverage.
That PR you just merged that creeps test times up by a few seconds?
Each of your team mates is submitting one just like it.
Before you know it, you're staring down 45 minute test suites, and all because you and your team were trying to do the right thing.

One thing you can do proactively to prevent this from happening is to set a ceiling on your build time, including tests.
If your build time goes above this threshold, you investigate ways for getting it back down.
If you need a starting value, my personal default is 10 minutes.

## First party client support

If your service does something useful and provides some sort of external API, chances are good that others will want to start using that API programmatically.
At some point, you might end up in a situation where someone has written an "unofficial" client for your API (hopefully) in one of the languages supported at your company.
In most cases, it's totally cool to let people curate unofficial clients, as long as it's made clear that support is going to be limited.
The expectation that engineers will be on the hook for fixing random Bash wrappers around your service's APIs can inspire a great deal of well-deserved crankiness.
But if you want to do your users a solid, you can provide first-party client support for them.
Again, if you're using an IDL, client generation is just one of the perks.
If you're not, it might be worth examining the top two or three languages in use at your organization and providing clients for them.

## Architecture documentation

Let's face it, few of us are as good at documentation as we'd like, and that usually goes double for architecture documentation.
This one usually sneaks up on very old projects over years, and doesn't get discovered until Sophie, engineer 4 at the company and keeper of all architectural knowledge, decides it's time to persue her next challenge.
Then it's a mad scramble to extract every piece of context from Sophie's brain, but it's too late.
First off, Sophie doesn't remember the context for every decision that was made (would you?).
Second, the product has grown in ways that Sophie stopped being privvy to a while ago.
It turns out that no one really knows how the whole thing works anymore.

You can avoid this situation (or at least make it less stressful) by including an ARCHITECTURE.md doc that documents the basic architecture and drivers of the system.
I personally like the C4 model, but use whatever feels right to you.
Even if this doc goes out of date, it'll at least be a starting point for someone trying to get a high-level view of the system.

## Enforcement of component boundaries

This one tends to happen a lot more quickly than people assume it will.
One day, you have a system with clear boundaries between components, the next you have classes attempting to bypass visibility mechanisms in order to call private methods of other classes.
To get ahead of this problem, you need to think in two directions: layers and peers.
Layers are the broad-strokes boundaries of your code, usually operating at the level of groups of packages.
There are many ways of structuring these, but the key insight is that some groups of packages provide functionality that's more foundational than others.
Dependencies should only go one way: less foundational things should only depend on more foundational things.
Peer dependencies are how packages within the same layer interact with each other.
Two good solutions here are being explicit about your layers in your package structure and enforcing component boundaries using automated tools like ArchUnit.

---

Like I mentioned, this list is non-exhaustive.
There are other problems that crop up, some much worse than the ones listed here.
But I hope that this list at least helps keep you vigilant about certain classes of problem.