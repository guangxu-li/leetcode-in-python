#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [set({()})] + [set() for _ in range(target)]

        for c in sorted(candidates):
            for i in range(target, c - 1, -1):
                for prev in dp[i - c]:
                    dp[i].add(prev + (c,))

        return dp[-1]


# @lc code=end
