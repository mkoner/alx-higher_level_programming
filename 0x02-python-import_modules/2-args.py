#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments")
    elif len(sys.argv) == 1:
        print("1 arguments:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(2, len(sys.argv) + 1):
            print("{:d}: {}".format(i - 1, sys.argv[i - 1]))
