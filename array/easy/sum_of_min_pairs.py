# Problem: Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Sample: nums = [1,4,3,2], Output: 4

from typing import List

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    # sort the array
    nums = sorted(nums)

    sum = 0
    for i in range(0, len(nums), 2):
      sum += nums[i]

    return sum

solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))
