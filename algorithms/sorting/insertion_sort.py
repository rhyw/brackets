#!/usr/bin/env python

def insertion_sort(arr):
    """
    Insertion sort always maintains a sorted sublist in the lower positions of
    the list. Each new item is then "inserted" back into the previous sublist
    such that the sorted sublist is one item larger. 
    """

    print "{: <16}: {}".format('Original array', arr)
    for i in range(1, len(arr), 1):
        # pos is the current index of the passnum.
        pos = i
        for j in range(i-1, -1, -1):
            if arr[j] > arr[pos]:
                arr[pos], arr[j] = arr[j], arr[pos]
                pos = j
        print "{: <16}: {}".format("After loop {}".format(i), arr)

if __name__ == '__main__':
    l = [144, 233, 5, 8, 21, 13, 55, 34, 89, 2, 3]
    insertion_sort(l)

