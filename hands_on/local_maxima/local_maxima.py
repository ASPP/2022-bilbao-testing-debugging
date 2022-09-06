def local_maxima(x):

    ret = []

    pos = 0
    incr = False


    if x[0] >= x[1]:
        ret.append(0)

    while pos < len(x)-2:

        while x[pos] < x[pos+1]:
        #    print("comparing {} and {}".format(vet[pos], vet[pos+1]))
            pos += 1
            incr = True

        if incr:
            ret.append(pos)
            incr = False

        while x[pos] == x[pos+1]:
            pos += 1
        #print("appending pos {} to ret".format(pos))
        
        if x[pos] > x[pos+1]:
            pos += 1
   
    if x[-2] < x[-1]:
        #print("LAST COMPARISON: {} - {}".format(vet[-2], vet[-1]))
        ret.append(len(x)-1)

    return ret
