class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        connect = defaultdict(list)
        for v1, v2 in edges:
            connect[v1].append(v2)
            connect[v2].append(v1)
        
        q = deque([(0, -1)])
        visited.add(0)
        while q:
            v, prev = q.popleft()
            for nb in connect[v]:
                if nb != prev:
                    if nb in visited:
                        return False
                    visited.add(nb)
                    q.append((nb, v))

        for i in range(n):
            if i not in visited:
                return False
        return True





