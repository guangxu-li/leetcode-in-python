#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
from collections import defaultdict


class Solution:
    def dfs(self, graph: defaultdict[int, set], visited: set[int], u: int) -> None:
        if u in visited:
            return
        visited.add(u)

        for v in graph[u]:
            self.dfs(graph, visited, v)

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        cnt, visited = 0, set()
        for i in range(n):
            if i in visited:
                continue
            cnt += 1
            self.dfs(graph, visited, i)

        return cnt


# @lc code=end
