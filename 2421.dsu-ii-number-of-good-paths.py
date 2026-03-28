#
# @lc app=leetcode id=2421 lang=python3
#
# [2421] Number of Good Paths
#

# @lc code=start
from collections import Counter, defaultdict
from typing import DefaultDict, Iterable, List


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        # path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i, j: int) -> None:
        i, j = self.find(i), self.find(j)

        # union by rank
        if self.rank[i] < self.rank[j]:
            self.parent[i] = j
        elif self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[j] = i
            self.rank[i] += 1

    # union_all unions each node together with i.
    def union_all(self, i: int, nodes: Iterable[int]) -> None:
        for j in nodes:
            self.union(i, j)

    # group_count returns the node count for each group.
    # It groups the provided nodes into several groups by root, then returns back the node count of each group.
    def group_count(self, nodes: List[int]) -> Iterable[int]:
        return Counter(self.find(i) for i in nodes).values()


class Solution:
    def build_graph(self, vals: List[int], edges: List[List[int]]) -> DefaultDict:
        graph = defaultdict(list)
        for u, v in edges:
            # only able to move from u to v when u's val is larger than or equal to v's val,
            # and vice versa
            if vals[u] <= vals[v]:
                graph[v].append(u)
            if vals[u] >= vals[v]:
                graph[u].append(v)

        return graph

    def group_by_val(self, vals: List[int]) -> DefaultDict:
        val2nodes = defaultdict(list)
        for i, val in enumerate(vals):
            val2nodes[val].append(i)

        return val2nodes

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        dsu = UnionFind(n)

        val2nodes = self.group_by_val(vals)
        graph = self.build_graph(vals, edges)

        def count(nodes):
            for cur in nodes:
                dsu.union_all(cur, graph[cur])

            groups_size = dsu.group_count(nodes)
            return sum(size * (size + 1) // 2 for size in groups_size)

        return sum(count(val2nodes[val]) for val in sorted(val2nodes.keys()))


# @lc code=end
