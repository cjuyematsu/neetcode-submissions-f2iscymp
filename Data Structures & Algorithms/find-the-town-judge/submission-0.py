class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trusts = [0] * (n + 1)
        pot_judges = []

        for a, b in trust:
            trusted[b] += 1
            trusts[a] += 1
            
            if trusted[b] == n - 1:
                pot_judges.append(b)
            
        for pot_judge in pot_judges:
            if trusts[pot_judge] == 0:
                return pot_judge

        return -1
