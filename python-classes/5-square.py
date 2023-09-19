#!/usr/bin/python3
# 5-square.py
# Matt Krozel
'''
file creating class for square
'''


class Square:
    '''
    an empty class square
    '''

    def __init__(self, size=0):
        '''
        initializing size of square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''
        gets size of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        calculates and returns area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        prints in stdout the square with # characters
        '''
        if self.__size == 0:
            print("")
        for x in range(self.__size):
            for y in range(self.size):
                print("#", end="")
            print("")
