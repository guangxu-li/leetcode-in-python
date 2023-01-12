#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#


# @lc code=start
from collections import Counter, defaultdict
from typing import Counter, List


class Solution:
    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()
        self.labels = ""
        self.cnts = []

    def dfs(self, cur: int) -> Counter:
        if cur in self.visited:
            return Counter()
        self.visited.add(cur)

        C = Counter(self.labels[cur])
        for adj in self.graph[cur] - self.visited:
            C += self.dfs(adj)

        self.cnts[cur] = C[self.labels[cur]]

        return C

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = labels
        self.cnts = [0] * n
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)

        self.dfs(0)

        return self.cnts


# @lc code=end
