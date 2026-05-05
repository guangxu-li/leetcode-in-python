#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#

# @lc code=start
class Solution:
    def getpath(self, i: int, j: int, dir: str) -> str:
        if (
            (i, j) in self.visited
            or i < 0
            or i == self.m
            or j < 0
            or j == self.n
            or not self.grid[i][j]
        ):
            return ""
        self.visited.add((i, j))

        return (
            dir
            + self.getpath(i - 1, j, "u")
            + self.getpath(i + 1, j, "d")
            + self.getpath(i, j - 1, "l")
            + self.getpath(i, j + 1, "r")
            + "b"
        )

    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        self.grid, self.m, self.n, self.visited = grid, len(grid), len(grid[0]), set()
        islands = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                path = self.getpath(i, j, "^")
                if path:
                    islands.add(path)

        return len(islands)


# @lc code=end
