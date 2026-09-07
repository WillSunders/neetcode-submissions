import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        vals = []
        for i, point in enumerate(points):
            vals.append([math.sqrt(point[0]*point[0]+point[1]*point[1]), i])
        heapq.heapify(vals)
        for j in range(k):
            out.append(points[heapq.heappop(vals)[1]])
        return out