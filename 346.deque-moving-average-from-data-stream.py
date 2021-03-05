#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#

# @lc code=start
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.movies = deque() 
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.movies) == self.size:
            self.sum -= self.movies.popleft()
        
        self.movies.append(val)
        self.sum += val
        
        return self.sum / len(self.movies)
         


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end

