#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [None] * n
        self.cnt = 0

    def find(self, i: int) -> int:
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        
        return i

    def union(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        if i != j:
            self.cnt -= 1
            self.parent[j] = i


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        counter = []

        for x, y in positions:
            i = x * n + y 
            if uf.parent[i] is None:
                uf.cnt += 1
                uf.parent[i] = i

                if x > 0 and uf.parent[i - n] is not None:
                    uf.union(i - n, i)
                if x < m - 1 and uf.parent[i + n] is not None:
                    uf.union(i, i + n)
                if y > 0 and uf.parent[i - 1] is not None:
                    uf.union(i - 1, i)
                if y < n - 1 and uf.parent[i + 1] is not None:
                    uf.union(i, i + 1)

            counter.append(uf.cnt)

        return counter
# @lc code=end
