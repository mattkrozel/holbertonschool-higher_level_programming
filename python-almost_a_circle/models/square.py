#!/usr/bin/python3
# square.py
# Matt Krozel

'''
file creating a rectangle class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    rectangle class as a subclass of base class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        initilizaing super id, orivate width, ehight, x, and y
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        gets width of rectangle
        '''
        return self.__width

    @size.setter
    def size(self, value):
        '''
        setter func for width
        '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        '''
        returns str format of rect
        '''
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''
        update rectangle
        assign key args to attributes
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

