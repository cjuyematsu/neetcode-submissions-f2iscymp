class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while(lo < hi):
            if(numbers[hi] + numbers[lo] > target):
                hi -= 1

            elif(numbers[hi] + numbers[lo] < target):
                lo += 1

            else:
                return [lo + 1, hi + 1]

        return [-1, -1]