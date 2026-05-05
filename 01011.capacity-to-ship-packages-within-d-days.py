#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#


# @lc code=start
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # constraint: d <= days
        # minimize capacity to maximize d
        #   capacity down, then d up
        #   capacity up, then d down
        # capacity answer space:
        #   - max(weights), sum(weight) // days
        #   - sum(weight)
        total = sum(weights)
        lo, hi = max(max(weights), total // days), total
        while lo <= hi:
            capacity = (lo + hi) >> 1
            d = 1
            load = 0
            for weight in weights:
                if load + weight > capacity:
                    d += 1
                    load = 0
                load += weight

            if d <= days:
                hi = capacity - 1
            else:
                lo = capacity + 1
        return lo


# @lc code=end
