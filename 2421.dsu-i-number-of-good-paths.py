#
# @lc app=leetcode id=2421 lang=python3
#
# [2421] Number of Good Paths
#

# @lc code=start
from collections import Counter
from typing import List


class UnionFind:
    def __init__(self, vals: List[int]) -> None:
        n = len(vals)
        self.cnt = n
        self.parent = list(range(n))
        self.counts = [Counter([val]) for val in vals]

    def find(self, i: int) -> int:
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]

        return i

    def union(self, val, i, j: int) -> None:
        i, j = self.find(i), self.find(j)
        ci, cj = self.counts[i], self.counts[j]
        self.cnt += ci[val] * cj[val]

        # merge j to i
        self.parent[j] = i
        # And in the future, the `val` will be continuously increasing.
        # So we don't need to merge the legacy `val` count here.
        ci[val] += cj[val]


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        dsu = UnionFind(vals)

        # why we care about the max value?
        # Let's say we have an edge (0, 1) with value 2 and 4.
        # Clearly, there's no way to make a good path than starts from 0 and passes/ends at 1.
        edges_weight = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)
        for val, i, j in edges_weight:
            dsu.union(val, i, j)

        return dsu.cnt


# @lc code=end
