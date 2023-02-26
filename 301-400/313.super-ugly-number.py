#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglys = [1]
        for _ in range(n - 1):
            ugly = heapq.heappop(uglys)
            for prime in primes:
                heapq.heappush(uglys, ugly * prime)
                if ugly % prime == 0:
                    break # to make sure we can generate uglys only with itself as much as possible

        return uglys[0]
# @lc code=end
