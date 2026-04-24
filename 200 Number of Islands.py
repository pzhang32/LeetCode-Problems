class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.searchAdjacentLand(i, j, grid)
        return count
    
    def searchAdjacentLand(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        
        if grid[i][j] == "0":
            return
        else:
            grid[i][j] = "0"

        self.searchAdjacentLand(i-1, j, grid)
        self.searchAdjacentLand(i+1, j, grid)
        self.searchAdjacentLand(i, j-1, grid)
        self.searchAdjacentLand(i, j+1, grid)
