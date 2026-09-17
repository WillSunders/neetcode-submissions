class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        LARGEST = 0x7FFFFFFF
        while b:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry
        return a if a <= LARGEST else ~(a ^ MASK)