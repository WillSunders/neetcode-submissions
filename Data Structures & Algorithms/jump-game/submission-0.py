class Solution:
    def canJump(self, nums: List[int]) -> bool:
        vals = [0]
        while vals:
            curr = heapq.heappop(vals)
            if curr == len(nums) - 1:
                return True
            jump = nums[curr]
            while jump > 0:
                if curr + jump not in vals:
                    heapq.heappush(vals, curr + jump)
                jump -= 1
        return False
        