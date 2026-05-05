#
# @lc app=leetcode id=1825 lang=python3
#
# [1825] Finiding MK Average
#

# @lc code=start
from collections import deque
from math import log2, trunc


class MKAverage:

    def update(self, bit: list[int], i: int, diff: int) -> None:
        while i < len(bit):
            bit[i] += diff
            i += i & -i
        
    def query(self, bit: list[int], i: int, j: int) -> int:
        ret = 0
        while j > i:
            ret += bit[j]
            j -= j & -j
        while i > j:
            ret -= bit[i]
            i -= i & -i
        
        return ret

    def __init__(self, m: int, k: int):
        self.vals, self.m, self.k = deque(), m, k
        self.bit_vals = [0] * (10 ** 5 + 2)
        self.bit_cnt = [0] * ((1 << 17) + 1) # use power of 2 for O(log n) find_kth_smallest

    def addElement(self, num: int) -> None:
        if len(self.vals) == self.m:
            val = self.vals.popleft()
            self.update(self.bit_vals, val, -val)
            self.update(self.bit_cnt, val, -1)

        self.vals.append(num)
        self.update(self.bit_vals, num, num)
        self.update(self.bit_cnt, num, 1)

    def find_kth_smallest(self, k: int) -> int:
        cnt, pos, n = 0, 0, len(self.bit_cnt)
        for i in reversed(range(trunc(log2(n)) + 1)):
            idx = pos + (1 << i)
            if idx < n and cnt + self.bit_cnt[idx] < k:
                cnt += self.bit_cnt[idx]
                pos = idx
            
        return pos + 1

    def calculateMKAverage(self) -> int:
        if len(self.vals) < self.m:
            return -1
        
        lo = self.find_kth_smallest(self.k)
        hi = self.find_kth_smallest(self.m - self.k)

        _sum = self.query(self.bit_vals, lo, hi)
        _sum += (self.query(self.bit_cnt, 0, lo) - self.k) * lo
        _sum -= (self.query(self.bit_cnt, 0, hi) - (self.m - self.k)) * hi

        return _sum // (self.m - 2 * self.k)
# @lc code=end
