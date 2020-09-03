# Problem: For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1]. Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

# Sample: A = [2,7,4], K = 181, Output: [4,5,5]

from typing import List

class Solution:
  def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    for i in range(len(A) - 1, -1, -1):
      if not K: break
      K, A[i] = divmod(A[i] + K, 10)
    # if K's digits are more than A length
    while K:
      K, a = divmod(K, 10)
      A = [a] + A
    
    return A

solution = Solution()
print(solution.addToArrayForm([2,7,4], 181))
