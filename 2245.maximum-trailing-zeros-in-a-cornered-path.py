#
# @lc app=leetcode id=2245 lang=python3
#
# [2245] Maximum Trailing Zeros in a Cornered Path
#

# @lc code=start
from functools import lru_cache
from typing import List


# Think in one dimension first.
# Assume we have an array and we wanna find the maximum trailing zeros of all product of subarrays
# We can convert it to a prefix sum of 2 or 5 factors problem.
#
# We can accumulate the number of 2 and 5 factors in the prefix sum array.
# And the maximum trailing zeros are the minimum of the number of 2 and 5 factors in the prefix sum array.
#
# This problem is a 2D version of the above problem.
# It's like combine two 1D arrays into a 2D array.
#   - up and left
#   - up and right
#   - down and left
#   - down and right
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def factor_nums(num: int) -> List[int]:
            a, b = 0, 0
            while num % 2 == 0:
                num //= 2
                a += 1
            while num % 5 == 0:
                num //= 5
                b += 1

            return [a, b]

        m = len(grid)
        n = len(grid[0])

        ps_col = [[[0, 0] for _ in range(n)] for _ in range(m)]
        ps_row = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                cur = factor_nums(grid[i][j])
                if i == 0:
                    ps_col[i][j] = cur
                else:
                    up = ps_col[i - 1][j]
                    ps_col[i][j] = [cur[0] + up[0], cur[1] + up[1]]
                if j == 0:
                    ps_row[i][j] = cur
                else:
                    left = ps_row[i][j - 1]
                    ps_row[i][j] = [cur[0] + left[0], cur[1] + left[1]]

        _max = 0
        for i in range(m):
            for j in range(n):
                cur = factor_nums(grid[i][j])

                rightmost = ps_row[i][n - 1]
                downmost = ps_col[m - 1][j]

                # include cur
                left = ps_row[i][j]
                up = ps_col[i][j]

                # not include cur
                right = [rightmost[0] - left[0], rightmost[1] - left[1]]
                down = [downmost[0] - up[0], downmost[1] - up[1]]

                up_left = [left[0] + up[0] - cur[0], left[1] + up[1] - cur[1]]
                up_right = [right[0] + up[0], right[1] + up[1]]
                down_left = [left[0] + down[0], left[1] + down[1]]
                down_right = [right[0] + down[0] + cur[0], right[1] + down[1] + cur[1]]

                _max = max(_max, min(up_left), min(up_right), min(down_left), min(down_right))

        return _max


# @lc code=end
