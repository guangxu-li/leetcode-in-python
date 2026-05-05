#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from collections import defaultdict


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        dp = defaultdict(list, {0: [[]]})
        for c in range(1, 10):
            for i in range(n, c - 1, -1):
                for prev in dp[i - c]:
                    if i == n and len(prev) != k - 1:
                        continue
                    dp[i].append(prev + [c])

        return dp[n]
# @lc code=end
