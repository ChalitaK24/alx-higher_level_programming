#!/usr/bin/python3
def pow(a, b):
    res = 1
    for _ in range(abs(b)):
        res = res * a
    if b < 0:
        res = 1 / res
    return res
