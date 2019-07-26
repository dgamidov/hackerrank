#!/usr/bin/env python3


# a = [17, 28, 30]
# b = [99, 16, 8]

a = [5, 6, 7]
b = [3, 6, 10]

result = [0, 0]

for index, a_value in enumerate(a):
    # print("{} {} {}".format(index, a_value, b[index]))

    b_value = b[index]

    if a_value == b_value:
        continue
    elif a_value > b_value:
        result[0] += 1
    else:
        result[1] += 1

print(result)
