class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0

        def search(r: int, c:int):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if visited[r][c] or grid[r][c] == '0':
                return
            visited[r][c] = True
            search(r+1,c)
            search(r-1,c)
            search(r, c+1)
            search(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] or grid[r][c] == '0':
                    continue
                search(r, c)
                count += 1
        return count