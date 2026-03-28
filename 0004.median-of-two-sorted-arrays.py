#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        l = m + n

        lo, hi = 0, m
        while lo <= hi:
            # i: len of nums1's left part
            # j: len of nums2's left part
            # i + j == (l + 1) // 2
            i = (lo + hi) >> 1
            j = (l + 1) // 2 - i

            if i < m and nums2[j - 1] > nums1[i]:
                lo = i + 1
            elif i >= 1 and nums1[i - 1] > nums2[j]:
                hi = i - 1
            else:
                max_left = 0
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if l & 1:
                    return max_left

                min_right = 0
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2

        return 0.0

# @lc code=end
