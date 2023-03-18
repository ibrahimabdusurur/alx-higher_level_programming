#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers == 99:
        print("{}".format(numbers))
        break
    print("{:02}".format(numbers), end=", ")
