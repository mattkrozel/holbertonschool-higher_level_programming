#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqsum = 0
    for item in set(my_list):
        uniqsum = item + uniqsum
    return (uniqsum)
