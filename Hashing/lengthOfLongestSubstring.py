class Solution:
    # @param A : string
    # @return an integer
    # def lengthOfLongestSubstring(self, A):




    def longestUniqueSubsttr(string):
        NO_OF_CHARS = 256
        n = len(string)
        cur_len = 1        # To store the lenght of current substring
        max_len = 1        # To store the result
        prev_index = 0    # To store the previous index
        i = 0

        # Initialize the visited array as -1, -1 is used to indicate
        # that character has not been visited yet.
        visited = [-1] * NO_OF_CHARS

        # Mark first character as visited by storing the index of
        # first character in visited array.
        visited[ord(string[0])] = 0

        # Start from the second character. First character is already
        # processed (cur_len and max_len are initialized as 1, and
        # visited[str[0]] is set
        for i in range(1,n):
            prev_index = visited[ord(string[i])]

            # If the currentt character is not present in the already
            # processed substring or it is not part of the current NRCS,
            # then do cur_len++
            if prev_index == -1 or (i - cur_len > prev_index):
                cur_len+=1

            # If the current character is present in currently considered
            # NRCS, then update NRCS to start from the next character of
            # previous instance.
            else:
                # Also, when we are changing the NRCS, we should also
                # check whether length of the previous NRCS was greater
                # than max_len or not.
                max_len = max(max_len, cur_len)

                cur_len = i - prev_index

            # update the index of current character
            visited[ord(string[i])] = i

        # Compare the length of last NRCS with max_len and update
        # max_len if needed
        max_len = max(max_len, cur_len)

        return max_len


if __name__ == '__main__':
    x = Solution()
    y = Solution.longestUniqueSubsttr("dadbc")
    print(y)
