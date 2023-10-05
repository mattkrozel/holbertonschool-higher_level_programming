#!/usr/bin/python3
# square.py
# Matt Krozel

'''
defines a square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    represents square
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        inntilizinng new square
        '''
        super().__init(size, size, x, y, id)
