#!/usr/bin/env python3


def plusMinus(arr):
    temp = [0, 0, 0]
    denominator = len(arr)

    for i in arr:
        if i > 0:
            temp[0] += 1
        elif i < 0:
            temp[1] += 1
        else:
            temp[2] += 1

    for item in temp:
        print(str(round(item / denominator, 6)).ljust(8, '0'))


arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))
