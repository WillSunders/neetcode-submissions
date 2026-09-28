class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/ x
            n = -n
        out = 1
        while n:
            if n % 2 == 1:
                out *= x
            x *= x
            n //= 2
        return out