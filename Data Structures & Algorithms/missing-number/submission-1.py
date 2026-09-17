class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = len(nums)
        for i, n in enumerate(nums):
            out ^= i ^ n
        return out