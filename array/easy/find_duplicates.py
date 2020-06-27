# Problem: Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Sample: nums = [1,2,3,1], Output: true

from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    map = {}
    for i in nums:
      if i in map:
        return True
      else:
        map[i] = 1
    
    return False

solution = Solution()
print(solution.containsDuplicate([1,2,1,4]))
