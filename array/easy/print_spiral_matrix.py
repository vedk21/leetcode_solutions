#Problem: Given an m x n matrix, return all elements of the matrix in spiral order.

# Sample: digits = [[9,9,9],[6,6,6],[3,3,3]], Output: [9, 9, 9, 6, 3, 3, 3, 6, 6]

from typing import List

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    i,j = 0, 0

    x, y = len(matrix), len(matrix[0])
    m,n = len(matrix), len(matrix[0])
    mStart, nStart = 0, 0

    result = []

    while len(result) < x * y:
      while j < n and len(result) < x * y:
        result.append(matrix[i][j])
        j += 1

      # reset j to last index
      j -= 1
      # move index to next row
      i += 1
      # remove processed row
      mStart += 1

      while i < m and len(result) < x * y:
        result.append(matrix[i][j])
        i += 1

      # reset i to last index
      i -= 1
      # move index to previous column
      j -= 1
      # remove processed column
      n -= 1

      while j >= nStart and len(result) < x * y:
        result.append(matrix[i][j])
        j -= 1

      # reset j to first index
      j += 1
      # move index to next row
      i -= 1
      # remove processed row
      m -= 1

      while i >= mStart and len(result) < x * y:
        result.append(matrix[i][j])
        i -= 1

      # reset i to last index
      i += 1
      # move index to previous row
      j += 1
      # remove processed row
      nStart += 1
    
    return result

solution = Solution()
print(solution.spiralOrder([[9]]))
