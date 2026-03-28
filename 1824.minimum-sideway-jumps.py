#
# @lc app=leetcode id=1825 lang=python3
#
# [1825] Finding MK Average
#

# @lc code=start
from collections import deque
class MKAverage:

    def __init__(self, m: int, k: int):
        self.nums = deque(maxlen=m)
        self.m, self.k = m, k

    def addElement(self, num: int) -> None:
        self.nums.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1
        
        nums = sorted(self.nums[-self.m:])
        
        if len(nums) <= self.k * 2:
            return 0
        
        return sum(nums[self.k:-self.k]) // (self.m - self.k * 2)
# @lc code=end
