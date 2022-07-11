#Problem: Write a function to find the longest common prefix string amongst an array of strings.

# Sample: strs = ['car', 'care'], Output: 'car'

from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:

    # find min length string
    idx, size = self.findMinStr(strs)

    if size:
      prefix = ''
      for i in range(size):
        ch = strs[idx][i]
        for item in strs:
          if item[i] != ch:
            return prefix
          
        prefix += ch

      return prefix
    else:
      return ''

  def findMinStr(self, strs: List[str]) -> (int, int):
    size = 210
    index = 0
    for i in range(len(strs)):
      if len(strs[i]) < size:
        size = len(strs[i])
        index = i
    
    return (index, size)

solution = Solution()
print(solution.longestCommonPrefix(['car', 'care', 'ascar']))
    