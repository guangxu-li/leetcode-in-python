#
# @lc app=leetcode id=2515 lang=python3
#
# [2515] Shortest Distance to Target String in a Circular Array
#

# @lc code=start
import math


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        _min = n
        for i, word in enumerate(words):
            if word == target:
                _min = min(_min, abs(i - startIndex), n - abs(i - startIndex))

        return -1 if _min == n else _min


# @lc code=end
