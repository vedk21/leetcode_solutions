# Problem: In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.  There is at least one empty seat, and at least one person sitting. Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. Return that maximum distance to closest person.

# Sample: seats = [1,0,0,0,1,0,1], Output: 2

from typing import List

class Solution:
  def maxDistToClosest(self, seats: List[int]) -> int:
    oneIndex = -1
    for i in range(len(seats)):
      if seats[i] == 1:
        oneIndex = i
      else:
        if oneIndex > -1:
          seats[i] = -abs(i - oneIndex)
        else:
          seats[i] = -20000
    
    oneIndex = -1
    maxD = abs(seats[len(seats) - 1]) if seats[len(seats) - 1] != 1 else -1
    for j in range(len(seats) - 1, -1, -1):
      if seats[j] == 1:
        oneIndex = j
      else:
        if oneIndex > -1:
          maxD = max(maxD, min(abs(seats[j]), abs(j - oneIndex)))

    return maxD

solution = Solution()
print(solution.maxDistToClosest([1,0,0,0,1,0,1]))
