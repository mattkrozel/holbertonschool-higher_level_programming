#!/usr/bin/python3
# rectangle.py
# Matt Krozel

'''
file creating a rectangle class
'''
from models.base import Base


class Rectangle(Base):
    '''
    rectangle class as a subclass of base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        initilizaing super id, orivate width, ehight, x, and y
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
