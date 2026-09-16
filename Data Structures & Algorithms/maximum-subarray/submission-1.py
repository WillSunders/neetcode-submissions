class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        best = res
        for n in nums[1:]:
            if res < 0:
                res = n
            else:
                res += n
            best = max(best, res)
        return best