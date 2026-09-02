# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.out = []
        if not root:
            return []
        self.search(root, 0)
        return self.out
    def search(self, root: Optional[TreeNode], depth: int):
        if depth >= len(self.out):
            self.out.append([root.val])
        else:
            self.out[depth].append(root.val)
        if root.left:
            self.search(root.left, depth + 1)
        if root.right:
            self.search(root.right, depth + 1)
            
