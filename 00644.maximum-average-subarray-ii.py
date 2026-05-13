#
# @lc app=leetcode id=644 lang=python3
#
# [644] Maximum Average Subarray II
#

# @lc code=start
from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class MaxSlopeCHT:
    def __init__(self):
        self.deque = deque()

    def _is_bad(self, a: Point, b: Point, c: Point) -> bool:
        # slope(a, b) >= slope(b, c)
        # a.y - b.y / a.x - b.x >= b.y - c.y / b.x - c.x
        return (a.y - b.y) * (b.x - c.x) >= (a.x - b.x) * (b.y - c.y)

    def _is_leq(self, a: Point, b: Point, c: Point) -> bool:
        # slope(a, c) <= slope(b, c)
        return (a.y - c.y) * (b.x - c.x) <= (b.y - c.y) * (a.x - c.x)

    def add_point(self, c: Point):
        while self.deque and self.deque[-1].x == c.x:
            if self.deque[-1].y >= c.y:
                self.deque.pop()

        while len(self.deque) >= 2 and self._is_bad(self.deque[-2], self.deque[-1], c):
            self.deque.pop()

        self.deque.append(c)

    def query(self, c: Point) -> int:
        while len(self.deque) >= 2 and self._is_leq(self.deque[0], self.deque[1], c):
            self.deque.popleft()

        return (c.y - self.deque[0].y) / (c.x - self.deque[0].x)



class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cht = MaxSlopeCHT()

        n = len(nums)
        accu = [0] * (n + 1)
        for i, num in enumerate(nums):
            accu[i + 1] = accu[i] + num

        avg = min(nums)
        for i in range(k, n + 1):
            cht.add_point(Point(i - k, accu[i - k]))
            avg = max(avg, cht.query(Point(i, accu[i])))

        return avg

# @lc code=end
