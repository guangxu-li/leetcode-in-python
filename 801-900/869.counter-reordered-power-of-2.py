#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return any(Counter(str(N)) == Counter(str(1 << i)) for i in range(31))


# @lc code=end
