from collections import deque

class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        self.cur_min = float('inf')

    def push(self, val: int) -> None:
        self.cur_min = min(self.cur_min, val)
        self.min_stack.append(self.cur_min)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

        self.cur_min = self.min_stack[-1] if self.min_stack else float('inf')
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
