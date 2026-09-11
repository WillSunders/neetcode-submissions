class Solution:
    def numDecodings(self, s: str) -> int:
        n1, n2 = 1, 1
        count = 0
        size = len(s)
        for i in range(size - 1, -1, -1):
            count = n1
            if int(s[i]) != 0:
                if i + 1 < size and (int(s[i]) == 1 or ((int(s[i]) == 2) and 0 <= int(s[i + 1]) <= 6)):
                    count += n2
            else:
                count = 0
            n1, n2 = count, n1
        return count

                
            
            