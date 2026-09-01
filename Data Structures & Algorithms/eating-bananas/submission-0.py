class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        left = 1
        right = maxPile
        while left < right:
            middle = left + (right - left) // 2
            total = 0
            for i in piles:
                total +=  (i + middle - 1) // middle
            if total > h:
                left = middle + 1
            else:
                right = middle
        return left
            