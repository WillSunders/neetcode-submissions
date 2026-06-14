class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprof = 0
        minval = prices[0]
        for price in prices:
            if price < minval:
                minval = price
            elif price - minval > mprof:
                mprof = price - minval
        return mprof
        