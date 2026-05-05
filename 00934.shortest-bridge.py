#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
from collections import deque


class Solution:
    def get_boundaries(self, i: int, j: deque) -> set:
        cells, border = deque([(i, j)]), set()

        while cells:
            i, j = cells.popleft()
            if self.A[i][j] < 0:
                continue
            self.A[i][j] = -1

            for dir in self.dirs:
                ni, nj = i + dir[0], j + dir[1]
                if 0 <= ni < len(self.A) and 0 <= nj < len(self.A[0]):
                    if not self.A[ni][nj]:
                        border.add((i, j, 0))
                    elif self.A[ni][nj] == 1:
                        cells.append((ni, nj))

        return border

    def get_first(self):
        for i, row in enumerate(self.A):
            for j, val in enumerate(row):
                if val:
                    return (i, j)

    def shortestBridge(self, A: list[list[int]]) -> int:
        self.dirs, self.A = [[-1, 0], [1, 0], [0, -1], [0, 1]], A.copy()
        border = deque(self.get_boundaries(*self.get_first()))

        while border:
            i, j, d = border.popleft()

            for dir in self.dirs:
                ni, nj = i + dir[0], j + dir[1]
                if 0 <= ni < len(A) and 0 <= nj < len(A[0]) and self.A[ni][nj] >= 0:
                    if self.A[ni][nj] == 1:
                        return d
                    border.append((ni, nj, d + 1))
                    self.A[ni][nj] = -1

        return 0


# @lc code=end
