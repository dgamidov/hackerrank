#!/usr/bin/env python3


def countingValleys(n, s):
    level = 0
    path = [0]

    for letter in s:
        if letter == "D":
            level -= 1
        else:
            level += 1

        path.append(level)

    result = 0

    # print(s)
    # print(path)

    for index, value in enumerate(path):
        if value == 0:
            if index < len(path) - 1:
                if path[index + 1] < 0:
                    result += 1

    return result


n = 8
s = "UDDDUDUU"
print(countingValleys(n, s))

n = 12
s = "DDUUDDUDUUUD"
print(countingValleys(n, s))
