# Problem: Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

# Sample: nums = [3, 1, 4, 1, 5], k = 2, Output: 2

from typing import List

class Solution:
  def findPairs(self, nums: List[int], k: int) -> int:
    nums = sorted(nums)

    count = 0
    pairs = {}
    for i in range(len(nums) - 1):
      idx = self.binarySearch(nums, i + 1, len(nums) - 1, nums[i] + k)
      if idx != -1:
        # check if pair already present in map
        if (nums[idx] not in pairs or pairs[nums[idx]] != nums[i]) and (nums[i] not in pairs or pairs[nums[i]] != nums[idx]):
          pairs[nums[i]] = nums[idx]
          count += 1
    
    return count

  def binarySearch(self, nums: List[int], left: int, right: int, key: int):

    if (left <= right):
      mid = left + (right - left) // 2
      if key == nums[mid]:
        return mid
      elif key > nums[mid]:
        return self.binarySearch(nums, mid + 1, right, key)
      else:
        return self.binarySearch(nums, left, mid - 1, key)

    return -1


solution = Solution()
print(solution.findPairs([3,1,4,3,5], 2))
