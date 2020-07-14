# problem: Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Sample: nums = [1,3,5,4,7], Output: 3

from typing import List

class Solution:
  def findLengthOfLCIS(self, nums: List[int]) -> int:
    if len(nums) > 0:
      count, maxSeq = 1, 1
      for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
          count += 1
        else:
          count = 1
        maxSeq = max(count, maxSeq)
      
      return maxSeq
    else:
      return 0

solution = Solution()
print(solution.findLengthOfLCIS([1,2,3,1,2,5,6,7,8]))
