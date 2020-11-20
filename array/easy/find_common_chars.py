# Problem: Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# Sample: A = ["bella","label","roller"], Output: ["e","l","l"]

from typing import List

class Solution:
  def commonChars(self, A: List[str]) -> List[str]:
    if len(A) > 1:
      hMap = {}
      result = []

      for char in A[0]:
        if char in hMap.keys():
          hMap[char][0] += 1
        else:
          hMap[char] = [1]

      for i in range(1, len(A)):
        for char in A[i]:
          if char in hMap.keys():
            if len(hMap[char]) < i:
              del hMap[char]
            elif len(hMap[char]) == i:
              hMap[char].append(1)
            else:
              hMap[char][i] += 1

      for key, val in hMap.items():
        if len(val) == len(A):
          minEle = min(val)
          for i in range(minEle):
            result.append(key)

      return result

    else:
      return [char for char in A[0]]


solution = Solution()
print(solution.commonChars(["cool","lock","cook"]))
