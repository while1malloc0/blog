---
title: My Engineering First Principles
date: 2021-11-12
status: published
---

# My Engineering First Principles

Gabe Ochoa, a friend and one of the most effective managers I know, recently let me read his "management first principles" document, a short list of fundamental statements that make up the core of his management philosophy.
This seems like a very useful document to have, so I decided to record my own list of first principles, adapted to my perspective as an individual contributor.

## Correctness is about code, writing code is about people

Whether or not a system is working as intended is a property of the system. 
It either does what it's supposed to or not.
_Writing code_ is about people.
Whether or not code is readable, easy to maintain, etc. is a function of the people interacting with it. 
There's no a priori way of writing code that's best for all people.
"Clean" is a deeply unhelpful descriptor.

## Technical arguments without data are just opinions

Opinions are useful, but they should be turned into data when it counts.
Past experience and estimations grounded in reality are forms of data.

## The medium is the message

Our tools shape how we think about solving problems in a way that puts limits on the solutions that we can implement.
Slow, brittle, inflexible tools encourage slow, brittle, inflexible code.

## The computers work for us

The current behavior of a piece of software does not dictate how we can solve a problem, because we can change or build upon that software.
Ignorance of a problem space, lack of incentives or support, and learned helplessness often masquerade as technical limitations.

## The best solutions are usually boring

Industrial software engineering generally has few novel technical problems and many novel business problems.
Misunderstanding which you're dealing with often leads to unnecessary complexity.

## Everything is a plugin

As many things as possible should be modeled on a system's extension points.
For example, software with a plugin system should implement as much fundamental functionality as possible with plugins.

## Run less software

The biggest contributor to complexity in software is dependencies.
Both at the level of code and systems, fewer dependencies is almost always preferable.