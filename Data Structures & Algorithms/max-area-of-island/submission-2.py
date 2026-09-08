class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxsize = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            count = 1
            while q:
                r, c = q.popleft()
                for x, y in dirs:
                    nr, nc = r + x, c + y
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        count += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            self.maxsize = max(self.maxsize, count)
                    
        for c in range(cols):
            for r in range(rows):
                if grid[r][c] == 1:
                    dfs(r, c)
        return self.maxsize