#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def jump(self, i: int) -> int:
        jump = 1

        for di in [-1, 1]:
            for j in range(i + di, i + di + di * self.d, di):
                if not (0 <= j < self.n and self.arr[j] < self.arr[i]):
                    break
                jump = max(jump, 1 + self.jump(j))

        return jump
#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def jump(self, i: int) -> int:
        jump = 0

        for di in [-1, 1]:
            for j in range(i + di, i + di + di * self.d, di):
                if not (0 <= j < self.n and self.arr[j] < self.arr[i]):
                    break
                jump = max(jump, 1 + self.jump(j))

        return jump

    def maxJumps(self, arr: List[int], d: int) -> int:
        self.arr = arr
        self.n = len(arr)
        self.d = d

        return max(map(self.jump, range(self.n)))


# @lc code=end


    def maxJumps(self, arr: List[int], d: int) -> int:
        self.arr = arr
        self.n = len(arr)
        self.d = d

        return max(map(self.jump, range(self.n)))


# @lc code=end
