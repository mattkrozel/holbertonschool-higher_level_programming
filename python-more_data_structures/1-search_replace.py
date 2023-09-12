#!/usr/bin/python3
def search_replace(my_list, search, replace):
    finallist = my_list[:]
    for i in range(len(finallist)):
        if finallist[i] == search:
            finallist[i] = replace
    return (finallist)
