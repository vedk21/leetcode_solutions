# Problem: Given an array, rotate the array to the right by k steps, where k is non-negative. Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem. Could you do it in-place with O(1) extra space?

# Sample: nums = [1,2,3,4,5,6,7], k = 3, Output: [5,6,7,1,2,3,4]

from typing import List

class Solution:
  def rotateBruteForce(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(k % len(nums)):
      prev_value = nums[0]
      for j in range(len(nums)):
        next_index = (j + 1) % len(nums)
        # swap nums[nextIndex] and prev_value
        temp = nums[next_index]
        nums[next_index] = prev_value
        prev_value = temp

  def reverse(self, nums: List[int], start: int, end: int) -> None:
    while start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start, end = start + 1, end - 1

  def rotateUsingReverse(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    self.reverse(nums, 0, n - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, n - 1)

solution = Solution()
ls = [1,2,3,4,5,6,7]
solution.rotateUsingReverse(ls, 3)
print(ls)
