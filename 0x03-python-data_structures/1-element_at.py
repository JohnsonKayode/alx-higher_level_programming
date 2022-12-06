#!/usr/bin/python3

def element_at(my_list, idx):
    s = len(my_list)
    if idx < 0:
        return None
    if idx > s:
        return None
    else:
        return my_list[idx]
