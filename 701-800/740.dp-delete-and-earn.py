#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
from collections import Counter


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
