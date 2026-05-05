#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# @lc code=start
from typing import List


class Solution:
    def __init__(self) -> None:
        self.A = []

    # search_in_row searchs the first element in the row (self.A[r][lo:hi]) that is greater than target.
    def search_in_row(self, r, lo, hi, target: int) -> int:
        while lo < hi:
            i = (lo + hi) >> 1
            m = self.A[r][i]

            if m <= target:
                lo = i + 1
            else:
                hi = i

        return lo

    # search_in_col searchs the first element in the row (self.A[lo:hi][c]) that is greater than target.
    def search_in_col(self, c, lo, hi, target: int) -> int:
        while lo < hi:
            i = (lo + hi) >> 1
            m = self.A[i][c]

            if m <= target:
                lo = i + 1
            else:
                hi = i

        return lo

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.A = matrix
        m = len(matrix)
        n = len(matrix[0])

        r = self.search_in_col(0, 0, m, target)
        if r == 0:
            return False

        c = self.search_in_row(r - 1, 0, n, target)
        if c == 0:
            return False

        return matrix[r - 1][c - 1] == target

# @lc code=end
