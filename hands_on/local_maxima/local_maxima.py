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
    list_of_maxima = []
    if x[0]>x[1]:
        list_of_maxima.append(0)


    for i in range(len(x) -2):
        if x[i+1] >= x[i] and  x[i+1] >= x[i+2]:
            list_of_maxima.append(i+1)

    if x[-1]>x[-2]:
        list_of_maxima.append(len(x)-1)
    return list_of_maxima

#def main():
    #x = [1, 3, -2, 0, 2, 1]
    #x = [-1, -1, 0, -1]
#    x = [4,2,1,3,1,5]
    #x = [1, 2,2,1]
    #x = input("enter sequence: ")
    #print( type(x))
#    print(find_maxima(x))

#if __name__ == '__main__':
    #main()
