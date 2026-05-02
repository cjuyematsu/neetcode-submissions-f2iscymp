class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        been = set()

        def dfs(x, y):
            been.add((x, y))

            if grid[x][y] == "1":
                grid[x][y] = "X"

            else:
                return

            d = [(0,1), (1,0), (0, -1), (-1, 0)]

            for dx, dy in d:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and (x + dx, y + dy) not in been:
                    dfs(x + dx, y + dy)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
                        
        return num_islands
