class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vals = {}
        for num in nums:
            if vals.get(num):
                return num
            vals[num] = 1
