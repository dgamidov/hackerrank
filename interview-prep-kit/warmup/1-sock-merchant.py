#!/usr/bin/env python3


def sockMerchant(n, ar):
    result = 0
    temp = {}

    for color in ar:
        if color in temp:
            if temp[color] == 1:
                result += 1
                temp[color] = 0
            else:
                temp[color] += 1
        else:
            temp[color] = 1

    return result


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(n, ar))
