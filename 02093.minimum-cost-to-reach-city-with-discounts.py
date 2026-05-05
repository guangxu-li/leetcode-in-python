#
# @lc app=leetcode id=2093 lang=python3
#
# [2093] Minimum Cost to Reach City With Discounts
#

# @lc code=start
import heapq
from collections import defaultdict


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in highways:
            graph[u][v] = w
            graph[v][u] = w

        q = [(0, 0, discounts)]
        visited = {} # node: remaining discounts
        while q:
            d, node, discounts = heapq.heappop(q)
            if discounts < 0:
                continue

            # skip if already found cheaper path with more remaining discounts
            if node in visited and discounts <= visited[node]:
                continue
            visited[node] = discounts

            if node == n - 1:
                return d

            for nxt, w in graph[node].items():
                # push with and without it discounted
                heapq.heappush(q, (d + w // 2, nxt, discounts - 1))
                heapq.heappush(q, (d + w, nxt, discounts))
        return -1


# @lc code=end
