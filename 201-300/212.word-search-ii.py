#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from collections import defaultdict
from itertools import product
from functools import reduce


class Solution:
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        Trie = lambda: defaultdict(Trie)
        root = Trie()

        for word in words:
            reduce(dict.__getitem__, word, root)["END"] = word

        def search(node: defaultdict[str, defaultdict], i: int, j: int):
            if "END" in node:
                found.append(node.pop("END"))

            if not node or i < 0 or i == m or j < 0 or j == n:
                return

            ch = board[i][j]
            board[i][j] = "."
            for dir in self.dirs:
                search(node[ch], i + dir[0], j + dir[1])
            board[i][j] = ch

        m, n, found = len(board), len(board[0]), []
        for i, j in product(range(m), range(n)):
            search(root, i, j)

        return found


# @lc code=end
