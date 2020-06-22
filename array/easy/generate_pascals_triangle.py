# Problem: Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Sample: numRows = 5

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      if numRows > 1:
        triangle = [[1], [1,1]] # initialize with first and second point
        for i in range(2, numRows):
          row = []
          for j in range(i + 1):
            if (j - 1) >= 0 and j < len(triangle[i - 1]):
              row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            else:
              row.append(1)
          triangle.append(row)

        return triangle
      elif numRows == 1:
        return [[1]]
      else:
        return []

solution = Solution()
print(solution.generate(0))