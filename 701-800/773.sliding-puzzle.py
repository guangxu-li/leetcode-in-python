#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        board, dirs = sum(board, []), [-3, 3, -1, 1]
        paths = defaultdict(lambda: float("inf"), {str(board): 0})

        heuristic = lambda b: sum(abs((b[i] + 5) % 6 - i) for i in range(6))

        boards = [(heuristic(board), board.index(0), board.copy())]
        while boards:
            h, i, b = heapq.heappop(boards)
            moves = paths[str(b)]

            if not h - moves:
                return moves

            for dir in dirs:
                ni = i + dir
                if not 0 <= ni < 6 or abs(i // 3 - ni // 3) + abs(i % 3 - ni % 3) != 1:
                    continue

                nb = b.copy()
                nb[i], nb[ni] = nb[ni], nb[i]
                nb_str = str(nb)
                if moves + 1 < paths[nb_str]:
                    paths[nb_str] = moves + 1
                    heapq.heappush(boards, (heuristic(nb) + paths[nb_str], ni, nb))

        return -1


# @lc code=end
