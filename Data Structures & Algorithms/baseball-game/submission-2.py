class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        tot = 0

        for op in operations:
            if op.isnumeric() or op.startswith('-') and op[1:].isnumeric():
                stack.append(int(op))
                tot += int(op)
            elif op == '+':
                prev1 = stack.pop() if stack else 0
                prev2 = stack.pop() if stack else 0
                tot += prev1 + prev2
                stack.append(prev2)
                stack.append(prev1)
                stack.append(prev1 + prev2)
            elif op == 'D':
                if stack:
                    prev = stack.pop()
                    tot += prev * 2
                    stack.append(prev)
                    stack.append(prev * 2)
            else:
                prev = stack.pop() if stack else 0
                tot -= prev
            
        return tot