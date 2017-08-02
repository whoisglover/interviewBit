# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(A):
        result = []
        stack = []
        current = A
        done = 0
        while(not done):
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if(len(stack) > 0):
                    current = stack.pop()
                    result.append(current.val)
                    current = current.right
                else:
                    done = 1

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    x = Solution()
    y = Solution.inorderTraversal(root)
    print(y)
