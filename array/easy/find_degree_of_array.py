# Probelm: Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements. Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Sample: nums = [1, 2, 2, 3, 1], Output: 2

from typing import List

class Solution:
  def findShortestSubArray(self, nums: List[int]) -> int:
    hashMap = {}
    for i in range(len(nums)):
      if nums[i] not in hashMap:
        hashMap[nums[i]] = [i, i, 1]
      else:
        hashMap[nums[i]] = [hashMap[nums[i]][0], i, hashMap[nums[i]][2] + 1]
    
    result = 1
    count = 0
    for v in hashMap.values():
      if v[2] > count:
        result = v[1] - v[0] + 1
        count = v[2]
      elif v[2] == count:
        result = min(result, v[1] - v[0] + 1)
    
    return result

solution = Solution()
print(solution.findShortestSubArray([3, 1, 3]))
