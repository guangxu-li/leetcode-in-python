#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from functools import reduce


class Solution:
    dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    def valid(self, i: int, j: int) -> bool:
        return 0 <= i < self.m and 0 <= j < self.n

    def calc(self, i: int, j: int) -> int:
        return reduce(
            lambda cnt, dir: cnt
            + int(self.valid(i + dir[0], j + dir[1]) and self.board[i + dir[0]][j + dir[1]] == "M"),
            self.dirs,
            0,
        )

    def update(self, i: int, j: int) -> None:
        if self.board[i][j] != "M" and self.board[i][j] != "E":
            return

        if self.board[i][j] == "M":
            self.board[i][j] = "X"
            return

        cnt_mine = self.calc(i, j)
        if cnt_mine:
            self.board[i][j] = str(cnt_mine)
        else:
            self.board[i][j] = "B"
            for dir in self.dirs:
                ni, nj = i + dir[0], j + dir[1]
                if self.valid(ni, nj):
                    self.update(ni, nj)

    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        self.m, self.n, self.board = len(board), len(board[0]), board
        self.update(*click)

        return board


# @lc code=end
