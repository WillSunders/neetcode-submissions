class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(si: int, pi:int) -> bool:
            if pi == len(p):
                if si == len(s):
                    return True
                return False
            if (si, pi) in dp:
                return dp[si, pi]
            if pi + 1 < len(p) and p[pi + 1] == '*':
                if si < len(s) and (s[si] == p[pi] or p[pi] == '.'):
                    if dfs(si + 1, pi):
                        dp[si, pi] = True
                        return True
                if dfs(si, pi + 2):
                    dp[si, pi] = True
                    return True
                  
            else:
                if si < len(s) and (s[si] == p[pi] or p[pi] == '.'):
                    if dfs(si + 1, pi + 1):
                        dp[si, pi] = True
                        return True
            dp[si, pi] = False
            return False
        return dfs(0, 0)