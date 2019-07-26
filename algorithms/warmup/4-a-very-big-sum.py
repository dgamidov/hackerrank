#!/usr/bin/env python3

from functools import reduce


def aVeryBigSum(ar):
    result = reduce(lambda acc, x: acc + x, ar)
    return result


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(aVeryBigSum(ar))
