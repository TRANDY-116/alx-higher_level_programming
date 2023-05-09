#!/usr/bin/python3
for letter in range(ord("a"), ord("z") + 1):
    # converting the codes in ASCII to characters
    mini_letters = chr(letter)

    if mini_letters == "q" or mini_letters == "e":
        continue

    print(mini_letters, end=" ")
