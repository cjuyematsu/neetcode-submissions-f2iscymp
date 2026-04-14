class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = []
        n = len(nums)
        added = set()

        def backTrack(cur: List[int], seen: set()):
            if len(cur) == n and tuple(cur) not in added:
                arr.append(cur[:])
                added.add(tuple(cur))
                return
            
            for i in range(n):
                if i in seen:
                    continue

                seen.add(i)
                cur.append(nums[i])
                backTrack(cur, seen)
                cur.pop()
                seen.remove(i)
            
        backTrack([], set())

        return arr
