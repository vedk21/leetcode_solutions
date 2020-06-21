# Problem: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.You may assume the integer does not contain any leading zero, except the number 0 itself.

# Sample: digits = [1,2,3]

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      i, sum = len(digits) - 1, 0
      while (i >= 0):
        sum = digits[i] + 1
        if (sum > 9):
          digits[i] = sum % 10
          i -= 1
        else:
          digits[i] = sum
          break
      else:
        digits.insert(0, sum // 10)

      return digits

solution = Solution()
print(solution.plusOne([4,9,9]))
