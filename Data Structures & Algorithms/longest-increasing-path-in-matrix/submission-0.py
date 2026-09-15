class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        def dfs(r: int, c:int) -> int:
            if (r, c) in dp:
                return dp[r,c]
            total = 1
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + x, c +y
                if 0 <= nr < rows and 0<= nc < cols and matrix[r][c] < matrix[nr][nc]:
                    total = max(total, 1 + dfs(nr, nc))
            dp[r, c] = total
            return total
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res