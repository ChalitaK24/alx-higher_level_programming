#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper = upper + "{}".format(chr(ord(c) - 32))
        else:
            upper = upper + "{}".format(c)
    print("{}".format(upper))
