# Problem: You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums
# Input: nums = [3,2,1,6,0,5], Output: [6,3,5,null,2,0,null,null,1]

from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
      return None
    
    i = nums.index(max(nums))
    node = TreeNode(nums[i])
    node.left = self.constructMaximumBinaryTree(nums[:i])
    node.right = self.constructMaximumBinaryTree(nums[i + 1:])
    return node

solution = Solution()
ls = [3,2,1,6,0,5]
print(solution.constructMaximumBinaryTree(ls))
