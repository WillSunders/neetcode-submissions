class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        count = 0
        for i in range(1, len(intervals)):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = min(res[-1][1], intervals[i][1])
                count += 1
        return count