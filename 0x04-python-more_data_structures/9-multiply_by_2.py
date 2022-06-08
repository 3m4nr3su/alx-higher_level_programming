#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_values = a_dictionary.values()
    dict_keys = a_dictionary.keys()
    multi_list = list()
    new_dict = dict()
    for no in dict_values:
        num = no * 2
        multi_list.append(num)
    for key in dict_keys:
        for val in multi_list:
            new_dict[key] = val
    return new_dict
