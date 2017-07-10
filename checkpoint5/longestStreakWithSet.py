class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):

        nums = set(A)
        streak = 0
        for x in nums:
            if x + 1 not in nums:
                y = x - 1
                while y in nums:
                    y -= 1
                streak = max(streak, x - y)
        return streak
