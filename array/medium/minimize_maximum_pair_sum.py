#Problem: The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs. Return the minimized maximum pair sum after optimally pairing up the elements.

# The optimal division of array into N pairs should result into a maximum pair sum which is minimum of other maximum pair sum of all possibilities.

# arr[] = { 5, 8, 3, 9 }  Output : (3, 9) (5, 8) 
# Explanation: Possible pairs are : 
# 1. (8, 9) (3, 5) Maximum Sum of a Pair = 17 
# 2. (5, 9) (3, 8) Maximum Sum of a Pair = 14 
# 3. (3, 9) (5, 8) Maximum Sum of a Pair = 13 
# Thus, in case 3, the maximum pair sum is minimum of all the other cases. Hence, the answer is(3, 9) (5, 8).

from typing import List

class Solution:
  def minPairSum(self, nums: List[int]) -> int:
    
    nums.sort(reverse=False)

    i, j = 0, len(nums) - 1

    maxSum = 0
    while i <= j:
      pairSum = nums[i] + nums[j]
      maxSum = max(pairSum, maxSum)
      i += 1
      j -= 1
    return maxSum

solution = Solution()
ls = [6,3,5,6,2,1]
print(solution.minPairSum(ls))
