# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-infinity")
        def nonsplit(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = nonsplit(root.left)
            right = nonsplit(root.right)
            split = left + right + root.val
            nsplit = max(left + root.val, right + root.val, root.val)
            self.res = max(self.res, split, nsplit)
            return nsplit
        nonsplit(root)
        return self.res