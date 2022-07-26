# Problem: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]], Output: [[7,4,1],[8,5,2],[9,6,3]]

from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    self.transpose(matrix)
    self.reflect(matrix)
    
  def transpose(self, matrix):
    n = len(matrix)
    for i in range(n):
      for j in range(i + 1, n):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

  def reflect(self, matrix):
    n = len(matrix)
    for i in range(n):
      for j in range(n // 2):
        matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

solution = Solution()
ls = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(ls)
print(ls)

