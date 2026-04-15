class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        self.sol = 0

        def backTrack(row):
            if row == n:
                self.sol += 1
                return

            for col in range(n):
                if self.canPlace(board, row, col):
                    board[row][col] = "Q"
                    backTrack(row + 1)
                    board[row][col] = "."

        backTrack(0)

        return self.sol

    def canPlace(self, board, x, y):
        n = len(board)
        m = len(board[0])

        for i in range(n):
            if board[i][y] == "Q":
                return False

        for j in range(m):
            if board[x][j] == "Q":
                return False

        i, j = x + 1, y + 1
        while i < n and j < m:
            if board[i][j] == "Q":
                return False
            
            i += 1
            j += 1

        i, j = x + 1, y - 1
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            
            i += 1
            j -= 1

        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            
            i -= 1
            j -= 1

        i, j = x - 1, y + 1
        while i >= 0 and j < m:
            if board[i][j] == "Q":
                return False
            
            i -= 1
            j += 1

        return True
