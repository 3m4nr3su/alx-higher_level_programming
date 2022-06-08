#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(my_list)
    count = 0
    for num in n_list:
        if num == search:
            n_list[count] = replace
        count = count + 1
    return n_list
