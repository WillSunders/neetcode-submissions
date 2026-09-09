class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        squares = [[grid[0][0], 0, 0]]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        maxH = 0
        while squares:
            h, x, y = heapq.heappop(squares)
            if (x, y) in visited:
                continue
            maxH = max(h, maxH)
            visited.add((x, y))
            if x == rows - 1 and y == cols - 1:
                return maxH
            for cx, cy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + cx, y + cy
                if 0 <= nx < rows and 0 <= ny < cols:
                    heapq.heappush(squares, [grid[nx][ny], nx, ny])

