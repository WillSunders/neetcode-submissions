class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        count = 0
        nxt = 1
        while count < len(intervals):
            current = intervals[count]
            while nxt < len(intervals):
                if current[1] < intervals[nxt][0]:
                    res.append(current)
                    break
                current = [min(current[0], intervals[nxt][0]), max(current[1], intervals[nxt][1])]
                nxt += 1
            count = nxt
            nxt += 1
        res.append(current)
        return res
                