#!/usr/bin/python3
for i1 in range(97, 123):
    if chr(i1) == 'q' or chr(i1) == 'e':
        continue
    print(chr(i1).format(i1), end='')
