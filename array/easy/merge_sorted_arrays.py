# Problem: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note: The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Sample: nums1 = [1,2,3,0,0], m = 3, nums2 = [2,5], n = 2

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # initialize count with nums1 last index
        count = m + n -1
        # initialize m and n to last array index
        m -= 1
        n -= 1

        while (m >= 0 and n >= 0):
          if nums1[m] > nums2[n]:
            nums1[count] = nums1[m]
            count -= 1
            m -= 1
          else:
            nums1[count] = nums2[n]
            count -= 1
            n -= 1
        
        # if any element left in nums2, add to nums1
        while n >= 0:
          nums1[count] = nums2[n]
          count -= 1
          n -= 1

solution = Solution()
nums1 = [5,9,11,0,0,0,0]
nums2 = [2,3,7,20]
solution.merge(nums1, (len(nums1) - len(nums2)), nums2, len(nums2))
print(nums1)
