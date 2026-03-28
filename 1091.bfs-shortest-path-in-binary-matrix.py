#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        dirs = [[1, 1], [1, 0], [0, 1], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        cells, visited, n, cnt = deque(), set(), len(grid), 1
        cells.append((0, 0))

        valid = lambda i, j: 0 <= i < n and 0 <= j < n and not grid[i][j]

        while cells:
            for i in range(len(cells)):
                i, j = cells.popleft()
                if not valid(i, j) or (i, j) in visited:
                    continue
                visited.add((i, j))
                if (i, j) == (n - 1, n - 1):
                    return cnt

                for dir in dirs:
                    cells.append((i + dir[0], j + dir[1]))
            cnt += 1

        return -1
# @lc code=end

