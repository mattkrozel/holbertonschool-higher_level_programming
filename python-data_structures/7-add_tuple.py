#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lengtha = len(tuple_a)
    lengthb = len(tuple_b)
    result = ()
    for i in range(2):
        if i >= lengtha:
            a = 0
        else:
            a = tuple_a[i]
        if i >= lengthb:
            b = 0
        else:
            b = tuple_b[i]
        if (i == 0):
            result = (a + b)
        else:
            result = (result, a + b)
    return (result)
