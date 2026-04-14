class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.arr = []

        def backTrack(cur, cur_len, start):
            if cur_len > k:
                return 

            if cur_len == k:
                self.arr.append(cur[:])
                return

            for i in range(start, n + 1):
                cur.append(i)
                backTrack(cur, cur_len + 1, i + 1)
                cur.pop()
            
        backTrack([], 0, 1)

        return self.arr
