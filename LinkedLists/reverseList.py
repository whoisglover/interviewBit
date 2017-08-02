class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseList(self, head):
        curr = head
        next = None
        prev = None
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(head)
    x = Solution()
    reversedHead = x.reverseList(head)
    print(reversedHead)



# 1 -> 2 -> 3 -> 4 -> 5 -> None

# prev null
# next null
# curr 1
#
#
#
# next = curr.next
#
# curr.next = prev
#
# prev = curr
#
# curr = next
#
#
# curr.next = prev
