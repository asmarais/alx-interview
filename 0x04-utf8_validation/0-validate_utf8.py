#!/usr/bin/python3


def validUTF8(data):
    """check if a given dataset is a valid UTF-8 encoding"""
    test = True
    for ele in data:
        if ele > 127 and ele < 192:
            test = False
        if ele > 255:
            test = False
    if test == False:
        return False
    return True
