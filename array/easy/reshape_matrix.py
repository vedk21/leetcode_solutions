# Problem: In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.You are given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively. The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were. If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# Sample: nums = [[1,2], [3,4]], r = 1, c = 4 Output: [[1,2,3,4]]

from typing import List
from collections import deque

class Solution:
  def matrixReshapeUsingQueue(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:

    if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
      return nums
    
    queue = deque()
    result = []
    for i in range(len(nums)):
      for j in range(len(nums[i])):
        queue.append(nums[i][j])

    for i in range(r):
      result.append([])
      for j in range(c):
        result[i].append(queue.popleft())
    
    return result

  def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:

    if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
      return nums

    result = []
    count = 0
    for i in range(len(nums)):
      for j in range(len(nums[i])):
        if len(result) <= count // c:
          result.append([])
        result[count // c].append(nums[i][j])
        count += 1
    
    return result

solution = Solution()
print(solution.matrixReshape([[1,2], [3,4]], 4, 1))
