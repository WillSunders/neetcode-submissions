
class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word)) + '#' + word
        return out

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            words.append(s[j+1: j+1+n])
            i = j + 1 + n
        return words