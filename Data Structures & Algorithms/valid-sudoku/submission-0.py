class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkColumn(board) and self.checkSubBox(board)

    def checkRow(self, board: List[List[str]]) -> bool:
        for y in range(0, 9):
            numCheck = {}
            for x in range(0, 9):
                if board[y][x] != ".":
                    if numCheck.get(board[y][x]) == 1: return False
                    else: numCheck[board[y][x]] = 1
        return True

    def checkColumn(self, board: List[List[str]]) -> bool:
        for x in range(0, 9):
            numCheck = {}
            for y in range(0, 9):
                if board[y][x] != ".":
                    if numCheck.get(board[y][x]) == 1: return False
                    else: numCheck[board[y][x]] = 1
        return True
    def checkSubBox(self, board: List[List[str]]) -> bool:
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                numCheck = {}
                for x2 in range(x, x+3):
                    for y2 in range(y, y+3):
                        if board[y2][x2] != ".":
                            if numCheck.get(board[y2][x2]) == 1: return False
                            else: numCheck[board[y2][x2]] = 1  
        return True