class Solution:
    # @param A : string
    # @return a list of list of strings
    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s):
        return sum([
            [[s[:i+1]] + p for p in self.partition(s[i+1:]) or [[]]]
            for i in xrange(len(s)) if self.isPalindrome(s, 0, i)
        ], [])
