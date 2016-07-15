#!/usr/bin/env python

def bubble_sort(arr):
    """
    The bubble sort makes multiple passes through a list. It compares
    adjacent items and exchanges those that are out of order. Each pass
    through the list places the next largest value in its proper place.
    In essence, each item "bubbles" up to the location where it belongs.
    """
    pass

def reverse_bubble_sort(arr):
    """
    This is a reverse bubble which which bubbles smallest numbers to top
    for each loop.
    """
    # For a n-length array, (n-1) loop is needed.
    print "{: <16}: {}".format('Original array', arr)
    for i in range(len(arr)-1):
        # Each loop moves the smallest item to left.
        for j in range(len(arr)-1, i, -1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print "{: <16}: {}".format("After loop {}".format(i), arr)

if __name__ == '__main__':
    l = [144, 233, 5, 8, 21, 13, 55, 34, 89, 2, 3]
    reverse_bubble_sort(l)

    # Worse case
    ll = range(30, 10, -3)
    reverse_bubble_sort(ll)
