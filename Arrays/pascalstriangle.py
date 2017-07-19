class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):

        if(A == 0):
            return []
        if(A == 1):
            result = []
            result.append("1")
            return result
        result = []
        prev = [1]
        result.append(prev)

        for i in range(1,A):
            current = [1]
            for j in range(0,len(prev)-1):
                current.append(prev[j] + prev[j+1])
            current.append(1)
            result.append(current)
            prev = current

        return result



if __name__ == '__main__':
    x = 1
    y = Solution()
    print(y.generate(x))
