#!/usr/bin/python3
from sys import argv
p = 0
for n in argv[1:]:
    p += int(n)
print("{:d}".format(p))
