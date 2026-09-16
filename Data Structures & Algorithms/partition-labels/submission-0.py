class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = defaultdict(list)
        for i in range(len(s)):
            cache[s[i]] = i
        end = 0
        out = []
        count = 0
        for i in range(len(s)):
            count += 1
            end = max(end, cache[s[i]])
            if end == i:
                out.append(count)
                count = 0
        return out
