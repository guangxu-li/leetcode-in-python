#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)
        for a, b in trust:
            out_degrees[a] += 1
            in_degrees[b] += 1

        for i in range(1, n + 1):
            if in_degrees[i] == n - 1 and out_degrees[i] == 0:
                return i

        return -1


# @lc code=end
