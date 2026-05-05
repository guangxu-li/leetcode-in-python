#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
from collections import Counter, defaultdict, deque


class FreqStack:

    def __init__(self):
        self.counter, self.stack, self._max = Counter(), defaultdict(deque), 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self._max = max(self.counter[val], self._max)
        self.stack[self.counter[val]].append(val)

    def pop(self) -> int:
        val = self.stack[self._max].pop()
        if not self.stack[self._max]:
            self._max -= 1
        self.counter[val] -= 1

        return val
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

