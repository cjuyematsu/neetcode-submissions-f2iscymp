from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        n = len(nums)
        sol = []

        for k, v in freqs.items():
            if(v > n // 3):
                sol.append(k)
            
        return sol
        