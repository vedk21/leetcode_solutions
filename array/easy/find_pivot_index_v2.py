# Problem: Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has. Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.) Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange. If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

# Sample: A = [1,2,5], B = [2,4], Output: [5,4]

from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
      
    leftSum = 0
    rightSum = 0
    # Find sum of nums arr for index 1-end
    for j in range(1, len(nums)):
      rightSum += nums[j]
    
    for i in range(0, len(nums)):
      if leftSum == rightSum:
        return i
      
      if i != len(nums) - 1:
        rightSum -= nums[i+1]
      
      leftSum += nums[i]
    
    return -1

solution = Solution()
print(solution.pivotIndex([1,5,3,9,7,2]))
