#
# @lc app=leetcode id=1874 lang=python3
#
# [1874] Minimize Product Sum of Two Arrays
#
# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/description/
#
# algorithms
# Medium (90.44%)
# Likes:    179
# Dislikes: 23
# Total Accepted:    13.9K
# Total Submissions: 15.4K
# Testcase Example:  '[5,3,4,2]\n[4,2,2,5]'
#
# The product sum of two equal-length arrays a and b is equal to the sum of
# a[i] * b[i] for all 0 <= i < a.length (0-indexed).
#
#
# For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5
# + 2*2 + 3*3 + 4*1 = 22.
#
#
# Given two arrays nums1 and nums2 of length n, return the minimum product sum
# if you are allowed to rearrange the order of the elements in nums1.
#
#
# Example 1:
#
#
# Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
# Output: 40
# Explanation: We can rearrange nums1 to become [3,5,4,2]. The product sum of
# [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.
#
#
# Example 2:
#
#
# Input: nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]
# Output: 65
# Explanation: We can rearrange nums1 to become [5,7,4,1,2]. The product sum of
# [5,7,4,1,2] and [3,2,4,8,6] is 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65.
#
#
#
# Constraints:
#
#
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 1 <= nums1[i], nums2[i] <= 100
#
#

# @lc code=start
from collections import Counter


class Solution:
    def minProductSum(self, nums1: list[int], nums2: list[int]) -> int:
        # can be optimized by counting sort
        # return sum(a * b for a, b in zip(sorted(nums1), sorted(nums2, reverse=True)))

        # counter of nums1 and nums2
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        lo, hi, res = 1, 100, 0
        while lo <= 100 and hi > 0:
            while c1[lo] == 0 and lo <= 100:
                lo += 1
            while c2[hi] == 0 and hi > 0:
                hi -= 1

            time = min(c1[lo], c2[hi])
            res += lo * hi * time
            c1[lo] -= time
            c2[hi] -= time

        return res


# @lc code=end
