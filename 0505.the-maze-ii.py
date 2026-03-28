#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        can_pass = lambda x, y: x >= 0 and x < m and y >= 0 and y < n and not maze[x][y]

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        q = [(0, start[0], start[1])]  # min heap based on the distance, (dist, x, y)
        distances = [[float("inf")] * n for _ in range(m)]
        distances[start[0]][start[1]] = 0

        while q:
            d, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return d

            for dx, dy in dirs:
                nx, ny = x, y
                cnt = 0
                while can_pass(nx + dx, ny + dy):
                    nx, ny = nx + dx, ny + dy
                    cnt += 1

                if distances[nx][ny] > d + cnt:
                    distances[nx][ny] = d + cnt
                    q.append((d + cnt, nx, ny))

        return -1


# @lc code=end
