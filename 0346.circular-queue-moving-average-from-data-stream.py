#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#

# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [0] * size
        self.cnt = 0
        self.sum = 0

    def next(self, val: int) -> float:
        i = self.cnt % self.size
        self.sum -= self.queue[i]

        self.queue[i] = val
        self.cnt += 1
        self.sum += val

        return self.sum / min(self.size, self.cnt);

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end

