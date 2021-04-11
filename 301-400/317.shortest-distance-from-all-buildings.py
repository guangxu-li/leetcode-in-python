#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#

# @lc code=start
from collections import deque, defaultdict


class Solution:
    def bfs(
        self, grid: list[list[int]], distances: defaultdict, i: int, j: int, mark: int
    ) -> None:
        valid = (
            lambda i, j: 0 <= i < len(grid)
            and 0 <= j < len(grid[0])
            and grid[i][j] != 2
        )

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        cells, reachable = deque([(i, j, 0)]), {(i, j)}
        while cells:
            x, y, d = cells.popleft()

            if (x, y) != (i, j):
                distances[(x, y)] += d

            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]
                if not valid(nx, ny):
                    continue

                if grid[nx][ny] == 1:
                    reachable.add((nx, ny))
                if grid[nx][ny] == mark:
                    grid[nx][ny] -= 1
                    cells.append((nx, ny, d + 1))

        return len(reachable)

    def shortestDistance(self, grid: list[list[int]]) -> int:
        distances, cnt, mark = defaultdict(int), sum(row.count(1) for row in grid), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue

                if self.bfs(grid, distances, i, j, mark) != cnt:
                    return -1
                mark -= 1

        return min(
            [distances[(i, j)] for i, j in distances if grid[i][j] == -cnt], default=-1
        )


# @lc code=end
