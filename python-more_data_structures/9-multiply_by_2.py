#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    if a_dictionary:
        for key, val in a_dictionary.items():
            result.update({key: val * 2})
        return (result)
