#
# @lc app=leetcode id=499 lang=python3
#
# [499] The Maze III
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])
        can_pass = lambda x, y: x >= 0 and x < m and y >= 0 and y < n and not maze[x][y]

        dirs = [['d', 1, 0],  ['l', 0, -1], ['r', 0, 1],  ['u', -1, 0] ]
        q = [(0, "", ball[0], ball[1])] # min heap based on the distance. (dist, path, x, y)
        distance = [[float("inf")] * n for _ in range(m)]
        distance[ball[0]][ball[1]] = 0

        ans = "impossible"

        while q:
            d, path, x, y = heapq.heappop(q)
            if [x, y] == hole:
                ans = path if ans == "impossible" else min(ans, path)
                continue

            for dir, dx, dy in dirs:
                nx, ny = x, y
                cnt = 0
                while can_pass(nx + dx, ny + dy):
                    nx, ny = nx + dx, ny + dy
                    cnt += 1

                    if [nx, ny] == hole:
                        break

                if distance[nx][ny] > d + cnt:
                    distance[nx][ny] = d + cnt
                    q.append((d + cnt, path + dir, nx, ny))

        return ans


# @lc code=end
