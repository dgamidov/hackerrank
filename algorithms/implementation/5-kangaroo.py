#!/usr/bin/env python3


def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        abs_speed = v1 - v2
        abs_position = x2 - x1

        if abs_position % abs_speed == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
