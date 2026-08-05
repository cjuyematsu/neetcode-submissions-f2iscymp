class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        sol = [-1] * len(arr)
        max_seen = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            sol[i] = max_seen
            max_seen = max(max_seen, arr[i])

        return sol