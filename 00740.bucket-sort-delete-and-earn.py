#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counter, prev, cur = Counter(nums), 0, 0
        for i in range(min(nums), max(nums) + 1):
            prev, cur = cur, max(i * counter[i] + prev, cur)
        return cur


# @lc code=end
