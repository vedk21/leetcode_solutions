# Problem: In a string S of lowercase letters, these letters form consecutive groups of the same character. For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy". Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group. The final answer should be in lexicographic order.

# Sample: S = "abcdddeeeeaabbbcd", Output: [[3,5],[6,9],[12,14]]

from typing import List

class Solution:
  def largeGroupPositions(self, S: str) -> List[List[int]]:
    if len(S) > 2:
      result = []
      start, end = 0, 1
      while (end < len(S)):
        if S[start] != S[end]:
          if (end - start >= 3):
            result.append([start, end - 1])
          start = end
          end += 1
        else:
          end += 1
      
      if (end - start >= 3):
        result.append([start, end - 1])
      
      return result
    else:
      return []

solution = Solution()
print(solution.largeGroupPositions('abcdddeeeeaabbbcd'))
