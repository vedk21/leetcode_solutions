# Problem: Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even. Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even. You may return any answer array that satisfies this condition.

# Sample: Input: [4,2,5,7], Output: [4,5,2,7]

from typing import List

class Solution:
  def sortArrayByParityII(self, A: List[int]) -> List[int]:
    f, l = 0, len(A) - 1
    while f < len(A) and l >= 0:
      while f < len(A) and (A[f] % 2 == 0 or (f % 2 != 0 and A[f] % 2 != 0)):
        f += 1
      while l >= 0 and (A[l] % 2 != 0 or (l % 2 == 0 and A[l] % 2 == 0)):
        l -= 1
      
      if f < len(A) and l >= 0:
        A[l], A[f] = A[f], A[l]
        f += 1
        l -= 1
    
    return A

solution = Solution()
print(solution.sortArrayByParityII([2,3,3,1,4,4,0,0,1,3]))
