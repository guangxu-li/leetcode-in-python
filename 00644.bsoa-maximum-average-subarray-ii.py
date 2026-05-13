#
# @lc app=leetcode id=644 lang=python3
#
# [644] Maximum Average Subarray II
#

# @lc code=start
import math


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        def feasible(avg: int) -> bool:
            n = len(nums)
            accu = [0] * (n + 1)
            for i, num in enumerate(nums):
                accu[i + 1] = accu[i] + num - avg

            _min = math.inf
            for i in range(k, n + 1):
                _min = min(_min, accu[i - k])
                if accu[i] - _min >= 0:
                    return True

            return False

        lo, hi = min(nums), max(nums)
        # In competitive programming, many prefer to just run the loop a fixed number of times.
        # Dividing the search space in half 60 times shrinks it by a factor of 260,
        #   which provides far more precision than a 64-bit float can even represent.
        # This guarantees the loop will terminate and completely avoids epsilon edge cases.
        # The exact loop value can be customized based on the search span and accuracy requirement,
        #   but 60 gives around 10^-18 scaling which is typically safe enough
        for _ in range(60):
            avg = (lo + hi) / 2
            if feasible(avg):
                lo = avg
            else:
                hi = avg

        return lo

# @lc code=end
