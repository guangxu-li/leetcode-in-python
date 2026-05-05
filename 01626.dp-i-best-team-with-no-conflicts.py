#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from typing import List


# Sort the scores by (score, age)
#
# Then the problems become finding the largest sum of subsequence.
# dp[i] = nums[i] + max(dp[j] for j in range(i) if nums[j] <= nums[i])
#
# https://leetcode.com/problems/best-team-with-no-conflicts/solutions/3120878/python-3-5-lines-dp-w-example-t-m-93-99/
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores = [score for _, score in sorted(zip(ages, scores))]
        n = len(scores)

        dp = [0] * n
        for i in range(n):
            dp[i] = scores[i]
            for j in range(i):
                if scores[j] <= scores[i]:
                    dp[i] = max(dp[i], dp[j] + scores[i])

        return max(dp)


# @lc code=end
