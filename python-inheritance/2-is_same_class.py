#!/usr/bin/python3
# 2-is_same_class.py
# Matt Krozel

'''
checking if object is instance of class
'''


def is_same_class(obj, a_class):
    '''
    if instance, returns true, else false
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
