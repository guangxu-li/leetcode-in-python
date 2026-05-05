#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, newColor: int
    ) -> list[list[int]]:
        anchor = image[sr][sc]
        if anchor == newColor:
            return image

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n, cells = len(image), len(image[0]), deque([(sr, sc)])

        valid = lambda i, j: 0 <= i < m and 0 <= j < n and image[i][j] == anchor

        while cells:
            i, j = cells.popleft()
            if not valid(i, j):
                continue
            image[i][j] = newColor

            for dir in dirs:
                cells.append((i + dir[0], j + dir[1]))

        return image


# @lc code=end
