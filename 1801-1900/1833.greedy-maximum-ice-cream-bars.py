#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# Constraints:
# costs.length == n
# 1 <= n <= 105
# 1 <= costs[i] <= 105
# 1 <= coins <= 108

# @lc code=start
from bisect import bisect


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return bisect(list(itertools.accumulate(sorted(costs))), coins)


# @lc code=end
