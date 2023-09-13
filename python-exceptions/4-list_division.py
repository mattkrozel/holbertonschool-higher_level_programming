#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    finallist = []
    res = 0
    for i in range(0, list_length):
        try:
            res = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("Wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            finallist.append(res)
    return (finallist)
