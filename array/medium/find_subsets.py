#Problem: Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

# Sample: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    output = [[]]
    
    for num in nums:
      output += [curr + [num] for curr in output]
    
    return output

solution = Solution()
ls = [1,2,3,4]
print(solution.subsets(ls))
