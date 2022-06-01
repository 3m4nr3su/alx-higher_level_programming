#!/usr/bin/python3
def uppercase(str):
    word = ''
    for i in range(len(str)):
        if (str[i] >= 'a' and str[i] <= 'z'):
            char = chr(ord(str[i]) - 32)
            word = word + char
        else:
            word = word + str[i]
    print("{}".format(word), end="\n")
