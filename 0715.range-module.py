#
# @lc app=leetcode id=715 lang=python3
#
# [715] Range Module
#

# @lc code=start
from bisect import bisect_left, bisect


class RangeModule:
    def __init__(self):
        self.tracker = []

    def addRange(self, left: int, right: int) -> None:
        lo, hi = bisect_left(self.tracker, left), bisect(self.tracker, right)
        self.tracker[lo:hi] = [left] * (lo % 2 == 0) + [right] * (hi % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        lo, hi = bisect(self.tracker, left), bisect_left(self.tracker, right)
        
        return lo == hi and lo % 2

    def removeRange(self, left: int, right: int) -> None:
        lo, hi = bisect_left(self.tracker, left), bisect(self.tracker, right)
        self.tracker[lo:hi] = [left] * (lo % 2 == 1) + [right] * (hi % 2 == 1)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# @lc code=end
