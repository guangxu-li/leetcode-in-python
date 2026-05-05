#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.counts = [1] * n

    def find(self, i: int) -> int:
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])

        return self.parents[i]

    def union(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return

        ranki = self.ranks[i]
        rankj = self.ranks[j]

        if ranki < rankj:
            self.parents[i] = j
            self.counts[j] += self.counts[i]
        elif ranki == rankj:
            self.parents[j] = i
            self.ranks[i] += 1
            self.counts[i] += self.counts[j]
        else:
            self.parents[j] = i
            self.counts[i] += self.counts[j]

    def count(self, i: int) -> int:
        return self.counts[self.find(i)]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        index = lambda x, y: x * n + y

        m = len(grid)
        n = len(grid[0])

        dsu = DisjointSet(m * n)

        _max = 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue

                if i - 1 >= 0 and grid[i - 1][j]:
                    dsu.union(index(i, j), index(i - 1, j))
                if j - 1 >= 0 and grid[i][j - 1]:
                    dsu.union(index(i, j), index(i, j - 1))

                _max = max(_max, dsu.count(index(i, j)))

        return _max


# @lc code=end
