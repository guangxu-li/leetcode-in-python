#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.tree = [0] * (4 * n - 1)

    def update(self, lo: int, hi: int, cur: int, i: int, val: int) -> None:
        if lo == hi:
            self.tree[cur] = val
            return

        mid = (lo + hi) >> 1
        if i <= mid:
            self.update(lo, mid, cur * 2 + 1, i, val)
        else:
            self.update(mid + 1, hi, cur * 2 + 2, i, val)

        self.tree[cur] = max(self.tree[cur * 2 + 1], self.tree[cur * 2 + 2])

    def query(self, lo: int, hi: int, cur: int, qlo: int, qhi: int) -> int:
        if qlo > hi or qhi < lo:
            return 0
        if qlo <= lo <= hi <= qhi:
            return self.tree[cur]

        mid = (lo + hi) >> 1
        left = self.query(lo, mid, cur * 2 + 1, qlo, qhi)
        right = self.query(mid + 1, hi, cur * 2 + 2, qlo, qhi)

        return max(left, right)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lo = min(nums)
        nums = [num - lo for num in nums]
        hi = max(nums)
        st = SegmentTree(hi + 1)

        _max = 1
        for num in nums:
            curr = 1 + st.query(0, hi, 0, 0, num - 1)
            st.update(0, hi, 0, num, curr)
            _max = max(_max, curr)

        return _max


# @lc code=end
