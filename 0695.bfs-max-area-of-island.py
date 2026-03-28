#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        valid = lambda x, y: 0 <= x < m and 0 <= y < n

        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def areas(i: int, j: int) -> int:
            s = 0
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                s += 1

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if valid(nx, ny) and grid[nx][ny]:
                        q.append((nx, ny))
                        visited.add((x, y))

            return s

        _max = 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j] or (i, j) in visited:
                    continue
                _max = max(_max, areas(i, j))

        return _max


# @lc code=end
