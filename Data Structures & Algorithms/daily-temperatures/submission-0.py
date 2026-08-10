class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = len(temperatures)
        output = [0] * count
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                x = stack.pop()
                output[x] = i - x
            stack.append(i)
        return output                

            