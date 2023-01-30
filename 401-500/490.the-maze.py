#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#

# @lc cokde=start
from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        destination = tuple(destination)
        m = len(maze)
        n = len(maze[0])

        can_pass = lambda i, j: i >= 0 and i < m and j >= 0 and j < n and not maze[i][j]

        q = deque([start])
        visited = set()
        while q:
            i, j = q.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if (i, j) == destination:
                return True

            for dir in dirs:
                ni, nj = i, j
                while can_pass(ni + dir[0], nj + dir[1]):
                    ni, nj = ni + dir[0], nj + dir[1]

                q.append((ni, nj))

        return False


# @lc code=end
