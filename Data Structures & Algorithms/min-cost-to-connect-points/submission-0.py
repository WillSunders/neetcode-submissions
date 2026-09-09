class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        cost = 0
        edges = [(0, 0)]

        while edges:
            dis, node = heapq.heappop(edges)
            print(node)
            if node in visited:
                continue
            cost += dis
            visited.add(node)
            if len(visited) == len(points):
                return cost
            for i in range(len(points)):
                if i not in visited:
                    ham = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    heapq.heappush(edges, (ham, i))