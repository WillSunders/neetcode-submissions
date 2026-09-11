class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        self.count = 0
        def dfs(num) -> int:
            if num == n:
                return 1
            if num > n:
                return 0
            if num not in memo:
                memo[num] = dfs(num + 1) + dfs(num + 2)
            return memo[num]
        return dfs(0)

                


