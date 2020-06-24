# Problem: Say you have an array prices for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times). Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Sample: prices = [7,1,5,3,6,4], Output: 7

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    i = 0
    profit = 0
    peak = prices[0]
    valley = prices[0]
    while (i < len(prices) - 1):
      # find next valley point
      while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
        i += 1
      valley = prices[i]

      # find next peak point
      while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):
        i += 1
      peak = prices[i]

      profit += peak - valley

    return profit

solution = Solution()
print(solution.maxProfit([1,2,3,4,5]))
