#!/usr/bin/python3
# 1-rectangle.py
# Matt Krozel
'''
file creating class for rectangle
'''


class Rectangle:
    '''
    class rectangle defining tectange figure
    '''

    def __init__(self, width=0, height=0):
        '''
        init for rectangle
        '''

        self.__width = width
        self.__height = height

        @property
        def width(self):
            '''
            width of rectangle
            '''
            return self.__width

        @width.setter
        def width(self, value):
            '''
            width setter of rectangle
            '''
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            '''
            height of rectangle
            '''
            return self.__height

        @height.setter
        def height(self, value):
            '''
            height setter of rectangle
            '''
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
