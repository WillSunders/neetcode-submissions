class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i: int, rem: int):
            if rem == 0:
                return 1
            if i == len(coins):
                return 0
            if (i+1, rem) in dp:
                skip = dp[i+1, rem]
            else:
                skip = dfs(i+1, rem)
            if coins[i] > rem:
                take = 0
            elif (i, rem - coins[i]) in dp:
                take = dp[i, rem-coins[i]]
            else:
                take = dfs(i, rem - coins[i])
            dp[i, rem] = skip + take
            return skip + take
        return dfs(0, amount)