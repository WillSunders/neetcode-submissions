class Solution:
    def maxArea(self, heights: List[int]) -> int:
        head = 0
        tail = len(heights) - 1
        maxarea = 0
        while head < tail:
            maxarea = max(maxarea, (tail - head) * min(heights[tail], heights[head]))
            if heights[head] < heights[tail]: head += 1
            else: tail -= 1
        return maxarea