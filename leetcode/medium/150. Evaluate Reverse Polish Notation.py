from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculation = {
            "+": True,
            "-": True,
            "*": True,
            "/": True
        }
        que = deque()
        que.append(tokens[0])
        i = 1
        while que and i < len(tokens):
            value = calculation.get(tokens[i])
            if value:#연산일 때
                y = que.pop()
                x = que.pop()
                que.append(self.calculate(x, y, tokens[i]))
            else:
                que.append(tokens[i])
            i += 1

        return que.pop()
    
    def calculate(self, x, y, c):
        x, y = int(x), int(y)
        if c == "+":
            return x + y
        if c == "-":
            return x - y
        if c == "*":
            return x * y
        if c == "/":
            return int(x / y)
