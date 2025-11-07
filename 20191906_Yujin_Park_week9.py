import os
import sys


cmd = []
scores = [78]

for score in scores:

    print("Grade : ", end='')
    if score >= 95:
        print("A+")
    elif score >= 90 and score < 95:
        print("A")
    elif score >= 80 and score < 90:
        print("B+")
    elif score >= 75 and score < 80:
        print("B")
    elif score >= 70 and score < 75:
        print("C+")
    elif score >= 65 and score < 70:
        print("C")
    elif score >= 60 and score < 65:
        print("D+")
    elif score >= 55 and score < 60:
        print("D")
    else:
        print("F")


