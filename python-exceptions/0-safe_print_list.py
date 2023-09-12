#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elemprinted = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elemprinted += 1
        except:
            continue
    print()
    return (elemprinted)
