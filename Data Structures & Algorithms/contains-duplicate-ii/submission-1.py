class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        min_window = min(len(nums), k + 1)

        for i in range(min_window):
            if nums[i] in seen:
                return True

            seen.add(nums[i])
            
        for i in range(k + 1, len(nums)):
            seen.remove(nums[i - k - 1])
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])
        
        return False