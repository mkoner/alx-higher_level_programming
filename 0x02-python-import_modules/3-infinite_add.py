#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    result = 0
    if total == 1:
        print(0)
    else:
        for i in range(1, total):
            op = int(sys.argv[i])
            result = result + op
        print(result)
