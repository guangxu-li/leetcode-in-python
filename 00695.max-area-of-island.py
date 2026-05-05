#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        valid = lambda x, y: 0 <= x < m and 0 <= y < n and grid[x][y]

        def area_bfs(i: int, j: int) -> int:
            area = 0
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                if not valid(x, y):
                    continue
                grid[x][y] = 0
                area += 1

                for xoffset, yoffset in dirs:
                    nx, ny = x + xoffset, y + yoffset
                    q.append((nx, ny))

            return area

        def area_dfs(i: int, j: int) -> int:
            if not valid(i, j):
                return 0
            grid[i][j] = 0
            area = 1
            for ioffset, joffset in dirs:
                ni, nj = i + ioffset, j + joffset
                area += area_dfs(ni, nj)
            return area

        def area_dfs_iterative(i: int, j: int) -> int:
            area = 0
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if not valid(x, y):
                    continue
                grid[x][y] = 0
                area += 1

                for xoffset, yoffset in dirs:
                    nx, ny = x + xoffset, y + yoffset
                    stack.append((nx, ny))
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # max_area = max(max_area, area_bfs(i, j))
                # max_area = max(max_area, area_dfs(i, j))
                max_area = max(max_area, area_dfs_iterative(i, j))

        return max_area


# @lc code=end
