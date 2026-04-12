class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxx_len = 0
        cur_len = 0

        for num in nums:
            if num - 1 in numbers:
                continue

            cur = num
            while(cur + 1 in numbers):
                cur_len += 1
                cur += 1

            maxx_len = max(cur_len + 1, maxx_len)
            cur_len = 0

        return maxx_len
            