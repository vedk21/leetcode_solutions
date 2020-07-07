# Problem: Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too. You need to find the shortest such subarray and output its length.

# Sample: Input: [2, 6, 4, 8, 10, 9, 15], Output: 5

from typing import List
from collections import deque
import sys

class Solution:
  def findUnsortedSubarrayUsingStack(self, nums: List[int]) -> int:
    stack = deque()
    left = len(nums) - 1
    right = 0

    for i in range(len(nums)):
      while (len(stack) != 0 and nums[stack[-1]] > nums[i]):
        left = min(left, stack.pop())
      stack.append(i)

    for i in range(len(nums) - 1, -1, -1):
      while (len(stack) != 0 and nums[stack[-1]] < nums[i]):
        right = max(right, stack.pop())
      stack.append(i)

    return  (right - left + 1) if right - left > 0 else 0

  def findUnsortedSubarray(self, nums: List[int]) -> int:
    minNumber = sys.maxsize - 1
    maxNumber = -sys.maxsize - 1
    flag = False

    for i in range(1, len(nums)):
      if nums[i] < nums[i - 1]:
        flag = True
      
      if flag:
        minNumber = min(minNumber, nums[i])

    flag = False

    for i in range(len(nums) - 2, -1, -1):
      if nums[i] > nums[i + 1]:
        flag = True
      
      if flag:
        maxNumber = max(maxNumber, nums[i])
    
    left = 0
    right = len(nums) - 1

    while(left < len(nums)):
      if minNumber < nums[left]:
        break
      left += 1
    
    while(right >= 0):
      if maxNumber > nums[right]:
        break
      right -= 1
    
    return (right - left + 1) if right - left > 0 else 0

solution = Solution()
print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 12, 15]))
