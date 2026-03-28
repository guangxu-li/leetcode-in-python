#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()
        self.t = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.t = x

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            val = self.q.popleft()
            self.q.append(val)
            self.t = val

        return self.q.popleft()

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
