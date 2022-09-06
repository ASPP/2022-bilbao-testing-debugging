def local_maxima(x):
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
    n = len(x)

    rv = [i for i in range(n)
          if i==0 and x[i] > x[i+1]
          or i==(n-1) and x[i-1] < x[i]
          or 0<i<n and x[i-1] <= x[i] >= x[i+1]
          ]

    return rv
