#
# @lc app=leetcode id=2345 lang=python3
#
# [2345] Finding the Number of Visible Mountains
#

# @lc code=start
from collections import Counter



# 1. Convert to list of (left, right) pairs
# 2. Sort by (left, -right)
# 3. Then this problem is converted to non-overlapping interval count problem
# 4. But do remember to remove those intervals with exactly same left and right
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        intervals = [(x - y, x + y) for x, y in peaks]
        intervals = sorted(intervals, key=lambda a: (a[0], -a[1]))
        counters = Counter(intervals)

        cnt = 0
        max_hi = float("-inf")
        for lo, hi in intervals:
            cnt += (hi > max_hi) and (counters[(lo, hi)] == 1)
            max_hi = max(max_hi, hi)
        return cnt


# @lc code=end
