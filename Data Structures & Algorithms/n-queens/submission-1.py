class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        solution = []

        def backTrack(row):
            if row == n:
                solution.append(["".join(row) for row in board])
                return

            for col in range(n):
                if self.canPlace(board, row, col):
                    board[row][col] = "Q"
                    backTrack(row + 1)
                    board[row][col] = "."

        backTrack(0)

        return solution
        
    def canPlace(self, board, x, y):
        n = len(board)
        m = len(board[0])

        for i in range(len(board[0])):
            if board[i][y] == 'Q':
                return False

        # diagonals 
        i, j = x + 1, y + 1
        while i < n and j < m:
            if board[i][j] == 'Q':
                return False
            i += 1
            j += 1
        
        i, j = x + 1, y - 1
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False

            i += 1
            j -= 1

        i, j = x - 1, y + 1
        while i >= 0 and j < m:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            
            i -= 1
            j -= 1

        return True
