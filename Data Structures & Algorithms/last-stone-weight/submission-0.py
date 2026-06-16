import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)

        while q:
            if len(q) == 1:
                return -q[0]
            
            heaviest_stone = -heapq.heappop(q)
            second_heaviest = -heapq.heappop(q)

            collision = heaviest_stone - second_heaviest

            if collision != 0:
                heapq.heappush(q, -collision)            
        
        return 0

        
