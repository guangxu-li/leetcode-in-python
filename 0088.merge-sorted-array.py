#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        for k in reversed(range(m + n)):
            num1 = nums1[i] if i >= 0 else -math.inf
            num2 = nums2[j] if j >= 0 else -math.inf

            if num1 >= num2:
                nums1[k] = num1
                i -= 1
            else:
                nums1[k] = num2
                j -= 1


# @lc code=end
