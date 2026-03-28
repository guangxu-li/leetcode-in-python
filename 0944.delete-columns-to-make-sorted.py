#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# Constraints:
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 1000
# strs[i] consists of lowercase English letters.

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*strs))


# @lc code=end
