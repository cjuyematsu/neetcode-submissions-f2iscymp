from collections import Counter
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if m < n:
            return False
        
        freq_s1 = Counter(s1)
        freq_s2 = defaultdict(int)

        for i in range(n):
            freq_s2[s2[i]] += 1

        if freq_s2 == freq_s1:
                return True
        
        for i in range(n, m):
            freq_s2[s2[i - n]] -= 1
            freq_s2[s2[i]] += 1

            if freq_s2[s2[i - n]] == 0:
                del freq_s2[s2[i - n]]

            if freq_s2 == freq_s1:
                return True
        
        return False