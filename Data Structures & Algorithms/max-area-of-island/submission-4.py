class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            count = 0

            if grid[x][y] == 1:
                grid[x][y] = 0

            for dx, dy in d:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                    count += 1 + dfs(new_x, new_y)
            
            return count
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur = dfs(i, j)
                    max_area = max(max_area, cur + 1)
                
        return max_area
