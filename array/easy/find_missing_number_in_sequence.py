# Problem: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Sample: nums = [2,6,4,9,3,5,7,0,1], Output: 8
# n(n + 1) / 2 (arithmetic sequence)

from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    # arithmetic sequence
    sum = (n * (n + 1)) // 2
    for i in nums:
      sum -= i

    return sum

solution = Solution()
print(solution.missingNumber([0,1,4,3]))
