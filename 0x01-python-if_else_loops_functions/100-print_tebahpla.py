#!/usr/bin/python3
for in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 0:
        add = 0
    else:
        add = 32
    a = chr(i - add)
    print('{}'.format(a), end='')
