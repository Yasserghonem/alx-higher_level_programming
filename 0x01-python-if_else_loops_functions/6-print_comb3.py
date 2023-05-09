#!/usr/bin/python3
for f in range(0, 8):
    for q in range(f + 1, 10):
        print("{:d}{:d}".format(f, q), end=', ')
print("{:d}{:d}".format(f + 1, q))
