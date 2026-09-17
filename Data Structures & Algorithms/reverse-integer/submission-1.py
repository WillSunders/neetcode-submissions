class Solution:
    def reverse(self, x: int) -> int:
        MAXINT = 2**31 - 1
        MININT = -2**31
        neg = -1 if x < 0 else 1

        x = abs(x)
        out = 0

        while x:
            out = out * 10 + x % 10
            x //= 10
        out *= neg

        if out > MAXINT or out < MININT:
            return 0
        return out