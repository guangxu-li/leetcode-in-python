#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return any(
            bin(int("".join(p))).count("1") == 1
            for p in permutations(str(N))
            if p[0] != "0"
        )


# @lc code=end
