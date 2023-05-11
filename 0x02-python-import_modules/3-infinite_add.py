#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    sum = 0
    for x in argv:
        sum += int(x)
    print("{}".format(sum))
