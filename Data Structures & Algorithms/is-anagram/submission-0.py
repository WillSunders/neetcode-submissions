class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        i = 0
        for i, x in enumerate(s):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        i = 0
        while(i < 26):
            if count[i] != 0: 
                return False
            i += 1
        return True