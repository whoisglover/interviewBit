class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if A == None or len(A) == 0:
            return 0
        sequenceHash = {}
        max_sequence = 1
        for n in A:
            sequenceHash[n] = 1
        for key, value in sequenceHash.items():
            if value == 1:
                down = key - 1
                up = key + 1
                sequence = 1
                #traverse downward loooking for values 1 less each time
                while down in sequenceHash:
                    sequence += 1
                    sequenceHash[down] = 0
                    down -= 1
                #traverse upward loooking for values 1 greater each time
                while up in sequenceHash:
                    sequence += 1
                    sequenceHash[up] = 0
                    up += 1
                if sequence > max_sequence:
                    max_sequence = sequence
        return max_sequence
