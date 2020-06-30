# Problem: Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements of [1, n] inclusive that do not appear in this array. 
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Sample: nums = [4,3,2,7,8,2,3,1], Output: [5,6]

from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
      absIndex = abs(nums[i]) - 1
      if nums[absIndex] > 0:
        nums[absIndex] = -nums[absIndex]
    
    result = []
    for j in range(len(nums)):
      if nums[j] > 0:
        result.append(j + 1)
    
    return result

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,3,8,2,3,1]))
