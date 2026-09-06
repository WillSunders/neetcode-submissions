class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out, path = [], []

        def dfs(op: int, cl: int):
            if op == cl == n:
                out.append("".join(path))
                return
            if op > cl:
                path.append(')')
                dfs(op, cl + 1)
                path.pop()
            if op < n:
                path.append('(')
                dfs(op + 1, cl)
                path.pop()
        dfs(0, 0)
        return out