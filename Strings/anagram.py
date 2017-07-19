import string
class Solution:
    # @param A : string
    # @return an integer
    def isAnagram(self, A, B):

        if len(A) != len(B):
            return false
        charCounter = {}
        for char in A:
            if(charCounter[char]):
                charCounter[char] += 1
            else:
                charCounter[char] = 1
        for char in B:
            if(!charCounter[char]):
                return false
            else:
                charCounter[char] -= 1
                if(charCounter[char] < 0):
                    return false

        return true

if __name__ == '__main__':
    x = Solution()
    print(x.isPalindrome("A man, a plsan, a canal: Panama"))






# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
