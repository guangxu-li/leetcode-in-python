#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from functools import reduce


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return reduce(
            lambda perms, n: [
                p[:i] + [n] + p[i:] for p in perms for i in range((p + [n]).index(n) + 1)
            ],
            nums,
            [[]],
        )


# @lc code=end
