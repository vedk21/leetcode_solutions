#Problem: Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Sample: numRows = 4, Output: [[1], [1,1], [1,2,1], [1,3,3,1]]

from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    
    result = [[1]]

    if numRows == 1:
      return result
    elif numRows == 2:
      result.append([1,1])
      return result
    else:
      result.append([1,1])
      prevRow = 1
      while numRows > 2:
        i = 1
        nums = [1]
        while i < len(result[prevRow]):
          nums.append(result[prevRow][i] + result[prevRow][i - 1])
          i += 1
        
        nums.append(1)
        result.append(nums)
        prevRow += 1

        numRows -= 1
    
      return result


solution = Solution()
print(solution.generate(10))
