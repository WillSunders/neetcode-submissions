class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            nxt = 0
            while n > 0:
                nxt += (n % 10) ** 2
                n = n // 10
            if nxt == 1:
                return True
            if nxt in nums:
                return False
            nums.add(nxt)
            n = nxt
            