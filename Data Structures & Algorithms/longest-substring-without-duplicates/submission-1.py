class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        head = 0
        tail = 0
        total = 0
        for letter in s:
            out = letters.get(letter)
            if out is not None and out >= head:
                head = out + 1
            letters[letter] = tail
            total = max(total, tail - head + 1)
            tail += 1
        return total


