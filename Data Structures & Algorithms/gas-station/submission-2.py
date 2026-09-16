class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [0] * len(gas)
        total = 0
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
            total += diff[i]
        if total < 0:
            return -1
        total = 0
        start = 0
        for i, val in enumerate(diff):
            if total < 0:
                start = i
                total = val
            else:
                total += val
        return start
