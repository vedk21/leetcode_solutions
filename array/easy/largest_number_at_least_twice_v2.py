# Problem: In a given integer array nums, there is always exactly one largest element. Find whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, otherwise return -1.

# Sample: nums = [3, 6, 1, 0], Output: 1

from typing import List

class Solution:
  def dominantIndex(self, nums: List[int]) -> int:
      
    if len(nums) == 1:
      return 0
    
    numsCp = nums.copy()
    # sort the nums arr
    numsCp.sort(reverse=True)
    
    if len(numsCp) > 1 and (numsCp[0] / 2) <= (numsCp[0] - numsCp[1]):
      return self.returnIndex(numsCp[0], nums)
    
    return -1
      
  def returnIndex(self, num: int, nums: List[int]) -> int:
    for i in range(0, len(nums)):
      if num == nums[i]:
        return i

solution = Solution()
print(solution.dominantIndex([2,3,6]))
