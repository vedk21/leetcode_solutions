# Problem: Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Sample: A = [-4,-1,0,3,10], Output: [0,1,9,16,100]

from typing import List

class Solution:
  def sortedSquares(self, A: List[int]) -> List[int]:
    for i in range(len(A)):
      A[i] = A[i] ** 2
    
    A = sorted(A)

    return A

  def sortedSquaresLinear(self, A: List[int]) -> List[int]:
    N = len(A)
    j = 0
    # find the first positive number from left
    while j < N and A[j] < 0:
      j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
      if A[i]**2 < A[j]**2:
        ans.append(A[i]**2)
        i -= 1
      else:
        ans.append(A[j]**2)
        j += 1

    while i >= 0:
      ans.append(A[i]**2)
      i -= 1
    while j < N:
      ans.append(A[j]**2)
      j += 1

    return ans

solution = Solution()
print(solution.sortedSquaresLinear([-4,-1,0,3,10]))
