#!/usr/bin/python3


def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    mid = length // 2
    if (mid == length - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]) and \
       (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    elif mid != 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
