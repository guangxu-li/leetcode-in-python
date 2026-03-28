#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from collections import defaultdict
from itertools import product


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = defaultdict(set, {0: {()}})
        for t, cand in product(range(1, target + 1), candidates):
            for comb in dp[t - cand]:
                dp[t].add(tuple(sorted(comb + (cand,))))

        return dp[target]


# @lc code=end
