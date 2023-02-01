#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from typing import List


# sort by (score, age)
#
# max_score[age] means max scores inside the `age` group
# dp[age] means the largest scores of the team that the largest age is `age`.
# dp[age] = largest increasing score sequences
#   - score <= max_score[age]
#
# for score, age in sorted((score, age)):
#   dp[age] = score + max(dp[:age + 1])
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * (max(ages) + 1)
        for score, age in sorted(zip(scores, ages)):
            # note here that the process of finding largest is able
            # to be optimised by the BIT/segment tree.
            dp[age] = score + max(dp[:age + 1])

        return max(dp)

# @lc code=end
