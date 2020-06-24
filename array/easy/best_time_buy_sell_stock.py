# Problem: Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one.

# Sample: prices = [7,1,5,3,6,4], Output: 5

from typing import List

class Solution:
  def maxProfitBruteForce(self, prices: List[int]) -> int:
    profit = 0
    for i in range(len(prices)):
      for j in range(i+1, len(prices)):
        current_profit = prices[j] - prices[i]
        if current_profit > 0:
          profit = max(current_profit, profit)
    
    return profit

  def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = 999999999 # a big number
    for i in range(len(prices)):
      current_profit = prices[i] - min_price
      if prices[i] < min_price:
        min_price = prices[i]
      elif current_profit > profit:
        profit = current_profit
    
    return profit

solution = Solution()
print(solution.maxProfit([7,6,5,4,2,1]))
