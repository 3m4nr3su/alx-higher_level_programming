#!/usr/bin/python3
def best_score(a_dictionary):
    dict_values = a_dictionary.values()
    dict_keys = a_dictionary.keys()
    sorted_values = sorted(dict_values)
    for key in dict_keys:
        if a_dictionary[key] is None:
            return None
        elif a_dictionary[key] == sorted_values[-1]:
            return key
        else:
            continue
