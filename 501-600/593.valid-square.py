#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
from functools import reduce
from itertools import combinations


class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        points = [p1, p2, p3, p4]
        if any(p1 == p2 for p1, p2 in combinations(points, 2)):
            return False

        distances = lambda a: {abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2 for b in points}
        return len(reduce(lambda res, s: res | s, map(distances, points))) == 3


# @lc code=end
