class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:      
        length_nums = len(nums)

        for i in range(length_nums):
            nums.append(nums[i])

        return nums