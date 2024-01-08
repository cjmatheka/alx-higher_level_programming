#!/usr/bin/python3

# Function for replacing an element in a list
def replace_in_list(my_list, idx, element):

    # if the index is negative or out of range
    if idx < 0 and idx >= len(my_list):
        return my_list

    # If the index is positive and in range
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list