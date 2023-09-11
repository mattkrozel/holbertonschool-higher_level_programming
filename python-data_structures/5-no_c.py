#!/usr/bin/python3
def no_c(my_string):
    finalstring = ""
    for x in my_string:
        if x not in "Cc":
            finalstring = finalstring + x
        return (finalstring)
