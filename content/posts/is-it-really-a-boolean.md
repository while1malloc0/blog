---
title: Is It Really A Boolean?
date: 2022-04-03
status: revising
---

# Is It Really A Boolean?

In a [recent post](https://thoughtbot.com/blog/reducing-leaky-abstractions-introduced-by-activerecord) on the Thoughbot blog, [Josh Clayton](https://twitter.com/joshuaclayton) wrote about reducing leaky abstractions caused by ActiveRecord.
As a working example, he shows a common way of modeling blog post data: a `Post` class with a `published` boolean field.
It's a great post, and the fix that's suggested for the leak is a good one.
Josh looks at the problem through the lens of ActiveRecord, but it's also a great example of a common error in data modeling more generally: storing values as booleans that really shouldn't be.
Let's look at some questions you can use to figure out whether storing a value as a boolean is a good idea.

## Is the "when" important?

One common mistake is to store data as a boolean that has implicit date information attached to it.
In Josh's example, the "published" field becomes a problem because publication date is an important piece of information.
Booleans don't have a notion of time. 
As such, they're generally a poor fit if _when_ something happens is important.

**Takeaway: if the "when" is important, don't use a boolean**

## Is the data nullable?

This is sometimes called the "three state boolean" problem.

For example, consider the case of a user accepting the horrendous cookie banners that plague the web:

```go
type User struct {
    // denotes whether or not the user has clicked our annoying cookie banner
    // if this field is nil, the user has not clicked either "accept" or "reject"
    ConsentedToCookies *bool
}
```

That boolean has three states: "accepted," "rejected," and "has not said one way or another."

In cases like this, you're often better off modeling each state as an enum:

```go
type CookieConsentState int

const (
    CookieConsentStateNone CookieConsentState = iota
    CookieConsentStateAgreed
    CookieConsentStateRejected
)

type User struct {
    CookieAcceptance CookieAcceptanceState
}
```

**If your data has more than two states, don't use a boolean.**

## Booleans as snapshots

You might be thinking "wait, isn't _when_ the user accepts cookies important?"
Indeed it is.
In fact, one of the key provisions of the GDPR is that a user can revoke consent for tracking at any time. 
This means that we not only care about when a user accepts cookies, but when they revoke that consent.
We have a few options to deal with this new requirement.
First, we could send events when this value changes state.
This might be a good solution if you're already streaming events into something like Honeycomb [TODO: link].
But we can also use data modeling to help here.
What we really want from our boolean is a snapshot of what the _current_ state of the world is.
In other words, does our user _currently_ consent to having their data pillaged with tracking cookies?

This sort of "snapshot boolean" is ultimately what the Thoughtbot post lands on (translated to Go for consistency):

```go
type Post struct{
    PublishedAt *time.Time
}

func (p *Post) IsPublished() bool {
    return p.PublishedAt != nil && *p.PublishedAt >= time.Now()
}
```

We can get a similar ability to view a "snapshot" of our cookie consent state by storing consent data as timestamps:

```go
type User struct{
    CookieConsentAcceptedAt *time.Time
    CookieConsentRejectedAt *time.Time
}

// [TODO: this is kind of messy]
func (u *User) ConsentsToCookies() bool {
    switch {
    // case 1: user never clicked "accept" 
    case u.CookieConsentAcceptedAt == nil:
        return false
    // case 2: user clicked "accept" and not "reject"
    case u.CookieConsentRejectedAt == nil:
        return true
    // case 3: user clicked "accept" and then clicked "reject" later
    case *u.CookieConsentRejectedAt > *u.CookieConsentAcceptedAt:
        return true
    default:
        return false
    }
}
```

**Takeway: use "snapshot" boolean methods to derive the current state from your data.**

---

So, here's the takeaway: the next time you're looking to model some data as a boolean, ask yourself whether or not it's _actually_ a two state value that's not likely to change.
If it is, great, write it as a boolean.
If not, consider storing it as an enum or timestamps and deriving snapshot booleans from that data.