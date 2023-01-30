#
# @lc app=leetcode id=1165 lang=python3
#
# [1165] Single-Row Keyboard
#

# @lc code=start
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        layout = {ch: i for i, ch in enumerate(keyboard)}
        cur = moves = 0
        for ch in word:
            nxt = layout[ch]
            moves += abs(nxt - cur)
            cur = nxt

        return moves
# @lc code=end
