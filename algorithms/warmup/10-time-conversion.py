#!/usr/bin/env python3


def timeConversion(s):
    day_part = s[-2:]
    time = s[:-2].split(":")

    for index, item in enumerate(time):
        time[index] = int(item)

    if day_part == "AM":
        if time[0] == 12:
            time[0] = 0

    if day_part == "PM":
        if time[0] != 12:
            time[0] += 12

    for index, item in enumerate(time):
        time[index] = str(item).rjust(2, "0")

    result = ":".join(time)

    return result


s = "07:05:45PM"
print(timeConversion(s))

s = "12:00:00AM"
print(timeConversion(s))
