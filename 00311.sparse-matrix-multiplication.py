#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        cols = [[(i, val) for i, val in enumerate(col) if val] for col in zip(*mat2)]
        return [[sum(row[i] * val for i, val in col) for col in cols] for row in mat1]


# @lc code=end
