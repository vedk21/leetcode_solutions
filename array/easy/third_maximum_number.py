# Problem: Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Sample: nums = [2, 2, 3, 1], Output: 1

from typing import List

class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    nums = list(set(nums)) # remove duplicates
    nums = sorted(nums, reverse=True) # sort desc
    if len(nums) >= 3:
      return nums[2] # return 3rd max
    else: # return max
      return nums[0]

solution = Solution()
print(solution.thirdMax([2,2,3,1]))
