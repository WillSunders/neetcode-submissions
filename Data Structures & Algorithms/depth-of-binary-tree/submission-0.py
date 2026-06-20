# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxdepth = 1
        maxdepth = max(maxdepth, self.helper(root.left, 1))
        maxdepth = max(maxdepth, self.helper(root.right, 1))
        return maxdepth
        
    def helper(self, root, depth) -> int:
        if not root: return depth 
        maxdepth = max(depth, self.helper(root.left, depth + 1))
        maxdepth = max(maxdepth, self.helper(root.right, depth + 1))
        return maxdepth