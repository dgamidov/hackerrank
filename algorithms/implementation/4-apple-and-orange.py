#!/usr/bin/env python3


def countApplesAndOranges(s, t, a, b, apples, oranges):
    result = {"apples": 0, "oranges": 0}

    for apple in apples:
        location = apple + a
        # print("location: {}".format(location))
        if location >= s and location <= t:

            result["apples"] += 1

    for orange in oranges:
        location = orange + b
        # print("location: {}".format(location))
        if location >= s and location <= t:
            result["oranges"] += 1

    print(result["apples"])
    print(result["oranges"])


s = 7
t = 11
a = 5
b = 15

apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)
