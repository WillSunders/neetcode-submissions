class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rs = [1] * rows
        cs = [1] * cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rs[r] = 0
                    cs[c] = 0
        for r in range(rows):
            for c in range(cols):
                if rs[r] == 0 or cs[c] == 0:
                    matrix[r][c] = 0
        




        