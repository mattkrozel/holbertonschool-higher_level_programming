#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    cache = dir(hidden_4)
    for name in cache:
        if name[0] != '_':
            print("{}".format(name))
