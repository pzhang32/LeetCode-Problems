class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = self.calculateArea(i, j, grid)
                    if area > max_area:
                        max_area = area

        return max_area
    
    def calculateArea(self, i, j, grid) -> int:
        area = 0
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
            if grid[i][j] == 1:
                area += 1
                grid[i][j] = 0
            else:
                return 0
        else:
            return 0
        
        area += self.calculateArea(i+1, j, grid)
        area += self.calculateArea(i-1, j, grid)
        area += self.calculateArea(i, j+1, grid)
        area += self.calculateArea(i, j-1, grid)

        return area
       

if __name__ == "__main__":
    grid = [[1,1]]
    sol = Solution()
    print(sol.maxAreaOfIsland(grid))