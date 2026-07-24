class Solution:
    def trap(self, height: List[int]) -> int:
        head = 0
        tail = len(height) - 1
        area = 0
        while head < tail:
            if height[head] < height[tail]:
                temp = head + 1
                neg = 0
                while height[temp] < height[head]:
                    neg += height[temp]
                    if temp >= tail:
                        return area
                    temp += 1
                area += (temp - head - 1) * height[head] - neg
                head = temp
            else:
                temp = tail - 1
                neg = 0
                while height[temp] < height[tail]:
                    neg += height[temp]
                    if temp <= head:
                        return area
                    temp -= 1
                area += (tail - temp - 1) * height[tail] - neg
                tail = temp
        return area
                