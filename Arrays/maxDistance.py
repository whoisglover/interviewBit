def maxDistance(A):
    size = len(A)
    result = 0
    lMin  = [0] * size
    rMax = [0] * size
    lMin[0] = A[0]
    if(size <= 1):
        return 0
    for i in range(1, size):
        lMin[i] = min(A[i], lMin[i-1])
    rMax[size-1] = A[size-1]

    for j in range(size-2, -1, -1):
        print("j: ", j)

        rMax[j] = max(A[j], rMax[j+1])

    print("lMin: ", lMin)
    print("rMax: ", rMax)

    i = 0
    j = 0
    maxDist = -1

    while(j < size and i < size):
        if(lMin[i] <= rMax[j]):
            maxDist = max(maxDist, j -i)
            j += 1
        else:
            i += 1

    print("maxDist: ", maxDist)
    return maxDist



if __name__ == '__main__':
    x = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0];
    y = [3,5,4,2]
    maxDistance(z)

# lMin:  [3, 3, 3, 2]
# rMax:  [5, 5, 4, 2]

#
# lMin:  [9, 2, 2, 2, 2, 2, 2, 2, 2, 0]
# rMax:  [0, 18, 18, 18, 18, 18, 18, 18, 18, 0]
