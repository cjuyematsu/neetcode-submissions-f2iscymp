class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        lo, hi = 0, n - 1
        row = 0
        
        while (lo <= hi):
            mid = (lo + hi) // 2
            if(matrix[mid][0] <= target <= matrix[mid][m - 1]):
                row = mid
                break
            elif(target < matrix[mid][0]):
                hi = mid - 1
            else:
                lo = mid + 1


        lo, hi = 0, m - 1

        while(lo <= hi):
            mid = (lo + hi) // 2

            if(matrix[row][mid] == target):
                return True
            elif(matrix[row][mid] > target):
                hi = mid - 1
            else:
                lo = mid + 1 

        return False
