def nextGreater(self, A):
        nge = [-1] * len(A)
        for i in xrange(len(A)):
            for n in A[i:]:
                if n > A[i]:
                    nge[i] = n
                    break
        return nge
