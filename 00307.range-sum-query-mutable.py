#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0] * self.n
        self.bit = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        i = index + 1
        while i <= self.n:
            self.bit[i] += diff
            i += i & -i

        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        right += 1
        while right > left:
            sum += self.bit[right]
            right -= right & -right
        while left > right:
            sum -= self.bit[left]
            left -= left & -left

        return sum


obj = NumArray([1, 3, 5])
obj.sumRange(0, 2)
obj.update(1, 2)
obj.sumRange(0, 2)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
