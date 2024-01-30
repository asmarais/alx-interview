#!/usr/bin/python3


def validUTF8(data):
    """check if a given dataset is a valid UTF-8 encoding"""
    test = True
    for ele in data:
        if ele >= 0 and ele <= 127:
            test = True
        elif ele >= 192 and ele <= 255:
            test = True
        else:
            test = False
    if test:
        return True
    return False
