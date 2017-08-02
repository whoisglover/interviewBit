class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x is 0:
            return 0
        res = 1
        mul = x % d
        while n:
            if n % 2:
                res = (res * mul) % d
            mul = (mul * mul) % d
            n /= 2
        return res
