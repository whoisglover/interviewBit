class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def maxDistance(self, A):
        size = len(A)
        maxDistance = -1
        origHash = {}
        for i in range(0, size):
            origHash[A[i]] = i


        return maxDistance
