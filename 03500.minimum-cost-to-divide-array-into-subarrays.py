#
# @lc app=leetcode id=3500 lang=python3
#
# [3500] Minimum Cost to Divide Array Into Subarrays
#

# @lc code=start
import math
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Line:
    # y = m * x + b
    m: int
    b: int

    def value(self, x: int) -> int:
        return self.m * x + self.b


# Min CHT
# Assumption here:
# - slopes are inserted in non-increasing order
# - query x is non-decreasing
class MonotonicCHT:
    def __init__(self):
        self.dq = deque()

    def _is_bad(self, l1: Line, l2: Line, l3: Line) -> bool:
        # l2 is bad if:
        #
        # x(l1, l2) >= x(l2, l3)
        #
        # x(l1, l2) = (b1 - b2) / (m2 - m1)
        # x(l2, l3) = (b2 - b3) / (m3 - m2)
        #
        # Avoid floating point:
        #
        # (b1 - b2) * (m3 - m2) >= (b2 - b3) * (m2 - m1)
        return (l1.b - l2.b) * (l3.m - l2.m) >= (l2.b - l3.b) * (l2.m - l1.m)

    def _is_leq(self, l1: Line, l2: Line, x: int) -> bool:
        # For min query:
        # if l1(x) >= l2(x), then l1 is no longer useful for current/future x.
        return l1.value(x) >= l2.value(x)

    def add_line(self, l: Line) -> None:
        while self.dq and self.dq[-1].m == l.m:
            if self.dq[-1].b <= l.b:
                return

            self.dq.pop()

        while len(self.dq) >= 2 and self._is_bad(self.dq[-2], self.dq[-1], l):
            self.dq.pop()

        self.dq.append(l)

    def query(self, x: int) -> int:
        while len(self.dq) >= 2 and self._is_leq(self.dq[0], self.dq[1], x):
            self.dq.popleft()

        return self.dq[0].value(x)


class Solution:
    def minimumCost(self, nums: list[int], cost: list[int], k: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        C = [0] * (n + 1)

        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            C[i + 1] = C[i] + cost[i]

        # 2D CHT
        # dp[p][i] = min_cost of dividing nums[:i] into p subarrays
        # dp[p][i] = min_{j < i}{ dp[p - 1][j] + (P[i] + k * p) * (C[i] - C[j] }
        #          = min_{j < i}{ dp[p - 1][j] + (P[i] + k * p) * C[i] - (P[i] + k * p) * C[j] }
        #          = (P[i] + k * p) * C[i] + min_{j < i}{ dp[p - 1][j] - (P[i] + k * p) * C[j] }
        #          = x * C[i] + min_{j < i}{ -C[j] * x + dp[p - 1][j] }
        #
        # x = P[i] + k * p
        # m = -C[j]
        # b = dp[p - 1][j]
        #
        # x: non-decreasing
        # m: non-increasing
        #
        # 1D CHT
        # dp[p][i] = min_{j < i}{ dp[p - 1][j] + (P[i] + k * p) * (C[i] - C[j]) }
        #          = min_{j < i}{ dp[p - 1][j] + P[i] * (C[i] - C[j]) + (k * p) * (C[i] - C[j]) }
        #
        # let cost(j, i) present C[i] - C[j], then the cost part that depends on the p is (k * p) * cost(j, i)
        #
        # suppose partition is [0, a), [a, b), [b, n)
        #
        # 2D DP cost part formula:
        # cost = k * 1 * cost(0, a)
        #      + k * 2 * cost(a, b)
        #      + k * 3 * cost(b, n)
        # cost = k * (cost(0, a)+cost(a,b)+cost(b,n))
        #      + k * (cost(a, n) + k * cost(b, n))
        #      + k * cost(b, n)
        # cost = k * cost(0, n) +  k * (a, n) + k * (b, n)
        #
        # dp[p][i] = min_{j < i}{ dp[p - 1][j] + P[i] * (C[i] - C[j]) + (k * p) * (C[i] - C[j]) }
        # => dp[i] = min_{j < i}{ dp[j] + P[i] * (C[i] - C[j]) + k * (C[n] - C[j]) }
        #          = min_{j < i}{ dp[j] + P[i] * (C[i] - C[j]) + k * (C[n] - C[j]) }
        #          = min_{j < i}{ dp[j] + P[i] * C[i] - P[i] * C[j] + k * C[n] - k*C[j] }
        #          = P[i] * C[i] + k*C[n] + min_{j < i}{ dp[j] - (P[i] + k) * C[j]}
        #
        # x = P[i] + k
        # m = -C[j]
        # b = dp[j]
        #
        # x: non-decreasing
        # m: non-increasing

        dp = [math.inf] * (n + 1)
        dp[0] = 0

        cht = MonotonicCHT()
        cht.add_line(Line(0, 0))

        for i in range(1, n + 1):
            dp[i] = P[i] * C[i] + k * C[n] + cht.query(P[i] + k)
            cht.add_line(Line(-C[i], dp[i]))

        return dp[-1]
# @lc code=end
