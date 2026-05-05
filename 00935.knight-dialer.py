#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
import numpy as np


class Solution:
    def knightDialer(self, n: int) -> int:
        """
        A is adjency matrix, number of n-length paths for i -> j equals to (i, j) in A^n
        """

        adj = np.array(
            [
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            ]
        )

        counter, N, mod = np.identity(10, int), n - 1, 10 ** 9 + 7
        while N:
            if N % 2:
                counter = counter @ adj % mod
            adj = adj @ adj % mod
            N //= 2

        return 10 if n == 1 else np.sum(counter) % mod


# @lc code=end
