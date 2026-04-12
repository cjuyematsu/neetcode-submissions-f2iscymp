class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if(c not in d):
                stack.append(c)
            else:
                if(stack):
                    pair = stack.pop()
                    if(d[c] != pair):
                        return False
                else:
                    return False

        return len(stack) == 0