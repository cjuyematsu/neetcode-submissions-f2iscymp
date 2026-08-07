from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        res = []

        for key, value in freqs.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        
        for i in range(len(heap)):
            res.append(heap[i][1])

        return res