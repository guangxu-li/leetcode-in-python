#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from typing import List


class BIT:
    def __init__(self, n: int) -> None:
        self.n = n + 1
        self.bit = [0] * self.n

    def update(self, i: int, val: int) -> None:
        while i < self.n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i: int) -> int:
        _max = float("-inf")
        while i:
            _max = max(_max, self.bit[i])
            i -= i & -i

        return _max

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        bit = BIT(max(ages) + 1)

        _max = 0
        for score, age in sorted(zip(scores, ages)):
            curr = score + bit.query(age)
            bit.update(age, curr)
            _max = max(_max, curr)

        return _max
# @lc code=end
