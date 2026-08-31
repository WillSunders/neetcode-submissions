from _heapq import heapreplace
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        head = tail = 0
        charS = [0] * 52
        charT = [0] * 52
        out = ""
        for val in t:
            charT[self.disp(val)] += 1
        matches = sum (1 for i in range(52) if charS[i] == charT[i])
        for letter in s:
            i = self.disp(letter)
            charS[i] += 1
            if charS[i] == charT[i]:
                matches += 1
            if matches == 52:
                while charS[self.disp(s[head])] > charT[self.disp(s[head])]:
                    charS[self.disp(s[head])] -= 1
                    head += 1
                if not out or len(out) > tail - head + 1:
                    out = s[head:tail+1]
            tail += 1
        tail -= 1
        while charS[self.disp(s[tail])] > charT[self.disp(s[tail])]:
            charS[self.disp(s[tail])] -= 1
            tail -= 1
        if matches == 52:
            if not out or len(out) > tail - head + 1:
                out = s[head:tail+1]
        return out

    def disp(self, letter) -> int:
        if ord(letter) < 97:
            return  ord(letter) - ord('A') + 26
        return ord(letter) - ord('a')
