#
# @lc app=leetcode id=488 lang=python3
#
# [488] Zuma Game
#

# @lc code=start
from functools import lru_cache
from math import log2


class Solution:
    def dedup(self, board: str) -> str:
        anchor = 0
        for i, b in enumerate(board):
            if b != board[anchor]:
                if i - anchor >= 3:
                    return self.dedup(board[:anchor] + board[i:])
                anchor = i
        
        return board
    
    @lru_cache(maxsize=None)
    def solve(self, board: str, hand: str) -> int:
        if board == "#":
            return 0
        
        board_set = set(board)
        hand = "".join(h for h in hand if h in board_set)

        ret = float("inf")
        for i, h in enumerate(hand):
            for j in range(len(board)):
                nxt_hand = hand[:i] + hand[i + 1:]
                nxt_board = self.dedup(board[:j] + h + board[j:])
                ret = min(ret, 1 + self.solve(nxt_board, nxt_hand))
                
        return ret

    def findMinStep(self, board: str, hand: str) -> int:
        step = self.solve(board + "#", hand)
        return -1 if step == float("inf") else step
# @lc code=end
