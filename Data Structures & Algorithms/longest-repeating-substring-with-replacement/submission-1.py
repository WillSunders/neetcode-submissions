class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = [0] * 26
        head = 0
        tail = 0
        total = 0
        n = 0
        for l in s:
            letters[ord(l) - ord('A')] += 1
            n = max(n, letters[ord(l) - ord('A')])
            while tail - head + 1 - n > k:
                letters[ord(s[head]) - ord('A')] -= 1
                head += 1
            total = max(total, tail - head + 1)
            tail += 1
        return total