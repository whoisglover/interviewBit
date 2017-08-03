class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, n):
        start, cur_n, mul = [0, 1], 1, 2
        if n == 1:
            return start

        while n != cur_n:
            start = start + [i + mul for i in start[::-1]]
            cur_n, mul = cur_n + 1, mul * 2
        return start
