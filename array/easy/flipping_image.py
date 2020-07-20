# Problem: Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image. To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1]. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Sample: A = [[1,1,0],[1,0,1],[0,0,0]], Output: [[1,0,0],[0,1,0],[1,1,1]]

from typing import List

class Solution:
  def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for row in A:
      start, end = 0, len(row) - 1
      while (start < end):
        if row[start] == row[end]:
          row[start] = 1 if row[start] == 0 else 0
          row[end] = 1 if row[end] == 0 else 0
        start += 1
        end -= 1

      if start == end:
        row[start] = 1 if row[start] == 0 else 0
    
    return A

solution = Solution()
print(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
