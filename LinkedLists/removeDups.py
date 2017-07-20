# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):

        if(A is None or A.next is None):
            return A
        curr = A
        while(curr is not None and curr.next is not None):
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return A
