class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        size = len(A)
        lengthCounter = 0
        # print("hello World")
        # print("size: ", size)
        spaceEncountered = 0
        lastWordLength = 0
        for i in range(0, size):
            if(A[i] == ' '):
                if(not spaceEncountered):
                    lastWordLength = lengthCounter
                    spaceEncountered = 1
                    lengthCounter = 0
            else:
                spaceEncountered = 0
                lengthCounter +=1
        print("spaceEncountered: ", spaceEncountered)
        print("lastWordLength: ", lastWordLength)
        if(spaceEncountered):
            print("here")
            return lastWordLength
        else:
            print("else block")
            return lengthCounter





if __name__ == '__main__':
    x = Solution()
    print(x.lengthOfLastWord("Hello World  "))

 #
 # "  xDGBklKecz IAcOJYOH O  WY WPi"
 #
 # "Hello World  "
