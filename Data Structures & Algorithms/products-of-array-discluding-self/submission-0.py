class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        i = 1
        prod = 1
        while i < len(nums):
            prod = prod * nums[i -1]
            output[i] *= prod
            i += 1
        i -= 2
        prod = 1
        while i >= 0:
            prod = prod * nums[i+1]
            output[i] *= prod
            i -= 1
        return output
