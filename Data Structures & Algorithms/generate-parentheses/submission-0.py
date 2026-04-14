class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []

        def backTrack(cur, num_open, num_close):
            if num_open == num_close and num_open == n:
                arr.append("".join(cur))
                return
            
            if num_open == num_close:
                cur.append('(')
                backTrack(cur, num_open + 1, num_close)
                cur.pop()
            elif num_open == n:
                cur.append(')')
                backTrack(cur, num_open, num_close + 1)
                cur.pop()
            else:
                cur.append('(')
                backTrack(cur, num_open + 1, num_close)
                cur.pop()                    

                cur.append(')')
                backTrack(cur, num_open, num_close + 1)
                cur.pop()

        backTrack([], 0, 0)

        return arr
        