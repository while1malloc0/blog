#!/usr/bin/env python3

import sys


def main():
    path = sys.argv[1]
    with open(path) as f:
        content = f.readlines()

    tweets = []
    tweet = []
    for (i, line) in enumerate(content):
        if line.startswith("#"):
            tweets.append("".join(tweet))
            line = line.replace("#", "")
            tweet = [line]
            continue

        tweet.append(line)
        tmp = "".join(tweet)
        if len(tmp) > 280:
            tweet.pop()
            tweets.append("".join(tweet))
            tweet = [line]

    for (i, tweet) in enumerate(tweets):
        tweet = tweet.replace("\n", " ")
        tweet = tweet.strip()
        print(tweet)
        print("---")


if __name__ == "__main__":
    main()
