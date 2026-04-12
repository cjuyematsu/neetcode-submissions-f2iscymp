class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        multi = 1

        for i in range(len(nums)):
            sol[i] *= multi
            multi *= nums[i]

        multi = 1

        for i in range(len(nums) - 1, -1, -1):
            sol[i] *= multi
            multi *= nums[i]

        return sol