#!/usr/bin/python3
# 3-is_kind_of_class.py
# Matt Krozel

def is_kind_of_class(obj, a_class):
    '''
    check type of class and inherited class
    '''
    if isinstance(obj, a_class):
        return True
    return False
