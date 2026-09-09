class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            size[rx] += size[ry]
            parent[ry] = rx
            return True
        
        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
        

