# Problem: Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die. Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Sample: flowerbed = [1,0,0,0,1], n = 1, Output: True

from typing import List

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    i = 0
    if len(flowerbed) > 1:
      while (i < len(flowerbed) and n > 0):
        if flowerbed[i] == 0:
          if i > 0 and i < len(flowerbed) - 1:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
              n -= 1
              flowerbed[i] = 1
          elif i == 0:
            if flowerbed[i + 1] == 0:
              n -= 1
              flowerbed[i] = 1
          elif i == len(flowerbed) - 1:
            if flowerbed[i - 1] == 0:
              n -= 1
              flowerbed[i] = 1
        i += 1

      return True if n <= 0 else False
    elif len(flowerbed) == 1:
      if flowerbed[0] == 0:
        n -= 1
      return True if n <= 0 else False
    else:
      return False

solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))
