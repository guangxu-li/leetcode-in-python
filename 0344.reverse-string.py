#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#


# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1


# @lc code=end
