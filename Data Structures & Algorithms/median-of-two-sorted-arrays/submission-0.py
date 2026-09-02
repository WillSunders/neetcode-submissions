class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A) - 1
        length = len(A) + len(B)
        half = length // 2
        while True:
            i = (l + r) // 2
            j = half - i - 2
            aleft = A[i] if i >= 0 else float("-infinity")
            aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            bleft = B[j] if j >= 0 else float("-infinity")
            bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if aleft <= bright and bleft <= aright:
                if length % 2:
                    return min(aright, bright)
                else:
                    return((max(aleft, bleft) + min(aright, bright))/ 2)
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1