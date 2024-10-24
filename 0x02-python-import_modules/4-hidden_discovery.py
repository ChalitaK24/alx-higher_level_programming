#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    filtered_names = filter(lambda name:
                            not name.startswith("__"), dir(hidden_4))

    for name in sorted(filtered_names):
        print(name)
