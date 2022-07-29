# Problem: Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

from typing import List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    if len(pre) == 0:
      return None
    
    root = TreeNode(pre.pop(0))
    post.pop(-1)
    if len(pre) == 0:
      return root
    
    idx = post.index(pre[0])
    root.left = self.constructFromPrePost(pre[:idx+1], post[:idx+1])
    root.right = self.constructFromPrePost(pre[idx+1:], post[idx+1:])
    return root

solution = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
print(solution.constructFromPrePost(pre, post))
