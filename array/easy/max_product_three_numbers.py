# Problem: Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Sample: Input: [1,2,3], Output: 6

from typing import List
import sys

class Solution:
  def maximumProduct(self, nums: List[int]) -> int:
    min1 = sys.maxsize
    min2 = sys.maxsize
    max1 = -sys.maxsize
    max2 = -sys.maxsize
    max3 = -sys.maxsize

    for n in nums:
      if (n <= min1):
        min2 = min1
        min1 = n
      elif (n <= min2):
        min2 = n
      
      if (n >= max1):
        max3 = max2
        max2 = max1
        max1 = n
      elif (n >= max2):
        max3 = max2
        max2 = n
      elif (n >= max3):
        max3 = n
      
    return max((min1 * min2 * max1), (max1 * max2 * max3))


solution = Solution()
print(solution.maximumProduct([1,2,3]))
