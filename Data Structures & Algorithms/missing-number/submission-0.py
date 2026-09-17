class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = int((len(nums) + 1) * len(nums) / 2)
        for n in nums:
            out -= n
        return out