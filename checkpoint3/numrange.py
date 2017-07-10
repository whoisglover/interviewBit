class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        a, b = 0, 0
        arrayLength = len(A)
        count = 0
        if(B == 0 and C == 0):
            return 0
        for i in range(arrayLength):
            while a != (arrayLength+1) and sum(A[i:a]) < B:
                a += 1
            while b != (arrayLength+1) and sum(A[i:b]) <= C:
                b += 1
            for j in range(a, b):
                count +=1
        return count
