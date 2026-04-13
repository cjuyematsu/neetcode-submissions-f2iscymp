class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k1 = k % n
        nums[:] = nums[n - k1:] + nums[:n - k1]
