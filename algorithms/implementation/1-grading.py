#!/usr/bin/env python3

from math import ceil


def gradingStudents(grades):
    result = []

    for grade in grades:
        if grade >= 38:
            next_multiply_of_5 = ceil(grade / 5) * 5
            if next_multiply_of_5 - grade < 3:
                grade = next_multiply_of_5

        result.append(grade)

    return result


grades = [73, 67, 38, 33]
gradingStudents(grades)
