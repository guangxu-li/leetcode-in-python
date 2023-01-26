#
# @lc app=leetcode id=1176 lang=python3
#
# [1176] Diet Plan Performance
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pre_sum = list(accumulate(calories, initial=0))

        points = 0
        for i in range(k, len(pre_sum)):
            total = pre_sum[i] - pre_sum[i - k]
            if total < lower:
                points -= 1
            if total > upper:
                points += 1

        return points

# @lc code=end
