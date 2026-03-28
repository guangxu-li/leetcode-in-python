#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
from typing import List

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self) -> None:
        pass


class Solution:
    def is_leaf(self, row_lo: int, row_hi: int, col_lo: int, col_hi: int) -> bool:
        return all(c == self.grid[row_lo][col_lo] for row in self.grid[row_lo:row_hi] for c in row[col_lo:col_hi])

    def build_quat_tree(self, row_lo: int, row_hi: int, col_lo: int, col_hi: int) -> "Node":
        print("---")
        print("row:", row_lo, row_hi)
        print("col:", col_lo, col_hi)

        if self.is_leaf(row_lo, row_hi, col_lo, col_hi):
            return Node(bool(self.grid[row_lo][col_lo]), True, None, None, None, None)

        row_mid = (row_lo + row_hi) // 2
        col_mid = (col_lo + col_hi) // 2

        top_left = self.build_quat_tree(row_lo, row_mid, col_lo, col_mid)
        top_right = self.build_quat_tree(row_lo, row_mid, col_mid, col_hi)
        bottom_left = self.build_quat_tree(row_mid, row_hi, col_lo, col_mid)
        bottom_right = self.build_quat_tree(row_mid, row_hi, col_mid, col_hi)

        return Node(False, False, top_left, top_right, bottom_left, bottom_right)

    def construct(self, grid: List[List[int]]) -> "Node":
        self.grid = grid
        n = len(grid)

        return self.build_quat_tree(0, n, 0, n)


# @lc code=end
