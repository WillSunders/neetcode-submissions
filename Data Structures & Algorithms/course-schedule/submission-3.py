class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        prereqs = {}
        done = set()
        prereqs = defaultdict(list)
        for course, pre in prerequisites:
            prereqs[course].append(pre)
            
        def dfs(n: int) -> bool:
            if n in done:
                return True
            if n in visit:
                return False
            visit.add(n)
            for p in prereqs[n]:
                if not dfs(p):
                    return False
            visit.remove(n)
            done.add(n)
            return True
        
        for n in range(numCourses):
            if n not in done:
                if not dfs(n):
                    return False
                done.add(n)
        return True
        



                    
        
        