#!/usr/bin/python3
from add_0 import add as add1
a = 1
b = 2
if __name__ == "__main__":
    print('{:d} + {:d} = {:d}'.format(a, b, add1(a, b)))
