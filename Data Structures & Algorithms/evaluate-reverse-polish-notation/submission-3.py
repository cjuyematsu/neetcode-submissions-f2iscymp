import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = {'+', '-', '*', '/'}

        for token in tokens:
            if token in ops:
                second = s.pop()
                first = s.pop()
                
                if token == "+":
                    s.append(first + second)
                elif token == "-":
                    s.append(first - second)
                elif token == "*":
                    s.append(first * second)
                elif token == '/':
                    s.append(int(first / second))
            else:
                s.append(int(token))
            
        return s[0]
