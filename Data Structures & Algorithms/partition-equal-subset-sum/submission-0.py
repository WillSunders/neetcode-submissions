class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target = target // 2
        sums = {0}
        for n in nums:
            new_sums = set()
            for s in sums:
                if s + n == target:
                        return True
                if s + n < target:
                    new_sums.add(s+n)
            sums |= new_sums
        return False