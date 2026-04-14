class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.arr = []

        def backTrack(cur, start):
            self.arr.append(cur[:])

            for i in range(start, len(nums)):
                cur.append(nums[i])
                backTrack(cur, i + 1)
                cur.pop()

        backTrack([], 0)

        return self.arr
