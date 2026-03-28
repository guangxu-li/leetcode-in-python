#
# @lc app=leetcode id=1776 lang=python3
#
# [1776] Car Fleet II
#

# @lc code=start
class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        stack, times = [], [-1] * len(cars)
        for i in range(len(cars) - 1, -1, -1):
            p, s = cars[i]
            while stack and (
                s <= cars[stack[-1]][1]
                or (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= times[stack[-1]] > 0
            ):
                stack.pop()

            if stack:
                times[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)

        return times


# @lc code=end
