class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        starts = []
        self.found = False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    starts.append([i, j])
                
        def backTrack(cur, x, y, word_index, visited):
            if "".join(cur) == word:
                self.found = True
                return
            
            if len(cur) >= len(word):
                return
                        
            if x + 1 < n and (x + 1, y) not in visited:
                if board[x + 1][y] == word[word_index]:
                    visited.add((x + 1, y))
                    cur.append(board[x + 1][y])
                    backTrack(cur, x + 1, y, word_index + 1, visited)
                    cur.pop()
                    visited.remove((x + 1, y))

            if y + 1 < m and (x, y + 1) not in visited:
                if board[x][y + 1] == word[word_index]:
                    visited.add((x, y + 1))
                    cur.append(board[x][y + 1])
                    backTrack(cur, x, y + 1, word_index + 1, visited)
                    cur.pop()
                    visited.remove((x, y + 1))

            if x - 1 >= 0 and (x - 1, y) not in visited:
                if board[x - 1][y] == word[word_index]:
                    visited.add((x - 1, y))
                    cur.append(board[x - 1][y])
                    backTrack(cur, x - 1, y, word_index + 1, visited)
                    cur.pop()
                    visited.remove((x - 1, y))

            if y - 1 >= 0 and (x, y - 1) not in visited:
                if board[x][y - 1] == word[word_index]:
                    visited.add((x, y - 1))
                    cur.append(board[x][y - 1])
                    backTrack(cur, x, y - 1, word_index + 1, visited)
                    cur.pop()
                    visited.remove((x, y - 1))

        for start_x, start_y in starts:
            backTrack([word[0]], start_x, start_y, 1, {(start_x, start_y)})

        return self.found
