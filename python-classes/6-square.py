#!/usr/bin/python3
# 4-square.py
# Matt Krozel
'''
file creating class for square
'''


class Square:
    '''
    an empty class square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        initializing size and position of square
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''
        setter for size attribute
        '''
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print()
        else:
            for x in range(self.postion[1]):
                print()
            for x in range(self.size):
                for y in range(self.position[0]):
                    print(end="")
                for z in range(self.size):
                    print("#", end="")
                print()
