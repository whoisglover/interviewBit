import pdb

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        stringA = str(A)
        substrings = []
        productDictionary = {}
        for i in range(len(stringA)):
            for j in range(i, len(stringA)+1):
                # pdb.set_trace()
                sub = stringA[i:j]
                # print("substring: ", stringA[i:j])
                if sub:
                    substrings.append(sub)
        # print("substrings: ", substrings)
        for substring in substrings:
            product = 1
            for char in substring:
                product = product * int(char)
            # print("substring: ", substring)
            # print("product: ", product)

            if(str(product) in productDictionary):
                return 0
            else:
                productDictionary[str(product)] = substring
        return 1



if __name__ == '__main__':
    x = 3245
    y = Solution()
    print(y.colorful(x))
