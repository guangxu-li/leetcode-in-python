#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # dp[i][j] means the sumRegion(0, 0, i, j)
        # dp[0][0] = matrix[0][0]
        # dp[0][j] = matrix[0][j] + dp[0][j - 1]
        # dp[i][0] = matrix[i][0] + dp[i - 1][0]
        # dp[i][j] = matrix[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        m, n = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dp[i][j] = matrix[i][j]
                if i > 0:
                    self.dp[i][j] += self.dp[i - 1][j]
                if j > 0:
                    self.dp[i][j] += self.dp[i][j - 1]
                if i > 0 and j > 0:
                    self.dp[i][j] -= self.dp[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        area = self.dp[row2][col2]
        if row1 > 0:
            area -= self.dp[row1 - 1][col2]
        if col1 > 0:
            area -= self.dp[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            area += self.dp[row1 - 1][col1 - 1]
        return area


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)# @lc code=end
