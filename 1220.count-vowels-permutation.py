#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start
import numpy as np


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        A is adjency matrix, number of n-length paths for i -> j equals to (i, j) in A^n
        """

        adj = np.array(
            [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 1], [1, 0, 0, 0, 0]]
        )

        counter, N, mod = np.identity(5, int), n - 1, 10 ** 9 + 7
        while N:
            if N % 2:
                counter = counter @ adj % mod
            adj = adj @ adj % mod
            N //= 2

        return 5 if n == 1 else np.sum(counter) % mod
# @lc code=end
