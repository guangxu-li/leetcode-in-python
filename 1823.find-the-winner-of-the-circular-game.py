#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
from functools import reduce


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        winner[n] = (winner[n - 1] + k) % n
        """
        # winner = 0
        # for i in range(1, n + 1):
        #     winner = (winner + k) % i
        
        # return winner + 1

        return reduce(lambda winner, i: (winner + k) % i, range(n + 1)) + 1
# @lc code=end
