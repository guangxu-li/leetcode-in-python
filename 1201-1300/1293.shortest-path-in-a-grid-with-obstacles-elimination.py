#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
import heapq


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(grid), len(grid[0])

        estimate = lambda i, j: m - i + n - j
        valid = (
            lambda i, j, rem: 0 <= i < m
            and 0 <= j < n
            and not (grid[i][j] and not rem)
            and (i, j, rem) not in visited
        )

        paths, visited = [(m + n, 0, (0, 0), k)], set((0, 0, m + n))
        while paths:
            _, distance, (i, j), rem = heapq.heappop(paths)
            if (i, j) == (m - 1, n - 1):
                return distance

            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                if not valid(ni, nj, rem):
                    continue
                nk = rem - grid[ni][nj]
                visited.add((ni, nj, nk))

                heapq.heappush(
                    paths,
                    (
                        estimate(ni, nj) + distance + 1,
                        distance + 1,
                        (ni, nj),
                        nk,
                    ),
                )
        return -1


# @lc code=end
