#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
import heapq
from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        q = deque([(0, src, 0)])  # (dist, start, stop)
        dist = defaultdict(lambda: float("inf"))

        while q:
            price, cur, stop = q.popleft()
            if stop == k + 1:
                continue

            for nxt, nxt_price in graph[cur].items():
                nprice = price + nxt_price
                if nprice < dist[nxt]:
                    dist[nxt] = nprice
                    q.append((nprice, nxt, stop + 1))

        return dist[dst] if dst in dist else -1


# @lc code=end
