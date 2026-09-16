class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        goal = len(nums) - 1
        while l <= r:
            if r >= goal:
                return count
            nr = r
            while l <= r:
                if nums[l] + l > r:
                    nr = max(nums[l] + l, nr)
                l += 1
            r = nr
            count += 1
        return 0

