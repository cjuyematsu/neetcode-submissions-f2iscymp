class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                el = board[i][j]
                if(el == "."):
                    continue

                if(el in rows[i] or el in cols[j] or el in boxes[(i // 3) * 3 + (j // 3)]):
                    return False

                rows[i].add(el)
                cols[j].add(el)
                boxes[(i // 3) * 3 + j // 3].add(el)

        return True
               
            