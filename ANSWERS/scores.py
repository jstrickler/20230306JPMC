#!/usr/bin/env python
from gradeutil import get_letter_grade

FILE_PATH = "../DATA/testscores.dat"

def main():
    data = read_data()

    for student, score in sorted(data.items()):
        print("{:20s} {} {}".format(student, score, get_letter_grade(score)))


def read_data():
    scores_by_student = {}

    with open(FILE_PATH) as scores_in:
        for line in scores_in:
            name, score = line.split(":")
            score = int(score)
            scores_by_student[name] = score

    return scores_by_student


main()