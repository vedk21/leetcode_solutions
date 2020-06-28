# Problem: Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Sample: nums = [1,2,3,1,2,3], k = 2, Output: false
# nums = [1,0,1,1], k = 1, Output: true

from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    map = {}
    for i in range(len(nums)):
      if nums[i] in map:
        if abs(i - map[nums[i]]) <= k:
          return True
        else:
          map[nums[i]] = i
      else:
        map[nums[i]] = i
    
    return False

solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 2))
