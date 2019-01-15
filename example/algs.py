import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return [1, 2, 3]

def bubblesort(x):
    """
    sort x by bubblesort: in each of x steps, iterate through the list,
    swapping elements if they're out of order.
    """
    # in X steps...
    for step in range(len(x)):
        # for each of the first X-step element pairs...
        for i in range(len(x)-1-step):
            # swap if they're out of order.
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    # then check:
    for i in range(len(x)-1):
        assert x[i] < x[i+1]
    return x

def quicksort(x):
    print(x)
    """
    sort x by quicksort: pick a pivot element, divide the list into halves
    larger and smaller than the pivot, sort those, then recompose.
    """
    if len(x) <= 1:
        return x
    # pick a pivot and partition indices. guess the middle, for the
    # kinda-sorted case. we store the pivot at the beginning.
    middle = len(x)//2
    x[0], x[middle] = x[middle], x[0]
    # partition: iterate in from both sides, ensuring that elements
    # less than the pivot are below the low iterator and elements
    # above the pivot are above the high iterator. When they cross,
    # we've partitioned.
    pivot = 0
    low = 1
    high = len(x)-1
    while low <= high:
        if x[low] > x[pivot] and x[high] <= x[pivot]:
            # We can swap these elements.
            x[low], x[high] = x[high], x[low]
        # Otherwise, just move iterators closer if we can.
        if x[low] <= x[pivot]: low += 1
        if x[high] > x[pivot]: high -= 1
    # recurse.
    return quicksort(x[1:low]) + [x[pivot]] + quicksort(x[low:])

