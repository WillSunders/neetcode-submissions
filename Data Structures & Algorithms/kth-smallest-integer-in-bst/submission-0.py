# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = collections.deque()
        curr = root
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            if k == 1:
                return curr.val
            k -= 1
            curr = curr.right