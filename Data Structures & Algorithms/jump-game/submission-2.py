class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 2, -1 , -1):
            if i + nums[i] >= goal:
                goal = i
            if goal == 0:
                return True
        return False
        