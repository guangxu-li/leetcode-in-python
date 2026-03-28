#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.n = n
        self.groups = defaultdict(None)

    def find(self, i: int) -> int:
        return i if self.groups[i] == i else self.find(self.groups[i][0])

    def get_groups(self) -> List[List[int]]:
        ret = []
        lo = 0
        while lo < self.n:
            group = self.groups[lo]
            if not group:
                lo += 1
                continue

            ret.append(group)
            lo = group[lo] + 1

        return ret

    def setnx(self, i: int) -> None:
        if i in self.groups:
            return

        self.groups[i] = [i, i]

    # union connects i and j. Expect i < j
    def union(self, i: int, j: int) -> None:
        i, j = self.find(i), self.find(j)

        if i == j:
            return

        if i > j:
            i, j = j, i

        # The smaller value acts as the root. Think the root as the start of the interval.
        self.groups[j][0] = i
        self.groups[i] = self.groups[j]

    def print(self) -> None:
        for i in range(self.n):
            if i in self.groups:
                print("i:", i, "group:", self.groups[i])
        print("===")


class SummaryRanges:
    def __init__(self):
        n = 10**4 + 1
        self.bucket = [0] * n
        self.dsu = DisjointSet(n)

    def addNum(self, val: int) -> None:
        if self.bucket[val]:
            return

        self.bucket[val] |= 1
        self.dsu.setnx(val)

        if val > 0 and self.bucket[val - 1]:
            self.dsu.union(val - 1, val)
        if val < len(self.bucket) - 1 and self.bucket[val + 1]:
            self.dsu.union(val, val + 1)

    def getIntervals(self) -> List[List[int]]:
        return self.dsu.get_groups()


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end
