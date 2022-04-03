---
title: Is It Really A Boolean?
date: 2022-04-03
status: draft
---

# Is It Really A Boolean?

Recently in a Thoughtbot blog post [TODO: link], Josh Clayton wrote about how to reduce a leaky abstraction caused by ActiveRecord.
The post is great, and the fix that's suggested for the example abstraction leak is a good one.
However, because it's an example, there's not much ink spilled as to _why_ the field was a boolean in the first place [TODO: expand].
I believe that this falls into one of the most common data modeling traps: representing things as booleans when they're not.
Because an ounce of prevention is worth a pound of cure, let's look at a few heuristics you can use when thinking through whether to model something as a boolean.

## Is the boolean state likely to change over time?

One really common trap is to model something as a boolean that has a temporal aspect to it.
This is exactly what happened in the above post: a field was modeled as a boolean, and it was fine until a temporal aspect of the thing it was modeling was introduced.
Booleans have no concept of temporality, and as such they're not particulary good at modeling data whose state changes often.
Even if your data really does only have two states, by modeling it as a boolean you lose any ability to introspect when those states change.

## Is the data nullable?

This is sometimes called the "three state boolean" problem.

For example, consider someone accepting those horrendous cookie banners that plague nearly every web page these days:

```go
type User struct {
    // denotes whether or not the user has clicked our annoying cookie banner
    // if this field is nil, the user has not clicked either "accept" or "reject"
    HasConsentedToBeTheProduct *bool
}
```

That boolean has three states: "accepted," "rejected," and "has not said one way or another."
In cases like this, you're often better off modeling each state as an enum:

```go
type CookieAcceptanceState int

const (
    CookieAcceptanceStateNone CookieAcceptanceState = iota
    CookieAcceptanceStateAgreed
    CookieAcceptanceStateRejected
)

type User struct {
    CookieAcceptance CookieAcceptanceState
}
```

## Booleans as snapshots

