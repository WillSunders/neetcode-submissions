class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        if len(t) > len(s):
            return 0
        def dfs(i: int, curr:int) -> int:
            if curr == len(t):
                return 1
            if i == len(s):
                return 0
            total = 0
            if s[i] == t[curr]:
                if (i + 1, curr + 1) in dp:
                    total = dp[i + 1, curr + 1]
                else:
                    total = dfs(i + 1, curr + 1)
                    dp[i + 1, curr + 1] = total
            if (i+ 1, curr) in dp:
                skip = dp[i+ 1, curr]
            else:
                skip = dfs(i + 1, curr)
                dp[i + 1, curr] = skip
            return total + skip

        return dfs(0, 0)