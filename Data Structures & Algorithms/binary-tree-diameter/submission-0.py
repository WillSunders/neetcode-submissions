# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxdiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.maxdiameter

    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.maxdiameter = max(self.maxdiameter, self.height(root.left) + self.height(root.right))
        return 1 + max(self.height(root.left), self.height(root.right))
