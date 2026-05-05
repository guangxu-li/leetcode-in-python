#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from collections import defaultdict


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int, {0: 1})
        dp.update(map(lambda i: (i, sum(dp[i - n] for n in nums)), range(1, target + 1)))
        return dp[target]


# @lc code=end
