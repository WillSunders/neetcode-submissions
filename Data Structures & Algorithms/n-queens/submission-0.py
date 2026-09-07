class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [["." for _ in range(n)] for _ in range(n)]
        cols, pos, neg = set(), set(), set()
        
        def search(r: int):
            if r == n:
                res.append(["".join(row) for row in queens])
                return
            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue
                queens[r][c] = 'Q'
                cols.add(c); pos.add(r+c); neg.add(r-c)
                search(r+1)
                queens[r][c] = '.'
                cols.remove(c); pos.remove(r+c); neg.remove(r-c)
        search(0)
        return res
            

