#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # 1: not possible -> -1
        # 3n:   -> n
        # 3n+1: -> 3 * (n - 1) + 4 -> n + 1
        # 3n+2: -> n + 1
        cnts = Counter(tasks).values()
        return -1 if 1 in cnts else sum((c + 2) // 3 for c in cnts)


# @lc code=end
