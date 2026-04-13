class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.summs = [[0] * m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i - 1 >= 0 and j - 1 >= 0:
                    self.summs[i][j] = self.summs[i - 1][j] + self.summs[i][j - 1] - self.summs[i - 1][j - 1] + matrix[i][j]
                elif j - 1 >= 0:
                    self.summs[i][j] = self.summs[i][j - 1] + matrix[i][j]
                elif i - 1 >= 0:
                    self.summs[i][j] = self.summs[i - 1][j] + matrix[i][j]
                else:
                    self.summs[i][j] = matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.summs[row2][col2]

        above = self.summs[row1 - 1][col2] if row1 - 1 >= 0 else 0
        left = self.summs[row2][col1 - 1] if col1 - 1 >= 0 else 0
        corner = self.summs[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0

        return total - above - left + corner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)