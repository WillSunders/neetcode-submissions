class Solution:
    def isValid(self, s: str) -> bool:
        rem = []
        for bracket in s:
            if not rem: rem.append(bracket)
            elif bracket == ']':
                if rem[-1] == '[': rem.pop()
                else: rem.append(bracket)
            elif bracket == ')':
                if rem[-1] == '(': rem.pop()
                else: rem.append(bracket)
            elif bracket == '}':
                if rem[-1] == '{': rem.pop()
                else: rem.append(bracket)
            else:
                rem.append(bracket)
        if not rem: return True
        return False
            