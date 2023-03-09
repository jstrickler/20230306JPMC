#!/usr/bin/env python
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

def get_letter_grade(score):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    return grade

main()