class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, fast in pairs:
            time = (target - pos) / fast
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)