# Problem: An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. Return true if and only if the given array A is monotonic.

# Sample: A = [1,2,4,5], Output: True

from typing import List

class Solution:
  def isMonotonic(self, A: List[int]) -> bool:
    if len(A) > 1:
      k = 0
      while (k < len(A) - 1 and A[k] == A[k + 1]):
        k += 1
      if k < len(A) - 1 and A[k] > A[k + 1]:
        for i in range(1, len(A) - 1):
          if A[i] < A[i + 1]:
            return False
        return True
      elif k < len(A) - 1 and A[k] < A[k + 1]:
        for i in range(1, len(A) - 1):
          if A[i] > A[i + 1]:
            return False
        return True
      else:
        return True
    else:
      return True

solution = Solution()
print(solution.isMonotonic([5,4,3,8]))
