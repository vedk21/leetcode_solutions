# Problem: Given a matrix A, return the transpose of A. The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

# Sample: A = [[1,2,3],[4,5,6],[7,8,9]], Output: [[1,4,7],[2,5,8],[3,6,9]]

from typing import List

class Solution:
  def transpose(self, A: List[List[int]]) -> List[List[int]]:
    R, C = len(A), len(A[0])
    ans = [[None] * R for _ in range(C)]
    for r, row in enumerate(A):
        for c, val in enumerate(row):
            ans[c][r] = val
                        
    return ans

solution = Solution()
print(solution.transpose([[1,2,3],[4,5,6]]))
