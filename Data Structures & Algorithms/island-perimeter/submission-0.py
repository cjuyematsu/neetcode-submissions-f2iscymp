class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        been = set()
        n = len(grid)
        m = len(grid[0])
        self.perimeter = 0

        def dfs(x, y):
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            been.add((x,y))
            neighbors = 0

            for dx, dy in d:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    if grid[new_x][new_y] == 1:
                        neighbors += 1
                    
                    if (new_x, new_y) not in been and grid[new_x][new_y] == 1:
                        been.add((new_x, new_y))
                        dfs(new_x, new_y)
                    
            self.perimeter += (4 - neighbors)
            print(self.perimeter)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return self.perimeter
        