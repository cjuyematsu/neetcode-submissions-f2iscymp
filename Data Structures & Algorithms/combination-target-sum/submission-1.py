class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.arr = []

        def backTrack(cur, cur_sum, start_index):
            if cur_sum == target:
                self.arr.append(cur[:])
            if cur_sum > target:
                return
            
            for i in range(start_index, len(nums)):
                cur.append(nums[i])
                backTrack(cur, cur_sum + nums[i], i)
                cur.pop()
            
        backTrack([], 0, 0)

        return self.arr
