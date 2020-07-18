# Problem: A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element. Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# Sample: matrix = [[1,2,3,4], [5,1,2,3], [9,5,1,2]], Output: True

from typing import List

class Solution:
  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    for r in range(len(matrix) - 1):
      for c in range(len(matrix) - 1):
        if matrix[r+1][c+1] != matrix[r][c]:
          return False
    
    return True

solution = Solution()
print(solution.isToeplitzMatrix([[1,2,3,4], [5,1,2,3], [9,5,1,2]]))
