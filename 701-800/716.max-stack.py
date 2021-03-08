#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#

# @lc code=start
from collections import deque


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append((x, max(x, self.dq[-1][1]) if self.dq else x))        

    def pop(self) -> int:
        return self.dq.pop()[0]

    def top(self) -> int:
        return self.dq[-1][0]

    def peekMax(self) -> int:
        return self.dq[-1][1]

    def popMax(self) -> int:
        buffer = []
        max = self.peekMax()
        while self.top() != max:
            buffer.append(self.dq.pop()[0])
        self.pop()
        map(self.push, reversed(buffer))

        return max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# @lc code=end

