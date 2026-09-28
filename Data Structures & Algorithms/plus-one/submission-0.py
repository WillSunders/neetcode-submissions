class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = len(digits) - 1
        out = []
        carry = 1
        while curr >= 0:
            num = digits[curr]
            if carry == 1:
                if num + carry > 9:
                    carry = 1
                    num = 0
                else:
                    num += 1
                    carry = 0
            out.append(num)
            curr -= 1
        if carry == 1:
            out.append(carry)
        out.reverse()
        return out