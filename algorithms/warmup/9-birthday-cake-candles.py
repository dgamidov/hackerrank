#!/usr/bin/env python3


def birthdayCakeCandles(ar):
    age = max(ar)
    count = 0

    for item in ar:
        if item == age:
            count += 1

    return count


arr = [3, 2, 1, 3]
birthdayCakeCandles(arr)
