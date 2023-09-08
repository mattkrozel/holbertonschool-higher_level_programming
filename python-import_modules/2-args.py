#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()
strarg = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    strarg += 's.'
elif argc == 1:
    strarg += ':'
else:
    strarg += 's:'
print(strarg.format(argc))

i = 0
for argument in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, argument))
    i += 1
