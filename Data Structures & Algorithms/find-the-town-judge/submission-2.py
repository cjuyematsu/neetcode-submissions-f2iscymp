class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trusts = [0] * (n + 1)

        for a, b in trust:
            trusted[b] += 1
            trusts[a] += 1
            
        for i in range(1, n + 1):
            if trusted[i] == (n - 1) and trusts[i] == 0:
                return i

        return -1
