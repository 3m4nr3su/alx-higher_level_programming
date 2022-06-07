#!/usr/bin/python3
def max_integer(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
        if count == 0:
            return None
        my_list.sort()
        return my_list[-1]
