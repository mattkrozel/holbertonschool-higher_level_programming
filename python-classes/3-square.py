#!/usr/bin/python3
# 3-square.py
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
      
    def area(self):
        '''
        calculates and returns area of the square
        '''
        return self.__size ** 2
