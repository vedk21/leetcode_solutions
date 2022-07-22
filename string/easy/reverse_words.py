# Problem: Given an input string s, reverse the order of the words

# Sample: s = ' hello  world ', Output: 'world hello'

from typing import List

class Solution:
  def reverseWords(self, s: str) -> str:

    parts = s.strip().split(' ')
    ret = ''
    for e in reversed(parts):
      tmp = e.strip()
      if tmp:
        if ret:
          ret += ' '
        ret += tmp
    return ret


solution = Solution()
print(solution.reverseWords(' hello      world '))
