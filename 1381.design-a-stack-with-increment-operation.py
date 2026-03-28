#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
from collections import deque


class CustomStack:
    def __init__(self, maxSize: int):
        self.nums, self.max_len = deque(), maxSize

    def push(self, x: int) -> None:
        if len(self.nums) == self.max_len:
            return

        self.nums.append([x, 0])

    def pop(self) -> int:
        if not self.nums:
            return -1

        ret = self.nums.pop()
        if self.nums:
            self.nums[-1][1] += ret[1]

        return sum(ret)

    def increment(self, k: int, val: int) -> None:
        if not self.nums:
            return

        self.nums[min(len(self.nums), k) - 1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
