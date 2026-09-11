class Solution:
    def climbStairs(self, n: int) -> int:
        def matMul(A, B):
            return[
                [A[0][0]*B[0][0] + A[0][1]*B[1][0],
                 A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0],
                 A[1][0]*B[0][1] + A[1][1]*B[1][1]],
            ]
        def matPow(M, p):
            result = [[1,0], [0, 1]]
            while p:
                if p & 1:
                    result = matMul(result, M)
                M = matMul(M, M)
                p >>= 1
            return result
        
        if n == 0:
            return 1

        M = [[1, 1],[1, 0]]
        P = matPow(M, n)
        return P[0][0]



                


