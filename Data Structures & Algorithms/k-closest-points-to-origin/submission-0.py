import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for i, (x, y) in enumerate(points):
            distance = math.sqrt(x**2 + y**2)

            heapq.heappush(heap, (-distance, i))

            if len(heap) > k:
                heapq.heappop(heap)

        for _, index in heap:
            result.append(points[index])

        return result