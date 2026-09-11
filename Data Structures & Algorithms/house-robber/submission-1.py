class Solution:
    def rob(self, nums: List[int]) -> int:
        count = len(nums) - 1
        if count == 0:
            return nums[count]
        elif count == 1:
            return max(nums[count], nums[count - 1])
        next1, next2, next3 = nums[count-2] + nums[count], nums[count - 1], nums[count]
        count -= 2
        while count > 0:
            count -= 1
            next1, next2, next3 = nums[count] + max(next2, next3), next1, next2
            print(next1, next2, next3)
        
        return max(next1, next2)