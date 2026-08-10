import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a/b),
        }
        stack = []
        for token in tokens:
            if token in ops:
                val2 = stack.pop()
                val1= stack.pop()
                stack.append(ops[token](val1, val2))
            else:
                stack.append(int(token))
        return int(stack.pop())
