#!/usr/bin/env python3


def diagonalDifference(arr):
    first = 0
    second = 0

    arr_max_index = len(arr) - 1

    for index, row in enumerate(arr):
        step = 0

        for item in row:
            if index == step:
                first += item

            if index == arr_max_index - step:
                second += item

            step += 1

    result = abs(first - second)

    return result


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))
