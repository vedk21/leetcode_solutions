# Problem: Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element. We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# Sample: nums = [4,2,3], Output: True

from typing import List

class Solution:
  def checkPossibility(self, nums: List[int]) -> bool:
    idx = None
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        if idx is not None:
          return False

        idx = i

    return (idx is None or idx == 0 or idx == len(nums) - 2 or nums[idx - 1] <= nums[idx + 1] or nums[idx] <= nums[idx + 2])

solution = Solution()
print(solution.checkPossibility([-1,0,3,6,8,10]))
