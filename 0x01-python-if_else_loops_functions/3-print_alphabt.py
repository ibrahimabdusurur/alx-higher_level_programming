#!/usr/bin/python3
for letters in range(97, 123):
    if letters == 113 or letters == 101:
        continue
    print("{}".format(chr(letters)), end="")
