#!/usr/bin/python3
for combination in range(0, 100):
    if (combination / 10) >= (combination % 10):
        continue
    elif combination == 89:
        print("{:02}".format(combination))
        break
    print("{:02}".format(combination), end=", ")
