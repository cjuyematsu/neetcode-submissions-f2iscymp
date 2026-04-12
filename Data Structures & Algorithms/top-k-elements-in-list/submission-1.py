from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elements = Counter(nums)
        freqs = sorted(freq_elements.values())
        top_k_freqs = set(freqs[len(freqs) - k:])
        sol = []

        for num, freq in freq_elements.items():
            if(freq in top_k_freqs):
                sol.append(num)


        return sol
