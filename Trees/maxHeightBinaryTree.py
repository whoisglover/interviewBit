# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A is None:
            return 0
        x = self.maxDepth(A.left)
        y = self.maxDepth(A.right)
        return max(x,y)+1
