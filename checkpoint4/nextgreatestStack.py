class Solution:
    # @param A : list of integers
    # @return a list of integers
    def newStack(self):
        return []

    def isEmpty(self, stack):
        return len(stack) == 0

    def push(self, stack, x):
        stack.append(x)

    def pop(self, stack):
        if self.isEmpty(stack):
            print("Error : stack underflow")
        else:
            return stack.pop()

    def nextGreater(self, arr):
        s = self.newStack()
        element = 0
        next = 0
        answer = []
        # push the first element to stack
        self.push(s, arr[0])

        # iterate for rest of the elements
        for i in range(1, len(arr), 1):
            next = arr[i]

            if self.isEmpty(s) == False:
                element = self.pop(s)
                while element < next :
                    answer.append(next)
                    if self.isEmpty(s) == True :
                        break
                    element = self.pop(s)
                if  element > next:
                    self.push(s, element)
            self.push(s, next)
        while self.isEmpty(s) == False:
                element = self.pop(s)
                next = -1
                answer.append(next)
        return answer


if __name__ == "__main__":
    # arr = [11, 13, 21, 3]
    arr =  [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
    solution = Solution()
    result = solution.nextGreater(arr)
    print(result)
