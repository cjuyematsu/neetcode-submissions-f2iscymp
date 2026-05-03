class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_present = [0] * len(nums)

        for num in nums:
            if num_present[num] == 1:
                return num
            else:
                num_present[num] = 1
