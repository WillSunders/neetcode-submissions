class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cost = {0:0}
        def search(n: int) -> int:
            if n in cost:
                return cost[n]
            best = float("inf")
            for c in coins:
                if c <= n:
                    sub = search(n-c)
                    if sub != -1:
                        best = min(best, sub + 1)
            cost[n] = -1 if best == float("inf") else int(best)
            return cost[n]
        return search(amount)


                



