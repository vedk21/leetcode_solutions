# Problem: There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c. 
# Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

# Sample: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], Output: 35

from typing import List, Dict

class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    count = 0

    buildingHeightDict = self.findMinVertically(grid)

    for i in range(len(grid)):
      for j in range(len(grid[i])):
        count += buildingHeightDict[(i, j)] - grid[i][j]
    
    return count
    

  def findMinVertically(self, grid: List[List[int]]) -> Dict:
    row = 0
    buildingHeightDict = {}

    while row < len(grid):
      col = 0
      while col < len(grid[row]):
        colMax, i = 0, 0
        while i < len(grid):
          colMax = grid[i][col] if grid[i][col] > colMax else colMax
          i += 1

        buildingHeightDict[(row, col)] = min(max(grid[row]), colMax)
        col += 1
      row += 1
        
    
    return buildingHeightDict

solution = Solution()
ls = [
  [59,88,44],
  [ 3,18,38],
  [21,26,51]
] 
print(solution.maxIncreaseKeepingSkyline(ls))

#0+0+7+35+20+0+30+25+0
