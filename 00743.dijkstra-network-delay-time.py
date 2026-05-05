#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        delays = [float("inf")] * n
        delays[k] = 0
        pq = [(0, k)]

        while pq:
            w, u = heappop(pq)

            for nw, v in graph[u]:
                if w + nw < delays[v]:
                    delays[v] = w + nw
                    heappush(pq, (w + nw, v))

        return max(delays)
# @lc code=end
