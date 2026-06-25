# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        self.balanced = True
        self.height(root)
        return self.balanced
    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if not -1 <= left - right <= 1: self.balanced = False
        return 1 + max(left, right)