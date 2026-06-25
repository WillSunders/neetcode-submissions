class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 0
        count = 0
        while x < 32:
            if n & 1 == 1: count += 1
            n >>= 1
            x += 1
        return count