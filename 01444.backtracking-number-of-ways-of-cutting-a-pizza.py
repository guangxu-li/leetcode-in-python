#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#

# Constraints:
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza consists of characters 'A' and '.' only.

# @lc code=start
from functools import lru_cache
from itertools import accumulate
from typing import List


# dfs(i, j, k) is the number of ways to cut the pizza into k pieces with k - 1 cuts
#   - top-left corner is (i, j)
#   - bottom-right corner is (0, 0)
# dfs(0, 0, k) is the answer
class Solution:
    MOD = 10**9 + 7

    def __init__(self) -> None:
        self.pizza = []
        # self.apples[i][j] is the number of apples in the rectangle from (i, j) to (m - 1, n - 1)
        self.apples = []
        self.m = 0
        self.n = 0

    # calculate self.pre_sum
    def count_apples(self) -> None:
        self.apples = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m - 1, -1, -1):
            for j in range(self.n - 1, -1, -1):
                self.apples[i][j] = self.apples[i][j + 1] + self.apples[i + 1][j] - self.apples[i + 1][j + 1]
                self.apples[i][j] += self.pizza[i][j] == "A"


    @lru_cache(None)
    def dfs(self, r, c, k: int) -> int:
        if self.apples[r][c] == 0:
            return 0

        if k == 0:
            return 1

        cnt = 0
        for nr in range(r + 1, self.m):
            if self.apples[r][c] > self.apples[nr][c]:
                cnt = (cnt + self.dfs(nr, c, k - 1)) % self.MOD

        for nc in range(c + 1, self.n):
            if self.apples[r][c] > self.apples[r][nc]:
                cnt = (cnt + self.dfs(r, nc, k - 1)) % self.MOD

        return cnt

    def ways(self, pizza: List[str], k: int) -> int:
        self.pizza = pizza
        self.m = len(pizza)
        self.n = len(pizza[0])
        self.count_apples()

        return self.dfs(0, 0, k - 1)


# @lc code=end
