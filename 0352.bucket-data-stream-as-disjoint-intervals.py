#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
from typing import List


class SummaryRanges:
    def __init__(self):
        _max = 10**4
        self.bucket = [0] * (_max + 1)

    def addNum(self, val: int) -> None:
        self.bucket[val] |= 1

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for num in filter(self.bucket):
            if intervals and intervals[-1][1] + 1 == num:
                intervals[-1][1] = num
            else:
                intervals.append([num, num])

        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end
