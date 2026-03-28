#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#

# @lc code=start
from collections import deque


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo = set()
        self.queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        while self.queue and self.queue[0][1] + 10 <= timestamp:
            self.memo.remove(self.queue.popleft()[0])

        if message not in self.memo:
            self.queue.append([message, timestamp])
            self.memo.add(message)
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# @lc code=end

