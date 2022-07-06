#Problem: Given two binary strings a and b, return their sum as a binary string.

# Sample: a = '1', b = '11', Output: '100'

from typing import List

class Solution:
  def addBinary(self, a: str, b: str) -> List[int]:
    
    result = []

    if len(a) > len(b):
      x, y = a, b
    else:
      y, x = a, b

    print(x, y)

    carry = 0

    for i in range(len(x) - 1, -1, -1):
      if len(x) - 1 - i < len(y):
        ans = 0
        numSum = int(x[i]) + int(y[len(y) - 1 - (len(x) - 1 - i)])

        if carry:
          ans = 1 if (numSum % 2 == 0) else 0
        else:
          ans = 1 if numSum == 1 else 0
        
        carry = 1 if (numSum == 1 and carry == 1) or numSum == 2 else 0

        result.append(ans)
      
      else:
        numSum = int(x[i]) + carry

        carry = 1 if numSum == 2 else 0

        result.append(0 if (numSum % 2 == 0) else 1)
    
    if carry:
      result.append(1)
      
    result.reverse()
    return ''.join([str(ele) for ele in result])

solution = Solution()
print(solution.addBinary('1111', '11'))
