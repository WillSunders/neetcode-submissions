class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for num in nums:
            if num not in vals:
                vals[num] = 1
            else:
                vals[num] += 1
        out = sorted(vals.items(), key=lambda pair: pair[1])
        return [pair[0] for pair in out[-k:]]
