#!/usr/bin/python3
def print_last_digit(num):
    last_dig = abs(num) % 10
    print(last_dig, end="")
    return last_dig
