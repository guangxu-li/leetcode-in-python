#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
from collections import defaultdict, deque
from math import dist
from typing import Dict, List, Tuple


class Solution:
    def find_reachable_nodes(self, node: int) -> Dict[int, int]:
        q = deque([(node, 0)])

        nodes_dist = {}

        while q:
            curr, dist = q.popleft()
            if curr in nodes_dist:
                continue
            nodes_dist[curr] = dist

            for next in self.graph[curr]:
                q.append((next, dist + 1))

        return nodes_dist

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.graph = defaultdict(list)
        for u, v in enumerate(edges):
            if v == -1:
                continue
            self.graph[u].append(v)

        dist1 = self.find_reachable_nodes(node1)
        dist2 = self.find_reachable_nodes(node2)
        common_nodes = dist1.keys() & dist2.keys()

        _min = len(edges) + 1
        ans = -1

        for node in range(len(edges)):
            if node not in common_nodes:
                continue
            curr = max(dist1[node], dist2[node])
            if _min > curr:
                _min = curr
                ans = node

        return ans


# @lc code=end
