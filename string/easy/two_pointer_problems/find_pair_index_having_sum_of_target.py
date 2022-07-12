#Problem: Find two numbers such that they add up to a specific target number. Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2. numbers is sorted in non-decreasing order

# Sample: numbers = [-8,-5,1,2,4,6], target = -4, Output: [4, 5]

from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:

    i, j = 0, len(numbers) - 1

    while i < j:
      sm = numbers[i] + numbers[j]
      if sm == target:
        return [i + 1, j + 1]

      if sm < target:
        i += 1
      else:
        j -= 1
    
    return [-1, -1]

solution = Solution()
print(solution.twoSum([-8,-5,1,2,4,6], -4))
