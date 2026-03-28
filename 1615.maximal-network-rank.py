#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        if len(roads) < 2:
            return len(roads)

        graph = defaultdict(set)

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                ret = max(ret, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        
        return ret
# @lc code=end
