#
# @lc app=leetcode id=2398 lang=python3
#
# [2398] Maximum Number of Robots Within Budget
#

# @lc code=start
from collections import deque


class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        # expansion: expand sliding window
        # corretion: validity check + shrink sliding window
        # query: maximum length
        # validity: to calculate current sliding window cost, we need sliding window maximum + sliding window sum

        n = len(chargeTimes)
        ans = 0
        maxs = deque()
        cost = 0

        lo = 0
        for hi in range(n):
            while maxs and chargeTimes[maxs[-1]] <= chargeTimes[hi]:
                maxs.pop()
            maxs.append(hi)

            cost += runningCosts[hi]
            while maxs and chargeTimes[maxs[0]] + (hi - lo + 1) * cost > budget:
                if maxs and maxs[0] == lo:
                    maxs.popleft()

                cost -= runningCosts[lo]
                lo += 1

            ans = max(ans, hi - lo + 1)

        return ans
# @lc code=end
