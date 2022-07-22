#Problem: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Sample: nums = [-6,3,2,6,3], val = 3, Output: [-6,2,6,,]

from typing import List

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:

    i, j = 0, 0

    while i < len(nums):

      if nums[i] != val:
        nums[j] = nums[i]
        j += 1
      
      i += 1

    return j

solution = Solution()
print(solution.removeElement([-6,3,2,6,3], 3))
