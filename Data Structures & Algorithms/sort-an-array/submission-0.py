import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sol = []
        heapq.heapify(nums)

        while(nums):
            el = heapq.heappop(nums)
            sol.append(el)

        return sol