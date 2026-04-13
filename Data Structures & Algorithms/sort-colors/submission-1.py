class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = n - 1    

        for i in range(n):
            while right >= 0 and nums[right] == 2:
                right -= 1

            if(right <= i):
                break 
            
            if nums[right] != 2 and nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]

        left = 0
        for i in range(right, 0, -1):
            while left < n and nums[left] == 0:
                left += 1

            if left >= i:
                break 
            
            if nums[left] != 0 and nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
