# Problem: In a given integer array nums, there is always exactly one largest element. Find whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, otherwise return -1.

# Sample: nums = [3, 6, 1, 0], Output: 1

from typing import List

class Solution:
  def dominantIndex(self, nums: List[int]) -> int:
    maxIndex, maxNum = 0, nums[0]

    for i in range(1, len(nums)):
      if nums[i] > maxNum:
        if maxNum <= nums[i] // 2:
          maxIndex = i
        else:
          maxIndex = -1
        maxNum = nums[i]
      else:
        if nums[i] > maxNum // 2:
          maxIndex = -1
    
    return maxIndex

solution = Solution()
print(solution.dominantIndex([2,3,6]))
