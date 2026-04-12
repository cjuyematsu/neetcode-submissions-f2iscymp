class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        sol = []

        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
                
            left = i + 1
            right = n - 1
            while(left < right):
                cur_sum = nums[i] + nums[left] + nums[right]
                if(cur_sum > 0):
                    right -= 1
                elif(cur_sum < 0):
                    left += 1
                else:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while(left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while(right > left and nums[right] == nums[right + 1]):
                        right -= 1

        return sol