class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        seen = set()
        solution = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ == target:
                        els = [nums[i], nums[j], nums[left], nums[right]]
                        solution.append(els)
                        right -= 1
                        left += 1

                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left +=1 

                    elif summ > target:
                        right -= 1
                    else:
                        left += 1
            
        return solution
