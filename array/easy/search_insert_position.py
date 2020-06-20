# Problem: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

# Sample: Given nums = [1,3,5,6], target = 5

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      for i in range(len(nums)):
        if nums[i] >= target:
          return i
      
      return len(nums)

solution = Solution()
print(solution.searchInsert([1,3,5,6], 6))
