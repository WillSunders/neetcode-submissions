class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0] * (n + 1)
        count = 1
        out[0] = 0
        offset = 1
        while count <= n:
            out[count] = out[count % offset] + 1
            count += 1
            if count == offset * 2: offset *= 2
        return out