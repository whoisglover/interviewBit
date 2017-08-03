class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, nums):
        # if(len(A) is 0):
        #     print([])
        #     return []
        # print(A[0:len(A)])
        # return self.subsets(A[0:len(A)-1])
        # return self.subsetsSolution([], sorted(A))
        if nums is None: return None
        subsets = [[]]
        next = []
        for n in nums:
            for s in subsets:
                next.append(s + [n])
            subsets += next
            next = []
        return subsets

    def subsetsSolution(self, cur, A):
        if A:
            return self.subsetsSolution(cur, A[1:]) + self.subsetsSolution(cur+[A[0]], A[1:])
        return [cur]


if __name__ == '__main__':
    input = [1,2,3]
    x = Solution()
    print(sorted(x.subsets(input)))
