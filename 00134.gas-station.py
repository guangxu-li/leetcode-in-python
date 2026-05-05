#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# Constraints:
# n == gas.length == cost.length
# 1 <= n <= 105
# 0 <= gas[i], cost[i] <= 104

# @lc code=start
from typing import List


# We need to prove that:
# If the total number of gas is not smaller than the total number of cost, there must be a solution.
#
# Then we only need to find the first start point i that can reach the end.
# Clearly, point i is able to reach the end N in this case.
# And we need to approve we can reach point i again contiue from the end N
#
# > Assume there is a point k between 0 and i that we can't move forward if starting from i.
# > So tank[0, k] + tank[i, N] < 0
# > But tank[0, k] + tank[k + 1, i - 1] + tank[i, N] >= 0
# > So tank[k + 1, i - 1] >= 0
# > However, if tank[k + 1, i - 1] >= 0, i won't be the first start point that is able to reach the end N.
# > So there is no point k between 0 and i that we can't move forward if starting from i.
# > So we can reach point i again contiue from the end N
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # not possible to be negative after considering the last point gas
            # We have
            #   1. tank[0, i - 1] + tank[i, N - 1] +  tank[N] >= 0
            #   2. tank[0, i - 1] < 0
            #
            # So tank[i, N - 1] + tank[N] >= 0
            if tank < 0:
                start = i + 1
                tank = 0

        return start


# @lc code=end
