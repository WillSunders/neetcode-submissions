class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = 0
        leftmax = 0
        for b in s:
            if b == '(':
                leftmin += 1
                leftmax += 1
            elif b == ')':
                if leftmin > 0:
                    leftmin -= 1
                leftmax -= 1
                if leftmax < 0:
                    return False
            else:
                if leftmin > 0:
                    leftmin -= 1
                leftmax += 1
        if leftmin <= 0 <= leftmax:
            return True
        return False
        