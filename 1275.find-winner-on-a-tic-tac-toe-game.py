#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        rows, cols, hill, dale, mark = [0, 0, 0], [0, 0, 0], 0, 0, 1
        for i, j in moves:
            rows[i] += mark
            cols[j] += mark
            hill += mark * (i == 2 - j)
            dale += mark * (i == j)

            if abs(rows[i]) == 3:
                return "A" if rows[i] == 3 else "B"
            elif abs(cols[j]) == 3:
                return "A" if cols[j] == 3 else "B"
            elif abs(hill) == 3:
                return "A" if hill == 3 else "B"
            elif abs(dale) == 3:
                return "A" if dale == 3 else "B"
            mark = -mark
        
        return "Pending" if len(moves) < 9 else "Draw"
# @lc code=end



