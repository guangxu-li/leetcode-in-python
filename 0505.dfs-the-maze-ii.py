#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start
from typing import List


class Solution:
    DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def can_pass(self, i: int, j: int) -> bool:
        return i >= 0 and i < self.m and j >= 0 and j < self.n and not self.maze[i][j]

    def roll(self, i: int, j: int) -> int:
        for dir in self.DIRS:
            x, y = i, j
            cnt = 0
            while self.can_pass(x + dir[0], y + dir[1]):
                x, y = x + dir[0], y + dir[1]
                cnt += 1

            if self.dist[x][y] > self.dist[i][j] + cnt:
                self.dist[x][y] = self.dist[i][j] + cnt
                self.roll(x, y)

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        self.maze = maze
        self.m = len(maze)
        self.n = len(maze[0])
        self.dist = [[float("inf")] * self.n for _ in range(self.m)]

        self.dist[start[0]][start[1]] = 0
        self.roll(*start)
        shortest = self.dist[destination[0]][destination[1]]

        return shortest if shortest != float("inf") else -1


# @lc code=end
