import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return [1, 2, 3]

###########
# Some clean versions so you can read what the hell I was doing...
###########

def bubblesort_clean(x):
    """
    this is just a version of the alg without the assignment- and 
    comparison- counting.

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
        assert x[i] <= x[i+1]
    return x

def quicksort_clean(x):
    print(x)
    """
    this is just a version of the alg without the assignment- and 
    comparison- counting.

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

########
# Okay, now some verisons where we're keeping track of assignments and
# comparisons.
########

def bubblesort(x):
    """
    A shell function so we can test without interacting with the
    counting.

    sort x by bubblesort: in each of x steps, iterate through the list,
    swapping elements if they're out of order.
    """
    return bubblesort_core(x)[0]

def bubblesort_core(x):
    """
    sort x by bubblesort. also, keep track of assignments and
    conditionals.
    """
    assignments = 0
    conditionals = 0
    # in X steps...
    for step in range(len(x)):
        # for each of the first X-step element pairs...
        for i in range(len(x)-1-step):
            # swap if they're out of order.
            conditionals += 1
            if x[i] > x[i+1]:
                assignments += 2
                x[i], x[i+1] = x[i+1], x[i]
    # then check. Not counting these.
    for i in range(len(x)-1):
        assert x[i] <= x[i+1]
    return x, conditionals, assignments

def quicksort(x):
    """
    A shell function so we can test without interacting with the
    counting.

    sort x by quicksort: pick a pivot element, divide the list into halves
    larger and smaller than the pivot, sort those, then recompose.
    """

    return quicksort_core(x)[0]

def quicksort_core(x):
    """
    sort x by quicksort. also, keep track of assignments and
    conditionals.
    """
    # we pass all assignments and conditionals below us in the
    # recursion tree "up".
    assignments = 0
    conditionals = 0
    conditionals += 1
    if len(x) <= 1:
        return (x, assignments, conditionals)
    # pick a pivot and partition indices. guess the middle, for the
    # kinda-sorted case. we store the pivot at the beginning.
    assignments += 3
    middle = len(x)//2
    x[0], x[middle] = x[middle], x[0]
    # partition: iterate in from both sides, ensuring that elements
    # less than the pivot are below the low iterator and elements
    # above the pivot are above the high iterator. When they cross,
    # we've partitioned.
    assignments += 3
    pivot = 0
    low = 1
    high = len(x)-1

    conditionals += 1 # first while
    while low <= high:
        conditionals += 4 # every other while and three ifs
        if x[low] > x[pivot] and x[high] <= x[pivot]:
            # We can swap these elements.
            assignments += 2
            x[low], x[high] = x[high], x[low]
        # Otherwise, just move iterators closer if we can.
        if x[low] <= x[pivot]: 
            assignments += 1
            low += 1
        if x[high] > x[pivot]: 
            assignments += 1
            high -= 1
    # recurse.
    # What I'm doing here is a bit of a kludge. This was written with
    # vanilla python lists in mind, but it doesn't work for numpy
    # arrays. Splicing a vanilla list creates a (deep) copy of that
    # list, while splicing a numpy array creates a new variable name
    # that points to the same object in memory. i.e.:
    # 
    # >>> A = [1, 2, 3]
    # >>> B = A[1:]
    # >>> B[1] = 5
    # >>> A
    # [1, 2, 3]
    # # but
    # >>> a = np.array([1, 2, 3])
    # >>> b = a[1:]
    # >>> b[1] = 5
    # >>> a
    # array([1, 2, 5])
    # 
    # To keep things simple, we just cast as a list and keep passing
    # things around. If I'd thought carefully about this inconvenience
    # between cases, I'd probably have started with a deep copy
    # approach and passed indices instead of sublists.
    lower = list(x[1:low])
    higher = list(x[low:])
    below = quicksort_core(lower)
    above = quicksort_core(higher)
    return (below[0] + [x[pivot]] + above[0], below[1] + above[1] + assignments, below[2] + above[2] + conditionals)

