# Problem: In a list of songs, the i-th song has a duration of time[i] seconds. Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

# Sample: time = [30,20,150,100,40], Output: 3

from typing import List
import collections

class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    reminders = collections.defaultdict(int)
    ret = 0
    for t in time:
      if t % 60 == 0: # check if a%60==0 && b%60==0
        ret += reminders[0]
      else: # check if a%60+b%60==60
        ret += reminders[60-t%60]
      reminders[t % 60] += 1 # reminder to update the reminders
    return ret


solution = Solution()
print(solution.numPairsDivisibleBy60([30,20,150,100,40]))
