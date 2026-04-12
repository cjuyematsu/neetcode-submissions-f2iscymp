class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while(lo < hi):
            res = numbers[hi] + numbers[lo]
            if(res == target):
                return [lo + 1, hi + 1]

            elif(res < target):
                lo += 1

            else:
                hi -= 1

        return [-1, -1]