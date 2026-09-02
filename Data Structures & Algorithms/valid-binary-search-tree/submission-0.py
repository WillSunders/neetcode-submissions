# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = float("-infinity")
        right = float("infinity")
        def valid(root: Optional[TreeNode], l, r) -> bool:
            if root:
                if l < root.val < r:
                    return valid(root.left, l, root.val) & valid(root.right, root.val, r)
                return False
            return True
        return valid(root, left, right)
