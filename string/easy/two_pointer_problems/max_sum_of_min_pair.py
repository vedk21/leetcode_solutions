#Problem: Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Sample: nums = [1,-5,2,6,-8,4], Output: 3 [-8,-5,1,2,4,6] (-8)+(1)+(4)=-3

from typing import List

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    # sort in asc order
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
      sum += nums[i]

    return sum


solution = Solution()
print(solution.arrayPairSum([1,-5,2,6,-8,4]))
