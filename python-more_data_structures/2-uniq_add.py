#!/usr/bin/python3
def uniq_add(my_list=[]):
   uniqsum = set()
   if my_list:
       for item in my_list:
           uniqsum.append(item)
    return sum(uniqsum)
