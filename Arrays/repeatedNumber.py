class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        hashMap = dict()
        for num in A:
            if num in hashMap:
                return num
            else:
                hashMap[num] = 1
        return -1





if __name__ == '__main__':
    x = [3, 4, 1, 4, 1]
    y = Solution()
    print(y.repeatedNumber(x))




#[3 4 1 4 1]
# 1
