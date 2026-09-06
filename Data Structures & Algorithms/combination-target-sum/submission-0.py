class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out, path = [], []
        def dfs(i: int, rem: int):
            if rem == 0:
                out.append(path.copy())
                return
            if rem < 0 or i >= len(nums):
                return
            path.append(nums[i])
            dfs(i, rem - nums[i])
            path.pop()
            dfs(i + 1, rem)
        dfs(0, target)
        return out
        
