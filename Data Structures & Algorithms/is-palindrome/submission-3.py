class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0;
        tail = len(s) - 1
        s = s.lower()
        while head < tail:
            while head < tail and not s[head].isalnum():
                head += 1
            while tail > head and not s[tail].isalnum():
                tail -= 1
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True
