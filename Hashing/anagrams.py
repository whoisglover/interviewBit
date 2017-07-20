class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        wordLengthDictionary = {}
        indexCounterDictionary = {}
        allWordsHashed = []
        resultContainer = []
        nextFreeIndex = 0
        for i in range (len(A)):
            word = A[i]
            wordHash = self.letterHash(word)
            found = 0
            for key in indexCounterDictionary:
                print("key is: ", key)
                print("resultContainer: ", resultContainer)
                if(wordHash == indexCounterDictionary[key]):
                    found = 1
                    resultContainer[key].append(i+1)
            if(found == 0):
                indexCounterDictionary[len(resultContainer)] = wordHash
                resultContainer.append([i+1])
        finalResult = []
        for group in resultContainer:
            if(len(group) >= 2):
                finalResult.append(group)
        return finalResult



    def letterHash(self, word):
        letterDict = {}
        for char in word:
            if char in letterDict:
                letterDict[char] +=1
            else:
                letterDict[char] = 1
        return letterDict
if __name__ == '__main__':
    # x = ["cat", "dog" ,"god", "tca", "hello"]
    x = [ "caat", "taac", "dog", "god", "acta" ]
    y = Solution()
    # print(y.anagrams(x))
    print(y.anagrams(x))





# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]
