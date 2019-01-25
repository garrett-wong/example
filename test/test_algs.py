import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)
    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))
    # generate a new random vector of length 10
    x = np.random.rand(10)
    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # test some known list
    x = [1,2,4,0,1]
    assert np.array_equal(algs.bubblesort(x), np.array([0, 1, 1, 2, 4]))
    # check on zero- and one-length input
    x = []
    assert np.array_equal(algs.bubblesort(x), x)
    x = [1]
    assert np.array_equal(algs.bubblesort(x), x)
    # check on even- and odd-length input
    x = np.random.rand(10)
    assert np.array_equal(algs.bubblesort(x), sorted(x))
    x = np.random.rand(9)
    assert np.array_equal(algs.bubblesort(x), sorted(x))
    # check on repeats
    x = np.random.randint(0, 3, 10)
    assert np.array_equal(algs.bubblesort(x), sorted(x))
    x = [1] * 10
    assert np.array_equal(algs.bubblesort(x), x)
    # check on only strings. sort by ascii order, as in canonical sort.
    x = ["a", "B", "A", "b"]
    assert np.array_equal(algs.bubblesort(x), sorted(x))
    # check that mixed strings throws a TypeError.
    try:
        x = ["1", 1]
        algs.bubblesort(x)
    except TypeError:
        pass
    else:
        assert False

def test_quicksort():
    # test some known list
    x = [1,2,4,0,1]
    assert np.array_equal(algs.quicksort(x), np.array([0, 1, 1, 2, 4]))
    # check on zero- and one-length input
    x = []
    assert np.array_equal(algs.quicksort(x), x)
    x = [1]
    assert np.array_equal(algs.quicksort(x), x)
    # check on even- and odd-length input
    x = np.random.rand(10)
    assert np.array_equal(algs.quicksort(x), sorted(x))
    x = np.random.rand(9)
    assert np.array_equal(algs.quicksort(x), sorted(x))
    # check on repeats
    x = np.random.randint(0, 3, 10)
    assert np.array_equal(algs.quicksort(x), sorted(x))
    x = [1] * 10
    assert np.array_equal(algs.quicksort(x), x)
    # check on only strings. sort by ascii order, as in canonical sort.
    x = ["a", "B", "A", "b"]
    assert np.array_equal(algs.quicksort(x), sorted(x))
    # check that mixed strings throws a TypeError.
    try:
        x = ["1", 1]
        algs.quicksort(x)
    except TypeError:
        pass
    else:
        assert False

