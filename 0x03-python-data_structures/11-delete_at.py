#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 > idx or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        del new_list[idx]
        return new_list
