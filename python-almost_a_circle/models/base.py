#!/usr/bin/python3
# base.py
# Matt Krozel


class Base:
    '''
    base model, respresents base for all other classes

    private class attributes, number of instantiated bases
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        initilizing new base
        args are identity of new base
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
