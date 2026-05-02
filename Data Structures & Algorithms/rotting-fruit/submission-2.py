from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        rotting = deque()
        n = len(grid)
        m = len(grid[0])
        steps = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_oranges += 1

                elif grid[i][j] == 2:
                    rotting.append((i, j))
                    grid[i][j] = 0
        
        if fresh_oranges == 0:
            return 0

        while rotting:
            steps += 1
            num_rotting = len(rotting)
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for _ in range(num_rotting):
                x, y = rotting.popleft()
                for dx, dy in d:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m:
                        if grid[new_x][new_y] == 1:
                            fresh_oranges -= 1
                            grid[new_x][new_y] = 0
                            rotting.append((new_x, new_y))
            
        return steps - 1 if fresh_oranges == 0 else -1

