class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place_index = 1
        search_index = 1
        seen = {nums[0]}

        while search_index < len(nums):
            if nums[search_index] not in seen:
                nums[place_index] = nums[search_index]
                place_index += 1
                seen.add(nums[search_index])
            
            search_index += 1

        return place_index