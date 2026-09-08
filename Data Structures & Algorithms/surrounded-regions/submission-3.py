class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        rows, cols = len(board), len(board[0])
        seen = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in 0, cols - 1:
                if board[r][c] != 'X':
                    seen[r][c] = True
                    q.append((r, c))
        for c in range(1, cols - 1):
            for r in 0, rows - 1:
                if board[r][c] != 'X':
                    seen[r][c] = True
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for x, y in ((1,0), (-1, 0), (0,1), (0, -1)):
                nr, nc = r+ x, c+y
                if 0<= nr < rows and 0<= nc < cols and board[nr][nc] != 'X' and not seen[nr][nc]:
                    seen[nr][nc] = True
                    q.append((nr, nc))

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] != 'X' and not seen[r][c]:
                    board[r][c] = 'X'
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for x, y in ((1,0), (-1, 0), (0,1), (0, -1)):
                nr, nc = r+ x, c + y
                if 0<= nr < rows and 0<= nc < cols and board[nr][nc] != 'X' and not seen[nr][nc]:
                    board[nr][nc] = 'X'
                    q.append((nr, nc))
        

                    

