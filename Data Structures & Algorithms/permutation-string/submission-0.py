class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = [0] * 26
        chars2 = [0] * 26
        head = tail = 0
        for val in s1:
            chars1[ord(val)-ord('a')] += 1
        for s in s2:
            i = ord(s) - ord('a')
            chars2[i] += 1
            if chars2 == chars1:
                return True
            while chars2[i] > chars1[i]:
                chars2[ord(s2[head]) - ord('a')] -= 1
                head += 1  
            tail += 1
        return False