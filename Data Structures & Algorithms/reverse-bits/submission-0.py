class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0
        out = 0
        while x < 32:
            out <<= 1
            out += n % 2
            n >>= 1
            x += 1
        return out