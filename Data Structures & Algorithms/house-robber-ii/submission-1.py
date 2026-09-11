class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(l: int, r:int) -> int:
            prev, curr = 0, 0
            for i in range(l, r):
                prev, curr = curr, max(curr, prev + nums[i])
            return max(prev, curr)
        size = len(nums)
        if size == 1:
            return nums[0]
        return max(helper(0, size - 1), helper(1, size))