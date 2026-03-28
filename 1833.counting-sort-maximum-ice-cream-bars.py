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
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        freq = [0] * (m + 1)
        for cost in costs:
            freq[cost] += 1

        cnt = 0
        for cost in range(1, m + 1):
            if not freq[cost]:
                continue
            if coins < cost:
                break

            n = min(freq[cost], coins // cost)
            cnt += n
            coins -= n * cost

        return cnt



# @lc code=end
