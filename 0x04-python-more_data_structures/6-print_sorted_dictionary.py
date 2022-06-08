#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = a_dictionary.keys()
    dict_values = a_dictionary.values()
    sorted_keys = sorted(dict_keys)
    new_dictionary = dict()
    for key in sorted_keys:
        for val in dict_values:
            if a_dictionary[key] == val:
                print("{}: {}".format(key, a_dictionary[key]))
