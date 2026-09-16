class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        farthest = 0
        currentend = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == currentend:
                count += 1
                currentend = farthest
        return count

