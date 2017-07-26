class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if(numerator == 0):
            return "0"
        if(denominator == 0):
            return ""
        result = ""
        if(numerator < 0 or denominator < 0):
            result += "-"
        num = abs(numerator)
        den = abs(denominator)

        res = int(num / den)
        result += str(res)
        # print("res: ", res)
        remainder = (num % den) * 10
        # print("remainder:", remainder)
        if(remainder == 0):
            return result
        hashMap = {}
        result += "."
        while (remainder !=0):
            #if digits repeat:
            if remainder in hashMap:
                beg = hashMap[remainder]
                part1 = result[0:beg]
                part2 = result[beg:len(result)]
                result = part1 + "(" + part2 + ")"
                return result
            hashMap[remainder] = len(result)
            res = int(remainder / den)
            result += str(res)
            remainder = (remainder % den) * 10
        return result


if __name__ == "__main__":
    x = Solution()
    y = x.fractionToDecimal(1, 4)
    print(y)
