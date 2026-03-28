#
# @lc app=leetcode id=356 lang=python3
#
# [356] Line Reflection
#

# @lc code=start
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        line = min(points)[0] + max(points)[0]
        origin = set(map(tuple, points))
        for point in points:
            reflected = (line - point[0], point[1])
            if reflected not in origin:
                return False

        return True


# @lc code=end
