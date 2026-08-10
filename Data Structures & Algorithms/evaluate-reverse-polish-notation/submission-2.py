class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in ops:
                val2 = stack.pop()
                val1= stack.pop()
                if token == '+':
                    stack.append(int(val1) + int(val2))
                elif token == '-':
                    stack.append(int(val1) - int(val2))
                elif token == '*':
                    stack.append(int(val1) * int(val2))
                elif token == '/':
                    stack.append(int(int(val1) / int(val2)))
            else:
                stack.append(token)
        return int(stack.pop())
