#
# @lc app=leetcode id=1525 lang=python3
#
# [1525] Number of Good Ways to Split a String
#

# @lc code=start
from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left, right, cnt = Counter(), Counter(s), 0
        for ch in s:
            left[ch] += 1
            right[ch] -= 1
            
            cnt += 1 if len(left) == len(+right) else 0
            
        return cnt
# @lc code=end
