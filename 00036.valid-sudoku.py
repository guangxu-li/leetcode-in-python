#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each bit reprensent one num existence
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                bit = 1 << num

                ri, ci, bi = i, j, i // 3 * 3 + j // 3
                if bit & rows[ri]:
                    return False
                if bit & cols[ci]:
                    return False
                if bit & boxes[bi]:
                    return False
                rows[ri] |= bit
                cols[ci] |= bit
                boxes[bi] |= bit

        return True


# @lc code=end
