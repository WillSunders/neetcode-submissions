# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "None,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)

        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.nodes = data.split(",")
        self.i = 0
        def create() -> Optional[TreeNode]:
            val = self.nodes[self.i]
            self.i += 1
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = create()
            node.right = create()
            return node
        return create()