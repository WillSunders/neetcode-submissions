class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1 + s2):
            return False
        dp = {}
        def dfs(i1: int, i2: int) -> bool:
            if i1 + i2 == len(s3):
                return True
            done = False
            if i1 < len(s1):
                if s1[i1] == s3[i1 + i2]:
                    if (i1 + 1, i2) in dp:
                        done = dp[i1+1, i2]
                    else:
                        done = dfs(i1 + 1, i2)
                        dp[i1+1, i2] = done
            if i2 < len(s2) and not done and i1 + i2 < len(s3):
                if s2[i2] == s3[i1 + i2]:
                    if (i1, i2 + 1) in dp:
                        done = dp[i1, i2 + 1]
                    else:
                        done = dfs(i1, i2 + 1)
                        dp[i1, i2 + 1] = done
            return done
        return dfs(0, 0)
