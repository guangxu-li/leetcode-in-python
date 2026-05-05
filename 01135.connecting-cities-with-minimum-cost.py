#
# @lc app=leetcode id=1135 lang=python3
#
# [1135] Connecting Cities With Minimum Cost
#

# @lc code=start
from typing import List


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.rank = [0] * n
        self.parent = list(range(n))
        self.group_cnt = n

    def find(self, i: int) -> int:
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return
        self.group_cnt -= 1

        if self.rank[i] < self.rank[j]:
            self.parent[i] = j
        elif self.rank[i] == self.rank[j]:
            self.parent[j] = i
            self.rank[i] += 1
        else:
            self.parent[j] = i

    def same_group(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        connections.sort(key=lambda x:x[2]) # sort by weight
        cost = 0

        for a, b, c in connections:
            ds.union(a, b)
            cost += c

        return cost if ds.group_cnt == 1 else -1
# @lc code=end
