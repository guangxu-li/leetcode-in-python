#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for p, (a, b) in zip(succProb, edges):
            graph[a].append((p, b))
            graph[b].append((p, a))

        probs = [0] * n
        pq = [(-1, start_node)] # max heap, always return the item with largest prob

        while pq:
            p, node = heappop(pq)
            p = abs(p)

            if node == end_node:
                return p
            for np, nxt in graph.pop(node, []):
                if p * np > probs[nxt]:
                    probs[nxt] = p * np
                    heappush(pq, (-p * np, nxt))
        return 0

# @lc code=end
