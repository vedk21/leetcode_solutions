#Problem: Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
# Sample: nums = [3,1,1,2,3], target: 5 Output: 2

from typing import List

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
    result = 100001

    for i in range(len(nums)):
      if nums[i] < target:
        sum = nums[i]
        count = 1
        for j in range(i+1, len(nums)):
          sum += nums[j]
          count += 1
          if sum == target:
            result = min(count, result)
            break
          elif sum > target:
            break
      elif nums[i] == target:
        result = 1
    
    return 0 if result == 100001 else result

    # below got accepted on leetcode but actually is wrong, cz if target subarray is not present then 0 is not retuned

    # ans = 100001
    # left = 0
    # sum = 0
    # for i in range(len(nums)):
    #   sum += nums[i]
    #   while sum >= target:
    #     ans = min(ans, i + 1 - left)
    #     sum -= nums[left]
    #     left += 1
    # return ans if (ans != 100001) else 0

solution = Solution()
print(solution.minSubArrayLen(2, [3,5,1,5]))
