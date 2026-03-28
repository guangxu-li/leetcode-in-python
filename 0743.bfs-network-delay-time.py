#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        delays = [0] + [float('inf')] * n

        q = deque([(k, 0)])
        while q:
            u, w = q.popleft()
            if delays[u] <= w:
                continue
            delays[u] = w

            for v, nw in graph[u]:
                q.append((v, w + nw))

        delay = max(delays)
        return -1 if delay == float('inf') else delay

# @lc code=end
