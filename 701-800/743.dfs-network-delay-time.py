#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.graph = defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((v, w))

        self.delays = [0] + [float('inf')] * n

        self.traversal(k, 0)

        delay = max(self.delays)
        return -1 if delay == float('inf') else delay

    def traversal(self, u: int, w: int) -> None:
        if self.delays[u] <= w:
            return
        self.delays[u] = min(self.delays[u], w)

        for u, nw in self.graph[u]:
            self.traversal(u, w + nw)


# @lc code=end
