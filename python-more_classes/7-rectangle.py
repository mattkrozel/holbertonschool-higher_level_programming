#!/usr/bin/python3
# 7-rectangle.py
# Matt Krozel
'''
file creating class for rectangle
'''


class Rectangle:
    '''
    class rectangle defining tectange figure
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        init for rectangle
        '''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''
        str medthod to print restangle
        '''
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for x in range(self.__height):
            for y in range(self.__width):
                string += str(self.print_symbol)
            if x < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        '''
        repr method for object t=rectangle
        '''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''
        delete method for rectangle
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        calculates area of rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        calulates perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
