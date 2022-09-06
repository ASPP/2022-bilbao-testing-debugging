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
    max_ls = []
    for i in range(len(x)):
        if i ==0:
            if x[i] > x[i+1]:
                max_ls.append(i)        
        elif i == len(x)-1:
            if x[i] > x[i-1]:
                max_ls.append(i)
        else:
            if x[i] >= x[i+1] and x[i] >= x[i-1]:
                max_ls.append(i)
    return max_ls 



    

