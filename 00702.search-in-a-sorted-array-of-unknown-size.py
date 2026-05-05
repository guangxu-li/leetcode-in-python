#
# @lc app=leetcode id=702 lang=python3
#
# [702] Search in a Sorted Array of Unknown Size
#

# Constraints:
# 1 <= secret.length <= 104
# -104 <= secret[i], target <= 104
# secret is sorted in a strictly increasing order.

# @lc code=start
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        lo, hi = 0, 10**4
        while lo <= hi:
            i = (lo + hi) >> 1
            m = reader.get(i)

            if reader.get(i) == target:
                return i
            elif m < target:
                lo = i + 1
            else:
                hi = i - 1

        return -1


# @lc code=end
