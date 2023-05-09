#!/usr/bin/python3
for number in range(0, 99 + 1):
    if number == 99:
        print(f"{number:2d}", end="\n")
    else:
        print(f"{number:2d}", end=",")
