# Problem: Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A. You may return any answer array that satisfies this condition.

# Sample: A = [3,1,2,4], Output: [2,4,3,1]

from typing import List

class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    i, j = 0, len(A) - 1

    while i < j:
      while (i < len(A) and A[i] % 2 == 0):
        i += 1
      while (j >= 0 and A[j] % 2 != 0):
        j -= 1
    
      if i < len(A) and j >= 0 and i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    
    return A

solution = Solution()
print(solution.sortArrayByParity([3,5]))
