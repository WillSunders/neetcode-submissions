class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols = len(board[0])
        rows = len(board)
        visited = [[False] * cols for _ in range(rows)]
        def search(r: int, c:int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if visited[r][c] or board[r][c] != word[i]:
                return False
            visited[r][c] = True
            found = (search(r + 1, c, i + 1) or
                     search(r - 1, c, i + 1) or
                     search(r, c + 1, i + 1) or
                     search(r, c - 1, i + 1))
            visited[r][c] = False
            return found
          
        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0):
                    return True
        return False
        