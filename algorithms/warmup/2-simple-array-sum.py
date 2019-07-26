#!/usr/bin/env python3


from functools import reduce


def simpleArraySum(ar):
    result = reduce(lambda acc, item: acc + item, ar)
    return result
