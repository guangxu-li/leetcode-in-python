#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from math import trunc


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        cnt = 0
        for f in [1, 0] + flowerbed + [0, 1]:
            n, cnt = n - trunc((cnt - 1) / 2) if f else n, 0 if f else cnt + 1

        return n <= 0


# @lc code=end
