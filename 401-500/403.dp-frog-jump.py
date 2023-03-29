#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
from collections import defaultdict
from typing import List


# step = stones[j] - stones[i]
# dp[j][step - 1] = dp[i][step]
# dp[j][step] = dp[i][step]
# dp[j][step + 1] = dp[i][step]
#
# dp[i][step] means we can jump from stones[i] with the step
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True

        for i in range(n):
            for j in range(i + 1, n):
                step = stones[j] - stones[i]
                if step > n - 1 or not dp[i][step]:
                    continue

                for nstep in {step - 1, step, step + 1}:
                    dp[j][nstep] = 0 < nstep < n

        return any(dp[j])


# @lc code=end
