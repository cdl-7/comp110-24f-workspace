"""Exercise 04 List Utils"""

__author__ = "730742183"


def all(num_list: list[int], num: int) -> bool:
    # Returns True is all nums in list are the same
    i = 0
    while i < len(num_list):
        if num_list[i] != num:
            # Returns False is there is a diff num
            return False
        i += 1
    return True


def max(num_list: list[int]) -> int:
    # Returns the maximum value in the list
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty list")
    max_num = 0
    i = 0
    while i < len(num_list):
        if num_list[i] > max_num:
            max_num = num_list[i]
        i += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    # Returns True is both lists are identical
    i = 0
    if len(list1) != len(list2):
        # Returns False is the lists are diff lengths
        return False
    while i < len(list1):
        if list1[i] != list2[i]:
            # Returns False is an index is different
            return False
        i += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    # Appends each idx of list2 to the end of list1
    i = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
    return None
