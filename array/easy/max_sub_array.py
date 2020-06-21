# Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Sample: Given nums = [-2,1,-3,4,-1,2,1,-5,4]

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      for i in range(1, len(nums)):
        current_sum = max(nums[i], (nums[i] + current_sum))
        max_sum = max(current_sum, max_sum)
      return max_sum

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,8,8,8]))
