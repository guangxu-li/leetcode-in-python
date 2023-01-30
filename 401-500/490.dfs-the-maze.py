#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#

# @lc code=start
from typing import List


class Solution:
    DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self) -> None:
        self.visited = set()

    def can_pass(self, i: int, j: int) -> bool:
        if (i, j) in self.visited:
            return False

        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.maze[i][j]:
            return False

        return True

    def can_reach(self, i: int, j: int) -> bool:
        if (i, j) in self.visited:
            return False
        self.visited.add((i, j))

        if (i, j) == self.destination:
            return True

        for dir in self.DIRS:
            ni, nj = i, j
            while self.can_pass(ni + dir[0], nj + dir[1]):
                ni, nj = ni + dir[0], nj + dir[1]

            if self.can_reach(ni, nj):
                return True

        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.maze = maze
        self.m = len(self.maze)
        self.n = len(self.maze[0])
        self.destination = (destination[0], destination[1])

        return self.can_reach(*start)


# @lc code=end
