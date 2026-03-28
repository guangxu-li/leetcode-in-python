#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
from collections import Counter


# Build the counter.
# Build the num * counter[num] sorted dicts `earns``.
#
# Then this problems becomes similar to the house robber problem.
#
# dp[i] means the max earn of the subproblem earns[:i].
# dp[i]:
#   - nums[i - 1] + 1 = nums[i]: max(dp[i - 1], earn[i] + dp[i - 2])
#   - nums[i - 1] + 1 <  nums[i]: cur + dp[i - 1]
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counter = dict((k, k * v) for k, v in Counter(nums).items())
        prev, cur, val_prev = 0, 0, None
        for num, earn in sorted(counter.items()):
            prev, cur, val_prev = (
                cur,
                max(cur, earn + prev) if val_prev == num - 1 else cur + earn,
                num,
            )

        return cur


# @lc code=end
