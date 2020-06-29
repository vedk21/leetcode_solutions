# Problem: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Sample: nums = [0,1,0,3,12], Output: [1,3,12,0,0]

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nonZeroElementIndex = 0
    for i in range(len(nums)):
      if (nums[i] != 0):
        nums[nonZeroElementIndex], nums[i] = nums[i], nums[nonZeroElementIndex]
        nonZeroElementIndex += 1

solution = Solution()
ls = [0,1,0,3,12,0,2]
solution.moveZeroes(ls)
print(ls)
