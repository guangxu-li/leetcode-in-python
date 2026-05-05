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
        for u, v, t in times:
            graph[u].append((t, v))

        delays = [0] + [float('inf')] * n
        delays[k] = 0
        pq = [(0, k)]

        while pq:
            t, u = heappop(pq)

            for vt, v in graph.pop(u, []):
                if t + vt < delays[v]:
                    delays[v] = t + vt
                    heappush(pq, (t + vt, v))

        delay = max(delays)
        return -1 if delay == float('inf') else delay

# @lc code=end
