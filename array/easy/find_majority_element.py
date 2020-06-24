# Problem: Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times. You may assume that the array is non-empty and the majority element always exist in the array.

# Sample: nums = [3,2,3], Output: 3

from typing import List
from collections import Counter

class Solution:
    def majorityElementUsingHashMap(self, nums: List[int]) -> int:
      map = Counter(nums)
      return max(map.keys(), key=map.get)

    def majorityElementUsingBoyerMooreAlgorithm(self, nums: List[int]) -> int:
      count = 0
      candidate = None
      for num in nums:
        if count == 0:
          candidate = num
        if num == candidate:
          count += 1
        else:
          count -= 1

      return candidate

solution = Solution()
print(solution.majorityElementUsingBoyerMooreAlgorithm([3,5,3,5,5]))
