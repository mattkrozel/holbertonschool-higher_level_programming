#!/bin/usr/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    if a_dictionary:
        result = max(a_dictionary, key=a_dictionary.get)
        if result:
            return (result)
