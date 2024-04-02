#!/usr/bin/python3


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = length // 2
    peak = list_of_integers[mid]

    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
       (mid == length - 1 or peak >= list_of_integers[mid + 1]):
        return peak

    if mid > 0 and list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
