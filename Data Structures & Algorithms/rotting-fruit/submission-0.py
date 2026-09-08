class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        
        while q:
            r, c, time = q.popleft()
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + x, c + y
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, time+1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time
                    