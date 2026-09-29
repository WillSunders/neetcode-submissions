class MyStack:
    from collections import deque
    def __init__(self):
        self.vals = deque()

    def push(self, x: int) -> None:
        self.vals.append(x)

    def pop(self) -> int:
        q2 = deque()
        out = 0
        while len(self.vals) > 1:
            q2.append(self.vals.popleft())
        out = self.vals.popleft()
        self.vals = q2
        return out

    def top(self) -> int:
        q2 = deque()
        out = 0
        while len(self.vals) > 1:
            q2.append(self.vals.popleft())
        out = self.vals.popleft()
        q2.append(out)
        self.vals = q2
        return out

    def empty(self) -> bool:
        if not self.vals:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()