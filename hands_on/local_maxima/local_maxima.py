import numpy as np
from typing import Union
from numpy.typing import NDArray
import sys

def find_maxima(numbers: Union[list, NDArray]):
    """Find local maxima of x.
    Example:
    >>> x = [1, 3, -2, 0, 2, 1]
    >>> find_maxima(x)
    [1, 4]
    If in a local maximum several elements have the same value,
    return the left-most index.
    Example:
    >>> x = [1, 2, 2, 1]
    >>> find_maxima(x)
    [1]
    Input arguments:
    x -- 1D list of real numbers
    Output:
    idx -- list of indices of the local maxima in x
    """
    max_idxs = []
    for ni, num in enumerate(numbers[:-1]):
        if ni == 0:
            pass
        elif (numbers[ni+1] <= num and numbers[ni-1] < num):
            max_idxs.append(ni)

    return max_idxs

if __name__ == '__main__':
    numbers = np.array(sys.argv[1:], dtype=np.int_)
    max_idxs = find_maxima(numbers)
    print(max_idxs)


