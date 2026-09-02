# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        while q:
            out.append(q[-1].val)
            qlen = len(q)
            for _ in range(qlen):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return out

        