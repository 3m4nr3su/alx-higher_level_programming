#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    my_list = list()
    new_list = list()
    if length == 0:
        first = None
    else:
        for char in sentence:
            my_list.append(char)
        first = my_list[0]
    new_list.append(length)
    new_list.append(first)
    new_tuple = tuple(new_list)
    return new_tuple
