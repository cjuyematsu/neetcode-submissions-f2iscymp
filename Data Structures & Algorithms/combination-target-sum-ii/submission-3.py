class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.arr = []
        candidates.sort()

        def backTrack(cur, cur_sum, start):
            if cur_sum == target:
                self.arr.append(cur[:])
                return
            
            if cur_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 

                cur.append(candidates[i])
                backTrack(cur, cur_sum + candidates[i], i + 1)
                cur.pop()


        backTrack([], 0, 0)
        return self.arr
