#!/usr/bin/env python3


def miniMaxSum(arr):
    arr.sort()

    min_numbers = arr[:-1]
    max_numbers = arr[1:]

    print("{} {}".format(sum(min_numbers), sum(max_numbers)))


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
