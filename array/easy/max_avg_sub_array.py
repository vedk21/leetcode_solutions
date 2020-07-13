# Problem: Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

# Sample: nums = [1,12,-5,-6,50,3], k = 4, Output: 12.75

from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    sum = 0
    for i in range(k):
      sum += nums[i]
    
    res = sum
    for i in range(k, len(nums)):
      sum += nums[i] - nums[i - k]
      res = max(res, sum)

    return res/k

solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
