# Problem: A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum. Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

# Sample: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]], Output: 1

from typing import List

class Solution:
  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    ans = 0
		
    for r in range(2, len(grid)):
      for c in range(2, len(grid[0])):
        subgrid = [grid[row][c - 2:c + 1] for row in range(r - 2, r + 1)]
        if self.is_magic_square(subgrid):
          ans += 1
    return ans

  def is_magic_square(self, M):
    NUMS_1_to_9 = set(x for x in range(1, 9 + 1))
    s = sum(M[0])
    M_reversed = [row[::-1] for row in M]

    rows_valid = all(sum(row) == s for row in M)
    cols_valid = all(sum(cols) == s for cols in zip(*M))
    diagonal1_valid = s == sum(M[x][x] for x in range(3))
    diagonal2_valid = s == sum(M_reversed[x][x] for x in range(3))
    uniqueness_valid = NUMS_1_to_9 == set(M[0] + M[1] + M[2])

    return rows_valid and cols_valid and diagonal1_valid and diagonal2_valid and uniqueness_valid

solution = Solution()
print(solution.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
