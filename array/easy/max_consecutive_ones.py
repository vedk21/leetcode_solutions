# Problem: Given a binary array, find the maximum number of consecutive 1s in this array.

# Sample nums = [1,1,0,1,1,1], Output: 3

from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    final_count = 0
    for i in range(len(nums)):
      if nums[i] == 1:
        count += 1
      else:
        final_count = max(count, final_count)
        count = 0

    final_count = max(count, final_count)
    
    return final_count

solution = Solution()
print(solution.findMaxConsecutiveOnes([0,0,0,1]))
