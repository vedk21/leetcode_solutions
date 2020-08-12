# Problem: Given an array A of integers, return true if and only if it is a valid mountain array. Recall that A is a mountain array if and only if: A.length >= 3 There exists some i with 0 < i < A.length - 1 such that: A[0] < A[1] < ... A[i-1] < A[i], A[i] > A[i+1] > ... > A[A.length - 1]

# Sample: Input: [0,3,2,1], Output: true

from typing import List

class Solution:
  def validMountainArray(self, A: List[int]) -> bool:
    isIncreasing = True
    if len(A) >= 3:
      # check for border conditions on both side of the array
      if A[0] >= A[1] or A[len(A) - 2] <= A[len(A) - 1]:
        return False

      for i in range(2, len(A) - 1):
        if isIncreasing and A[i] < A[i - 1]:
          isIncreasing = False
        
        if isIncreasing and A[i] == A[i - 1]:
          return False
        
        if not isIncreasing and A[i] >= A[i - 1]:
          return False
      
      return True
    else:
      return False

solution = Solution()
print(solution.validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]))
