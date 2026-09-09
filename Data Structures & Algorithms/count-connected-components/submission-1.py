class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n 
        self.components = n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            self.components -= 1
        for v1, v2 in edges:
            union(v1, v2)
        return self.components