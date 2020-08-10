# Problem: In a deck of cards, each card has an integer written on it. Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where: Each group has exactly X cards. All the cards in each group have the same integer.

# Sample: Input: deck = [1,1,2,2,2,2], Output: true, Explanation: Possible partition [1,1],[2,2],[2,2].

from typing import List
from math import gcd
import collections
from functools import reduce

class Solution:
  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    vals = collections.Counter(deck).values()
    return reduce(gcd, vals) >= 2

solution = Solution()
print(solution.hasGroupsSizeX([1,1,1,1,2,2,2,2,3,3]))
