class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = currmax = currmin = nums[0]
        for n in nums[1:]:
            candidates = (n, currmax*n, currmin *n)
            currmax = max(candidates)
            currmin = min(candidates)
            res = max(res, currmax)
        return res
        