class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i: int, val: int):
            if i == len(nums):
                if val == target:
                    return 1
                else:
                    return 0
            if (i + 1, val + nums[i]) in dp:
                add = dp[i+1, val + nums[i]]
            else:
                add = dfs(i+1, val + nums[i])
            if (i + 1, val - nums[i]) in dp:
                sub = dp[i+1, val - nums[i]]
            else:
                sub = dfs(i+1, val - nums[i])
            dp[i, val] = add + sub
            return add + sub
        return dfs(0, 0)