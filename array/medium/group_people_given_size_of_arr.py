# Problem: You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3. Return a list of groups such that each person i is in a group of size groupSizes[i].

# Sample: nums = [2,3,2,3,3,1], Output: [[0,2], [5], [1,3,4]]

from typing import List

class Solution:
  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

    result = []
    groupDict = {}

    for i in range(len(groupSizes)):
      if groupSizes[i] in groupDict:
        groupDict[groupSizes[i]].append(i)
      else:
        groupDict[groupSizes[i]] = [i]
    
    for key, val in groupDict.items():
      if key != len(val):
        for i in range(0, len(val), key):
          result.append(val[i:i+key])
      else:
        result.append(val)

    return result

solution = Solution()
ls = [1,2,2,2,2]
print(solution.groupThePeople(ls))
