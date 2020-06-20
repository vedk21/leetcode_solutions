# Problem: Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Sample: Given nums = [0,1,2,2,3,0,4,2], val = 2

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      i = 0
      for j in range(len(nums)):
        if nums[j] != val:
          nums[i] = nums[j]
          i += 1
      
      return i

solution = Solution()
print(solution.removeElement([3,2,3,7,6,3,9,2,3,3,1], 3))
