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

    @property
    def width(self):
        '''
        gets width of rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter func for width
        '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''
        gets height of rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        setter func for height
        '''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''
        gets x coordinates
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        setter func for x
        '''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''
        gets y coordinates
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        setter func for y
        '''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''
        returns area of rectangle
        '''
        return (self.__width * self.__height)
