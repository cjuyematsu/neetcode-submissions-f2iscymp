class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = []
        n = len(nums)
        nums.sort()

        def backTrack(cur, cur_len, start):
            if cur_len > n:
                return

            arr.append(cur[:])

            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                cur.append(nums[i])
                backTrack(cur, cur_len + 1, i + 1)
                cur.pop()

        backTrack([], 0, 0)

        return arr
