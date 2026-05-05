#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
# dp[i] means the ans for the substring s[:i+1]
#
# dp[0] = 0
# 1. s[i] == 0: dp[i] = min(num of 1 in s[:i], 1 + dp[i - 1])
# 2. s[i] == 1: dp[i] = dp[i - 1]
from itertools import accumulate


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt, flips = 0, 0
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                flips = min(cnt, 1 + flips)

        return flips
# @lc code=end
