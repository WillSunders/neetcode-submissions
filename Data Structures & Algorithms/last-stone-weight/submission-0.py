class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = []
        for stone in stones:
            rocks.append(-stone)
        heapq.heapify(rocks)
        while(len(rocks) > 1):
            r1 = heapq.heappop(rocks)
            r2 = heapq.heappop(rocks)
            heapq.heappush(rocks, -abs(r1-r2))
        return -rocks[0]
            