class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][0] > height:
                out = stack.pop()
                index = out[1]
                maxArea = max(maxArea, out[0] * (i - index))
            stack.append([height, index])
        while stack:
            out = stack.pop()
            maxArea = max(maxArea, out[0] * (len(heights) - out[1]))
        return maxArea