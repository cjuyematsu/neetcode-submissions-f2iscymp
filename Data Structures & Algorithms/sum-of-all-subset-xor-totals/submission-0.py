class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.summ = 0

        def backTrack(start_index, cur):
            adding = 0
            for num in cur:
                adding ^= num
            
            self.summ += adding

            for i in range(start_index, len(nums)):
                cur.append(nums[i])
                backTrack(i + 1, cur)
                cur.pop()
            
        
        backTrack(0, [])

        return self.summ
