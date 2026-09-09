class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        done = set()
        visit = set()
        out = []
        prereqs = defaultdict(list)
        for c, p in prerequisites:
            prereqs[c].append(p)

        def dfs(c) -> bool:
            if c in visit:
                return False
            if c in done:
                return True
            visit.add(c)
            for p in prereqs[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            out.append(c)
            done.add(c)
            return True

        for c in range(numCourses):
            if c not in done:
                if not dfs(c):
                    return []
        return out
            