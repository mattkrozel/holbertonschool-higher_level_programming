#!/usr/bin/python3
# 4-inherits_from.py
# Matt Krozel

'''
define a inherited class checking function
'''


def inherits_from(obj, a_class):
    '''
    check inherited instance of class
    '''
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
