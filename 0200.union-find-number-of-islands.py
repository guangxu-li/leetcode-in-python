#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.Roots = list(range(n))

    def find(self, x: int) -> int:
        if self.Roots[x] != x:
            return self.find(self.Roots[x])

        return x

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)

        if x != y:
            self.Roots[x] = y
            self.n -= 1

class Solution:
    def hash(self, i, j: int) -> int:
        return i * self.n + j

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        uf = UnionFind(self.m * self.n)

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '0':
                    uf.n -= 1
                else:
                    if i > 0 and grid[i - 1][j] == '1':
                        uf.union(self.hash(i, j), self.hash(i - 1, j))
                    if j > 0 and grid[i][j - 1] == '1':
                        uf.union(self.hash(i, j), self.hash(i, j - 1))

        return uf.n


# @lc code=end
