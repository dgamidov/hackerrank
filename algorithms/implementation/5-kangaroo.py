#!/usr/bin/env python3


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    if v2 >= v1:
        return "NO"
    else:
        speed = v1 - v2
        position = x2 - x1

        if position % speed == 0:
            return "YES"
        else:
            return "NO"

print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
