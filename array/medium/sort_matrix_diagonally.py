# Problem: Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]], Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

from typing import List

class Solution:
  def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    # xl, yl = len(mat), len(mat[0])
    # t = [ [] for i in range( xl+yl ) ]
    
    # for i in range(xl):
    #   for j in range(yl):
    #     t[i - j].append(mat[i][j])
            
    # for l in t:
    #   l.sort(reverse=True)

    # for i in range(xl):
    #   for j in range(yl):
    #     mat[i][j] = t[i-j].pop()
            
    # return mat

    m, n = len(mat), len(mat[0])
    def sort(i, j):
      vals = []
      while i < m and j < n:
        vals.append(mat[i][j])
        i += 1
        j += 1
      vals.sort()
      while i and j:
        j -= 1
        i -= 1
        mat[i][j] = vals.pop()
    for i in range(m): sort(i, 0)
    for j in range(n): sort(0, j)
    return mat

solution = Solution()
ls = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(solution.diagonalSort(ls))
