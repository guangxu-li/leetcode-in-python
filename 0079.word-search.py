#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from itertools import product


class Solution:
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def __init__(self):
        self.visited = set()

    def valid(self, i: int, j: int, k: int) -> bool:
        return (
            0 <= i < self.m
            and 0 <= j < self.n
            and self.board[i][j] == self.word[k]
            and (i, j) not in self.visited
        )

    def found(self, i: int, j: int, k: int) -> bool:
        if k == len(self.word):
            return True

        self.visited.add((i, j))
        res = any(
            self.found(i + dir[0], j + dir[1], k + 1)
            for dir in self.dirs
            if self.valid(i + dir[0], j + dir[1], k)
        )
        self.visited.remove((i, j))

        return res

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board, self.word = board, word
        self.m, self.n = len(board), len(board[0])

        return any(
            self.found(i, j, 1)
            for i, j in product(range(self.m), range(self.n))
            if board[i][j] == word[0]
        )


# @lc code=end
