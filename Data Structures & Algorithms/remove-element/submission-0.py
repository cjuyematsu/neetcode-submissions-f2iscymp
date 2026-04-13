class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]

            elif nums[right] == val and nums[left] != val:
                right -= 1
                left += 1

            elif nums[right] == val:
                right -= 1
            
            else:
                left += 1

        nums = nums[len(nums) - right - 1:]

        return len(nums)
            