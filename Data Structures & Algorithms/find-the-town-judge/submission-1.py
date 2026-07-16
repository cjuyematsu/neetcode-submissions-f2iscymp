class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trusts = [0] * (n + 1)
        pot_judge = float('inf')

        for a, b in trust:
            trusted[b] += 1
            trusts[a] += 1
            
            if trusted[b] == n - 1:
                pot_judge = b
            
        if pot_judge == float('inf'):
            return -1
        
        if trusts[pot_judge] == 0:
            return pot_judge

        return -1            
        
