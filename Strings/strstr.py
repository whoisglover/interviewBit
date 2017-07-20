class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        indexEncountered = -1
        needleIndexCounter = 0
        tracking = 0
        substring = ""
        needleSize = len(needle)
        haystackSize = len(haystack)
        if not needle:
            return -1
        if not haystack:
            return -1
        j = 0
        for i in range(len(haystack)):
            if(haystack[i] == needle[needleIndexCounter]):
                if(indexEncountered < 0):
                    indexEncountered = i
                tracking = 1
                needleIndexCounter += 1

                print("needleIndexCounter : ", needleIndexCounter)
                print("substring: ", substring)
                print("len(needle): ", len(needle));
                if(needleIndexCounter == len(needle)):
                    return indexEncountered
            else:
                needleIndexCounter = 0
                indexEncountered = -1
                tracking = 0
        return -1





if __name__ == '__main__':
    x = Solution()
    # print(x.strStr("What peach wonderful world", "peach"))
    # print(x.strStr("bbbbbbbbab", "baba"))
    print(x.strStr("babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba", "bababbbbbbabbbaabbaaabbbaababa"))


# "babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba"
# "bababbbbbbabbbaabbaaabbbaababa"



# What peach wonderful world
# 0123456789
