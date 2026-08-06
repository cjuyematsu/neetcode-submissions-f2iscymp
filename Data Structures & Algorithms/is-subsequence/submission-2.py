class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        
        if len(s) > len(t):
            return False

        for i in range(len(t)):
            if p1 >= (len(s) - 1):
                return True
            
            if s[p1] == t[i]:
                p1 += 1
            
        return True if p1 > (len(s) - 1) else False