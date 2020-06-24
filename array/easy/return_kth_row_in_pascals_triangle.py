# Problem: Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle. Note that the row index starts from 0.

# Sample: k = 3, Output: [1,3,3,1]

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
      if rowIndex > 1:
        prev_row = [1,1] # initialize with first and second point
        for i in range(2, rowIndex + 1):
          row = []
          for j in range(i + 1):
            if (j - 1) >= 0 and j < i:
              row.append(prev_row[j - 1] + prev_row[j])
            else:
              row.append(1)
          prev_row = row

        return prev_row
      elif rowIndex == 1:
        return [1,1]
      else:
        return [1]

solution = Solution()
print(solution.getRow(32))
