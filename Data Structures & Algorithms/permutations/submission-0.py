class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.arr = []

        def backTrack(cur, cur_len):
            if cur_len > n:
                return
            elif cur_len == n:
                self.arr.append(cur[:])
                return

            for i in range(n):
                if nums[i] in set(cur):
                    continue

                cur.append(nums[i])
                backTrack(cur, cur_len + 1)
                cur.pop()

        backTrack([], 0)

        return self.arr
