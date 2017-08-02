# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if A is None:
            return 1
        lh = self.height(A.left)
        rh = self.height(A.right)
    def height(self, A):
        if A is None:
            return 0
        return 1 + max(self.height(A.left), self.height(A.right))





if __name__ == '__main__':
