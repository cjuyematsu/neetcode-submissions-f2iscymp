class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

        res = []

        if len(digits) == 0:
            return []
        
        def backTrack(cur, start):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            
            for i in range(start, len(digits)):
                for letter in phone[digits[i]]:
                    cur.append(letter)
                    backTrack(cur, i + 1)
                    cur.pop()
            
        backTrack([], 0)

        return res
                
