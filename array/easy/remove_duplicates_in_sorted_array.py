# Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Sample: nums = [1,1,3,4,5,6,6], Output: 5

from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:

    i = 0
    for num in nums:
      if num != nums[i]:
        i += 1
        nums[i] = num
        
    return i + 1

solution = Solution()
print(solution.removeDuplicates([-1,-1,1,1,1,2]))
