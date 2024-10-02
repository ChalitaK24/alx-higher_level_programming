#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    n_args = len(argv) - 1

    if n_args == 0:
        print(f"{n_args} arguments.")
    elif n_args == 1:
        print(f"{n_args} argument:")
    else:
        print(f"{n_args} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
