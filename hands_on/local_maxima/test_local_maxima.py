from local_maxima import find_maxima


def test_find_maxima():
    values = [1, 3, -2, 0, 2, 1]
    expected = [1, 4]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_negative():
    values = [-1, -1, 0, -1]
    expected = [2]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_edges():
    values = [4, 2, 1, 3, 1, 5]
    expected = [3]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau():
    values = [1,2,2,3,4,4,2]
    expected = [1,4]
    maxima = find_maxima(values)
    assert maxima == expected
 
