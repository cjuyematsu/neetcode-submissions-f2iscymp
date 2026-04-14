from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = []
        n = len(nums)
        counts = Counter(nums)

        def backTrack(cur):
            if len(cur) == n:
                arr.append(cur[:])
                return
            
            for num in counts:
                if counts[num] > 0:
                    cur.append(num)
                    counts[num] -= 1
                    backTrack(cur)
                    cur.pop()
                    counts[num] += 1

                
        backTrack([])

        return arr
