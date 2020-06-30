# Problem: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

# Sample: N = 4, Output: 3

from typing import List

class Solution:
  def fib(self, N: int) -> int:
    if N <= 1:
      return N
    
    return self.memoize(N)
  
  def memoize(self, N: int) -> {}:
    cache = {0: 0, 1: 1}
    
    for i in range(2, N + 1):
      cache[i] = cache[i - 1] + cache[i - 2]
      
    return cache[N]

solution = Solution()
print(solution.fib(30))
