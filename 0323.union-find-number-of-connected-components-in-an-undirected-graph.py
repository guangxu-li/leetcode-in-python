#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
from functools import reduce


class Solution:
    def find(self, i: int) -> int:
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, i: int, j: int) -> int:
        i, j = self.find(i), self.find(j)
        self.parent[j] = i
        return i != j

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        self.parent = list(range(n))
        return reduce(lambda cnt, edge: cnt - self.union(*edge), edges, n)


# @lc code=end
