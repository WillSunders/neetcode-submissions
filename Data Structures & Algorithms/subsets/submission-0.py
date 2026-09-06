class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            for i in range(len(out)):
                out.append(out[i] + [num])
        return out