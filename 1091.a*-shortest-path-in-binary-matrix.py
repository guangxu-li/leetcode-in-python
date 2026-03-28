#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
import heapq


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        dirs = [[1, 1], [1, 0], [0, 1], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        n = len(grid)
        
        h = lambda i, j: max(n - i, n - j)
        valid = lambda i, j: 0 <= i < n and 0 <= j < n and not grid[i][j]

        paths = [(h(0, 0), 1, (0, 0))]
        while paths:
            _, distance, (i, j) = heapq.heappop(paths)
            if not valid(i, j):
                continue
            grid[i][j] = 1

            if (i, j) == (n - 1, n - 1):
                return distance
            
            for dir in dirs:
                v = (i + dir[0], j + dir[1])
                heapq.heappush(paths, (h(*v) + 1 + distance, distance + 1, v))
        return -1

# @lc code=end


