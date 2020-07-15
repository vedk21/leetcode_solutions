# Problem: We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11). Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

# Sample: bits = [1, 1, 1, 0], Output: False

from typing import List

class Solution:
  def isOneBitCharacter(self, bits: List[int]) -> bool:
    if len(bits) > 1:
      i = len(bits) - 2
      count = 0
      while (i >= 0 and bits[i] == 1):
        count += 1
        i -= 1
      
      return count % 2 == 0
        
    else:
      return True

solution = Solution()
print(solution.isOneBitCharacter([1, 1, 0, 1, 0, 0]))
