class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        p1, p2, curr = 0, 1, 1
        count = 2
        while count < n:
            p1, p2, curr = p2, curr, p1 + p2 + curr
            count += 1
        return curr
        
