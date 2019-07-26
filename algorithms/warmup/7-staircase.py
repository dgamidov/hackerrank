#!/usr/bin/env python3


def staircase(n):
    result = []

    step = n

    while step:
        item = "#" * step
        result.append(item.rjust(n, " "))
        step -= 1

    result.reverse()

    for item in result:
        print(item)


n = 10
staircase(n)
