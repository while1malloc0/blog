# FizzBuzz as a Service in Clojure

FizzBuzz is a terrible interview question.
If you've never heard the problem, it goes something like this: "Write a function that takes an integer. If that integer is divisible by 3, return the string 'fizz'. If that integer is divisible by 5, return the string 'buzz'. If that integer is divisible by 15, return the string 'fizzbuzz'. Otherwise return the integer as a string."
At best, giving a candidate the FizzBuzz question will screen out the nearly-nonexistent population who are trying to get software engineering jobs without having coded before, but more likely the question will just insult the intelligence of the candidate and (hopefully) make them think twice about working with you.
However, a lot of things that make FizzBuzz a comically bad interview question make it a great problem for learning new things about a programming language.
From [enterprise FizzBuzz](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition) to [ludicrously code-golfed](https://codeburst.io/javascript-breaking-down-the-shortest-possible-fizzbuzz-answer-94a0ad9d128a) solutions, adding some arbitrary restrictions to the FizzBuzz problem turns it into a useful vehicle for diving into dark corners of a language, or learning a new one.
A personal favorite variation is to write FizzBuzz As A Service (FBAAS).
At its core, FBAAS service is about exploring all of the non-functional aspects of the problem.
The core logic is easy enough to write in a few lines, so you can focus on things like how a language or library handles routing URLs and serving web traffic.
I've been interested in learning some Clojure for a while, so I decided to write FBAAS in Clojure.
Here's how it went.

## First steps: installing lein and getting to "Hello, World!"

The first step for working in most programming languages is to install the language tooling and get to a program that can print "Hello, world!". Clojure is no exception.
Leiningen, often abbreviated as `lein`, is the de facto standard for creating Clojure projects.
Installing `lein` was dead simple: download the script, put it in your `$PATH`, and run it.
That's the kind of installation experience that every tool should strive for.
`lein` installs all of the components that it needs when it's invoked, so the first startup was a bit slower than subsequent ones.
However, five minutes after finding the link to the install script, I was able to type `lein repl` and get a running session.
The REPL is one of Clojure's best features, and one that I had missed from when I was writing Ruby.
My primary language these days is Go. There are a few Go REPLs out there, but none of them have the first-class language integration of a Ruby, Python, or Clojure.
I had forgotten how nice it is to have an idea, throw it into the REPL, and work through it interactively.
However, it'd be a bit much to write a whole web service in a REPL session, so I needed to figure out how to compile Clojure.
Again, `lein` makes this really easy: simply type `lein new` and you're presented with a folder structure where you can begin to fill in the parts of your project.
This is an area where I personally wish Go was more opinionated.
Folder structure can be one of the biggest bike sheds in software engineering, and often the only important quality about a folder structure is consistency.
Go does a good job of avoiding bike sheds on the whole by keeping a minimal language syntax, but this is a major blind spot for it.
I'd love to be able to type `go new` and get some standard package structure.
While I enjoyed the experience that `lein new` provides, I found it a bit peculiar that it includes an Eclipse Publice License in your project by default.
I'm sure that there's some interesting history there, but I still found it a bit strange.

After marveling at my newly generated folders, I went about writing my first Clojure program.
My editor setup at the time of this experiment was NeoVim backed by Conquer of Completion (COC), a runtime for the Language Server Protocol that backs VSCode.
(For the curious, I've since begun using Doom Emacs, and it's likely that I'll stick with it as my daily driver from now on).
It became clear pretty quickly that Emacs is the preferred editor for writing Clojure, and while the installation process for the Clojure language server was easy enough, it never really felt like an integrated tool the way that something like `ts-server` does.
But this wouldn't be the first time I've fought with my editor on a new language, and so I soldiered on to write my first Clojure program in all its glory:

```clojure
(ns fbaas.core)

(println "Hello, world!")
```

I ran the program with `lein run`, and we were off to the races.

## FizzBuzz (not yet as a service)

FizzBuzz is a nice problem for learning a new language because it's easy to write tests for it.
Even though the most obvious tests aren't very good tests in general, they're good to make sure that the test runner is working.
For now, it's enough to be able to test-drive a solution with tests like "give a number divisible by three and check that it comes back as fizz".

The process of writing tests for Clojure was absolutely delightful.
Here's the first test I wrote:

```clojure
; requires omited for brevity
(ns fbaas.core_test)

(deftest fizzbuzz
  (testing "numbers divisible by 3 but not 5 return fizz"
    (is (= (fizz-buzz 3) "fizz"))))
```

Come on, that's beautiful.
You define a test group with the `deftest` macro, give it a doc string with `testing`, and then write your assertions.
No complex boilerplate, no overriding the behavior of `main` so that your test runner is invoked, no inheriting from a magical base class.
The test code looks and feels like the code it's testing, and the `testing` function can be arbitrarily nested for RSpec-style "when" blocks.

Unfortunately, while writing this test was a nice introduction to what I've heard described as "the joy of Clojure," it also introduced me to the one of Clojure's downsides: the JVM startup time.
One of the things that Go excels at is fast compilation and startup, and I was sorely missing that here.
Running `lein test` felt like it took forever to give me feedback.
I'm guessing that there's a step I missed in the setup that professional Clojure programmers use that starts a long-running JVM process to avoid this or something.
To Clojure's credit, I was still excited to keep going.
Historically, most experiments I've done with languages that run on the JVM (especially Java itself) have lasted a short time before I hit some tooling issue and got too frustrated to continue.
I stubbornly refuse to let a programming language dictate what editor I use, and given that the fix for a lot of Java tooling problems is tied to rebuilding indexes in an IDE, I basically don't touch JVM languages unless I'm being paid for it.
This was a much more positive experience for the JVM than I'd been used to, which I found pleasantly surprising even if the process was slower than I liked.

Getting a passing test was easy enough:

```clojure
(ns fbaas.core)

(defn fizz-buzz [x]
  "fizz")
```

I usually get skip the "just return the literal thing" part of test driven development, but in this case it was useful to make sure that my test runner was working.
I ran `lein test`, saw that my tests passed, and moved on to writing a basic test suite:

```clojure
(deftest fizzbuzz
  (testing "numbers divisible by 3 but not 5 return fizz"
    (is (= (fizz-buzz 3) "fizz")))
  (testing "numbers divisible by 5 but not 3 return buzz"
    (is (= (fizz-buzz 5) "buzz")))
  (testing "numbers divisible by both 3 and 5 return fizzbuzz"
    (is (= (fizz-buzz 15) "fizzbuzz")))
  (testing "numbers not divisible by 3 or 5 return themselves"
    (is (= (fizz-buzz 1) "1"))))
```

And a straightforward implementation:

```clojure
(defn fizz-buzz [x]
  (cond
    (= (mod x 15) 0) "fizzbuzz"
    (= (mod x 3) 0) "fizz"
    (= (mod x 5) 0) "buzz"
    :else (str x)))
```

For whatever reason, at some point in my life I came to the conclusion that repeating the test for divisibility by 15 was bad.
The more "optimal" solution is to only do the tests for divisibility by three and five and append to an empty string;
If the string is empty at the end of the function, return the string representation of the input.
I decided to give that a shot in Clojure and came up with this:

```clojure
(defn fizz-buzz [x]
   (def msg "")
   (if (= (mod x 3) 0) (def msg (str msg "fizz"))
   (if (= (mod x 5) 0) (def msg (str msg "buzz")))
   (if (= msg "") (def msg (str x)))
   msg)
```

I was a bit taken aback when I finished it.
Why would my optimal solution look so... bad?
I'm sure that my lack of proficiency in the langauge is to blame.
Someone who knew what they were doing could make that look better, maybe by modeling it as a sequence of transformations on a string or something.
But more importantly, Clojure pushes you towards not mutating data.
Overall, I think that's actually one of its best properties.
One of the most important things about a language isn't what you _can_ do in it, [but what it makes easy](https://nibblestew.blogspot.com/2020/03/its-not-what-programming-languages-do.html).
Turing-completeness means you can write and evaluate almost any program, so at some point what you "can" do in a language becomes a meaningless distinction.
On a more practical level, you're rarely going to reach for the dark corners of a language in your day-to-day usage of it.
You'll do what the language makes easy, because you have stuff to get done, and life is too short to fight with a compiler.
Another thing Clojure shepherds you into doing is composing a program out of small functions.
So while I couldn't over engineer a solution that mutated a string, I could still over engineer a solution out of small functions:

```clojure
(defn fizzy? [x]
  "fizzy? returns whether a number is divisble by three"
  (= (mod x 3) 0))

(defn buzzy? [x]
  "buzzy? returns whether a number is divisible by five"
  (= (mod x 5) 0))

(defn fizzbuzzy? [x]
  "fizzbuzzy? returns whether a number is divisble by 15"
  (and (fizzy? x) (buzzy? x)))

(defn fizz-buzz [x]
  (cond
    (fizzbuzzy? x) "fizzbuzz"
    (fizzy? x) "fizz"
    (buzzy? x) "buzz"
    :else (str x)))
```

Two things to note about my silly over engineered version that wasn't in the original simple version.
First, each function includes a doc string, which is a wonderful thing to have in a language.
Second, Clojure function names can be very expressive.
Having worked in a large Ruby code base before, I feel pretty confident that allowing predicate functions (functions that check for some boolean value) to end with a question mark, mutative functions to end with an exclamation point, etc. are Good Things.

Now that I had a working FizzBuzz, it was time to do what security teams the world over fear most: hook it up to the internet.

## Adding web components

I was originally apprehensive about this part, because my experience with JVM languages and webservers has involved a lot of scary words like Servlet and Dispatch, and I wasn't really looking forward to writing that in a LISP.
Luckily, Clojure has two libraries--[http-kit](https://github.com/http-kit/http-kit) and [compojure](https://github.com/weavejester/compojure)--that make serving web traffic from Clojure a pleasant experience.

My first order of business when building a web server is usually to get to a working "/" route as quickly as possible.
This usually involves three steps: install dependencies, declare the route, and write a handler for it.

Adding dependencies with `lein` means adding them to a `project.clj` file.
Clojure dependencies are declared in Clojure, which I found to be a really nice paradigm.

After a short bit of research, I figured out that `compojure` is the piece that's used to declare routes, and `http-kit` is the piece that handles handlers.

Declaring a simple HTTP handler with `http-kit` is straightforward:

```clojure
(defn index [_]
  {:status 200
   :body "<h1>Welcome to FizzBuzz as a service!</h1>"
   :headers {"Content-Type" "text/html"}})
```

The handler is a just a Clojure function that takes a request (which I'm explicitly ignoring with the `_`) and returns a map.
It's hard to get much more straightforward than that.

Declaring the handler gave me high hopes that declaring routes would be similarly straightforward, but I honestly wasn't expecting to be actually delighted by it.
But, lo and behold, it turns out that `compojure` possesses my new favorite route declaration syntax:

```clojure
(defroutes routes
  (GET "/" [] index))
```

You declare a group of named routes, and each route is a function named after an HTTP method that takes a path, some arguments, and the handler to invoke.
The simple syntax benefits from Clojure's macro system.
Under the hood, `defroutes` and `GET` are generating more verbose functions.
This allows you to do Ruby-like metaprogramming, but in a much safer way since the code is generated at compile time instead of run time.

Including research time, I was able to go from zero to a running webserver in under 20 minutes.
That's quite a bit longer than Go, which has an HTTP server as part of its standard library, but still impressive.

Hooking the FizzBuzz code up was easy:

```clojure
; some dependencies omited for brevity
(ns fbaas.web
  (:require [fbaas.core :as c]))

(defn fizzbuzz [req]
  (let [params (:params req)
        num (edn/read-string (:num params))
        result (c/fizz-buzz num)]
    {:status 200
     :body result
     :headers {"Content-Type" "text/html"}})

(defroutes routes
  (GET "/fb/:num" [] fizzbuzz))
```

## JSONifying the responses

The last thing to do was to return JSON responses instead of plain text.
While the responses were simple enough that returning a formatted string using `printf` would have been reasonable, I wanted to see how Clojure does JSON serialization.
I was slightly apprehensive about this, because JSON serialization is an area that Go makes a little painful.
Luckily, Clojure's JSON serialization relies primarily on maps, and it proved to be painless to add a proper JSON response:

```clojure
(defn fizzbuzz [req]
  (let [params (:params req)
        num (edn/read-string (:num params))
        result (c/fizz-buzz num)
        body (json/write-str {:value result :input (:num params)})]
    {:status 200
     :body body
     :headers {"Content-Type" "application/json"}}))
```

The thing I found most surprising here was that there didn't seem to be an obvious "parse an int from a string" function that didn't involve dropping into the Java host language.
I settled on `edn/read-string`, but I get the sense that the `edn` package is a bit heavier than string parsing, and that it was more of a happy accident that that function happened to work here.

---

Overall I consider the experiment with Clojure successful, and will most likely use it for a bit of leisure programming in the future.

Some general thoughts on things I enjoyed:

- Doing configuration in the same language was really nice. I've gotten used to configuration being in an external language like YAML or JSON, so this felt really refreshing.
- Clojure's syntax is really expressive. Being able to write miniature DSLs and name methods with characters such as `!` and `?` is really powerful.
- `lein` is a really delightful tool

And some things I didn't care for:

- I found myself missing static types, but not as much as I usually do. I think this might have to do with the fact that Clojure isn't really a struct-based language, so types don't really help as much.
- The JVM startup time felt slow. I'm hoping that someone is working on a version of Clojure hosted in Rust or something.
- The VIM integration feels really second class. I actually switched to using emacs while writing this post, and the integration has felt much deeper. Most things Just Work.
- Some of the error messages, especially if you miss a paren, are really painful.
