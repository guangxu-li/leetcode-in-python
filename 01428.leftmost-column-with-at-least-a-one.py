#
# @lc app=leetcode id=1428 lang=python3
#
# [1428] Leftmost Column With At Least A One
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, matrix: "BinaryMatrix") -> int:
        m, n = matrix.dimensions()

        r, c = 0, n - 1
        ans = -1
        while r < m and c >= 0:
            if matrix.get(r, c) == 1:
                ans = c
                c -= 1
            else:
                r += 1

        return ans


# @lc code=end
