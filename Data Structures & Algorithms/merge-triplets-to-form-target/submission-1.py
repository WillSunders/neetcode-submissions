class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cx, cy, cz = 0, 0, 0
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                cx = max(x, cx)
                cy = max(y, cy)
                cz = max(z, cz)
        if target == [cx, cy, cz]:
            return True
        return False