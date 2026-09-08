"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        if not node:
            return None
        def search(node: Optional['Node']):
            for n in node.neighbors:
                if n not in nodes:
                    nodes[n] = Node(n.val, None)
                    search(n)
                nodes[node].neighbors.append(nodes[n])
        nodes[node] = Node(node.val, None)
        search(node)
        return nodes[node]
                    
        

