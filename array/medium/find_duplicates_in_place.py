# Probblem: Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
# Input: nums = [4,3,2,7,8,2,3,1], Output: [2,3]

from typing import List

class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    result = []
    
    for i in range(len(nums)):
      val = abs(nums[i]) - 1
      if nums[val] < 0:
        result.append(val + 1)
      else:
        nums[val] = -nums[val]
    
    return result

solution = Solution()
ls = [4,3,2,7,8,2,3,7]
print(solution.findDuplicates(ls))
