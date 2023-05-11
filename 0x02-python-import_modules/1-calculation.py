#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    c = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(c, b, add(c, b)))
    print("{:d} - {:d} = {:d}".format(c, b, sub(c, b)))
    print("{:d} * {:d} = {:d}".format(c, b, mul(c, b)))
    print("{:d} / {:d} = {:d}".format(c, b, div(c, b)))
