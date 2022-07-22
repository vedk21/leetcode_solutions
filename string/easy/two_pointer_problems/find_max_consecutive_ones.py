#Problem: Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Sample: numbers = [1,0,1,1,1,0,1,1], Output: 3

from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    result = 0

    for i in range(0, len(nums)):
      if nums[i] == 0:
        count = 0
      
      else:
        count += 1
        result = max(result, count)
    
    return result

solution = Solution()
print(solution.findMaxConsecutiveOnes([1,0,0,1,1]))
