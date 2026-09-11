class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        count = len(cost) - 1
        c1, c2 = cost[count], 0

        while count > 0:
            count -= 1
            c1, c2 = cost[count] + min(c1, c2), c1
        return min(c1, c2)

        