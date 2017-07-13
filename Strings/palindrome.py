import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        #strip anything but letters
        #split into character array

        # counters i, j run from opposite ends at each stop if arr[i] != arr[j] return 0
        string = ''.join(ch for ch in A if ch.isalnum())
        string = string.lower()
        size = len(string)
        print("string: ", string)
        i = 0
        j = size - 1
        while i < size - 1:
            if string[i] != string[j]:
                return 0
            i += 1
            j -= 1

        return 1





if __name__ == '__main__':
    x = Solution()
    print(x.isPalindrome("A man, a plsan, a canal: Panama"))






# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
