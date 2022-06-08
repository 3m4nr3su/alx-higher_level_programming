#!/usr/bin/python3
def weight_average(my_list=[]):
    while (len(my_list) == 0):
        return 0
    add, weight = 0, 0
    for n in my_list:
        add = add + (n[0] * n[1])
        weight = weight + n[1]
    return add / weight
