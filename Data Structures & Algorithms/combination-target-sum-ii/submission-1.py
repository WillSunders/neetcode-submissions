class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out, path = [], []
        def dfs(i: int, rem: int):
            if rem == 0:
                out.append(path[:])
                return
            if i >= len(candidates) or candidates[i] > rem:
                return
            path.append(candidates[i])
            dfs(i+1, rem - candidates[i])
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates [i + 1]:
                i += 1
            dfs(i+1, rem)
        dfs(0, target)
        return out