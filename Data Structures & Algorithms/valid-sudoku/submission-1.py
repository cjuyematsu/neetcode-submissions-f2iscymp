class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    if num in rows[i]:
                        return False
                    
                    elif num in cols[j]:
                        return False
                    
                    elif num in boxes[(i // 3) + 3 * (j // 3)]:
                        return False

                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3 + 3 * (j // 3))].add(num)
        
        return True
