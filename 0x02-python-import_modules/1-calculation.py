#!/usr/bin/python3
from calculator_1 import (
        add, sub, mul, div
)

if __name__ == "__main__":
    c = 10
    b = 5
    print("{} + {} = {}".format(c, b, add(c, b)))
    print("{} - {} = {}".format(c, b, sub(c, b)))
    print("{} * {} = {}".format(c, b, mul(c, b)))
    print("{} / {} = {}".format(c, b, div(c, b)))
