class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        been = set()

        def dfs(x, y):
            if (x, y) in been:
                return 

            been.add((x, y))

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                grid[x][y] = "X"

            else:
                return

            d = [(0,1), (1,0), (0, -1), (-1, 0)]

            for dx, dy in d:
                dfs(x + dx, y + dy)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
                        
        return num_islands
