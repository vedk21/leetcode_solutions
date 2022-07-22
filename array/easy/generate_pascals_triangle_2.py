# Problem: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# Sample: rowIndex = 1, Output: [1,1]

from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    result = [[1]]

    rowNums = rowIndex

    if rowIndex == 0:
      return result[rowNums]
    elif rowIndex == 1:
      result.append([1,1])
      return result[rowNums]
    else:
      result.append([1,1])
      prevRow = 1
      while rowIndex > 1:
        i = 1
        nums = [1]
        while i < len(result[prevRow]):
          nums.append(result[prevRow][i] + result[prevRow][i - 1])
          i += 1
        
        nums.append(1)
        result.append(nums)
        prevRow += 1

        rowIndex -= 1
    
      return result[rowNums]

solution = Solution()
print(solution.getRow(5))