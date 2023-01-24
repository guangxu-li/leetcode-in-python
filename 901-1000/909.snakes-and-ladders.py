#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque
from typing import List, Tuple


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def decode(k: int) -> Tuple[int, int]:
            x, y = (k - 1) // n, (k - 1) % n
            x, y = ~x, y if x % 2 == 0 else ~y

            return x, y

        dist = [0] * (n + 1)
        q = deque([1])
        while q:
            cur = q.popleft()
            for next in range(cur + 1, cur + 7):
                x, y = decode(next)
                if board[x][y] > 0:
                    next = board[x][y]
                if next == n * n:
                    return 1 + dist[cur]
                if dist[next] == 0:
                    dist[next] = 1 + dist[cur]
                    q.append(next)

        return -1


# @lc code=end
