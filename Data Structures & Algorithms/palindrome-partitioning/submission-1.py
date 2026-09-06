class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        
        def isPalindrome(word:str):
            if not word:
                return False
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r-= 1
            return True
        def dfs(start: int):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start + 1, len(s) + 1):
                word = s[start:i]
                if isPalindrome(word):
                    path.append(word)
                    dfs(i)
                    path.pop()
        dfs(0)
        return res
