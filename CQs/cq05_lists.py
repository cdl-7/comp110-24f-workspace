"""Mutating functions."""

__author__ = "730742183"


def manual_append(list: list[int], num: int) -> None:
    list.append(num)


def double(input_list: list[int]) -> None:
    i = 0
    while i < len(input_list):
        input_list[i] = input_list[i] * 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
