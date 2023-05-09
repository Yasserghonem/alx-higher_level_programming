#!/usr/bin/python3

def uppercase(str):
    for uch in str:
        if ord(uch) >= 97 and ord(uch) <= 122:
            uch = chr(ord(uch) - 32)
        print("{:s}".format(uch), end='')

    print('\n', end="")
