#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    i = 0
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        new_string[i] == c
        i++

    return new_string
