#!/usr/bin/env python

def find_max_index(arr):
    """
    Returns index of the max element in an array.
    """
    i = 0
    for j in range(1, len(arr), 1):
        if arr[i] < arr[j]:
            i = j
    return i

def selection_sort(arr):
    """
    The selection sort improves on the bubble sort by making only one exchange
    for every pass through the list. In order to do this, a selection sort
    looks for the largest value as it makes a pass and, after completing the
    pass, places it in the proper location.
    """
    print "{: <16}: {}".format('Original array', arr)
    length = len(arr)
    for i in range(length-1, 1, -1):
        # Note arr[0:3] returns [arr[0], arr[1], arr[2]] with arr[3] excluded.
        max_index = find_max_index(arr[0:i+1])
        arr[i], arr[max_index] = arr[max_index], arr[i]
        print "{: <16}: {}".format("After loop {}".format(i), arr)

if __name__ == '__main__':
    l = [144, 233, 5, 8, 21, 13, 55, 34, 89, 2, 3]
    selection_sort(l)

