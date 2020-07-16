# Problem: Given an array of integers nums, write a method that returns the "pivot" index of this array. We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index. If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

# Sample: nums = [1,7,3,6,5,6], Output: 3

from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    n = len(nums)
    if n > 0:
      # save the sum of prev sub-array at ith index
      for i in range(1, n):
        nums[i] = nums[i - 1] + nums[i]
      
      for i in range(n):
        if i > 0 and i < n - 1:
          if nums[i - 1] == (nums[n - 1] - nums[i]):
            return i
        elif i == 0:
          if nums[n - 1] - nums[i] == 0:
            return i
        else:
          if nums[i - 1] == 0:
            return i
      
      return -1
    else:
      return -1

solution = Solution()
print(solution.pivotIndex([1]))
