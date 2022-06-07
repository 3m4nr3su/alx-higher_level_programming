#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = tuple()
    my_list_c = list(tuple_c)
    my_list_b = list(tuple_b)
    my_list_a = list(tuple_a)
    while len(my_list_a) < 2 or len(my_list_b) < 2:
        my_list_a.append(int(0))
        my_list_b.append(int(0))
    first_num = my_list_a[0] + my_list_b[0]
    second_num = my_list_a[1] + my_list_b[1]
    my_list_c.append(first_num)
    my_list_c.append(second_num)
    tuple_c = tuple(my_list_c)
    return tuple_c
