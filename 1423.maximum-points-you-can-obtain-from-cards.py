#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
from functools import reduce


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        _sum = _max = sum(cardPoints[n - k:])
        for lo, hi in zip(cardPoints[:k], cardPoints[n - k:]):
            _sum += lo - hi
            _max = max(_max, _sum)
        
        return _max
# @lc code=end
