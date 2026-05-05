#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from typing import List


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.tree = [0] * (4 * n - 1)

    def update(self, lo: int, hi: int, node: int, i: int, val: int) -> None:
        if lo == hi:
            self.tree[node] = val
            return

        mid = (lo + hi) >> 1
        if i <= mid:
            self.update(lo, mid, node * 2 + 1, i, val)
        else:
            self.update(mid + 1, hi, node * 2 + 2, i, val)

        self.tree[node] = max(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def query(self, lo: int, hi: int, node: int, qlo: int, qhi: int) -> int:
        if qlo > hi or qhi < lo:
            return 0

        if qlo <= lo <= hi <= qhi:
            return self.tree[node]

        mid = (lo + hi) >> 1  # left end
        left = self.query(lo, mid, node * 2 + 1, qlo, qhi)
        right = self.query(mid + 1, hi, node * 2 + 2, qlo, qhi)

        return max(left, right)


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = max(ages)
        st = SegmentTree(n + 1)
        _max = curr = 0
        for score, age in sorted(zip(scores, ages)):
            curr = score + st.query(0, n, 0, 0, age)
            st.update(0, n, 0, age, curr)
            _max = max(_max, curr)

        return _max


# @lc code=end
