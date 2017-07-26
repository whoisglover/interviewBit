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

        # print("needleSize: ", needleSize)
        # print("haystackSize: ", haystackSize)
        if not needle:
            return -1
        if not haystack:
            return -1
        j=0
        for i in range(0,len(haystack)):
            if(haystack[i] == needle[0]):
                j = 0
                # print("i: ", i)
                # print("first i+j: ", i + j)
                while(j<needleSize and (j+i < haystackSize) and haystack[j+i] == needle[j]):
                    j += 1
                    # print("i+j: ", i + j)
                if(j == needleSize):
                    return i

        return -1





if __name__ == '__main__':
    x = Solution()
    print(x.strStr("danny", "ny"))
    print(x.strStr("bbbbbbbbab", "baba"))
    # print(x.strStr("babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba", "bababbbbbbabbbaabbaaabbbaababa"))


# "babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba"
# "bababbbbbbabbbaabbaaabbbaababa"



# What peach wonderful world
# 0123456789
