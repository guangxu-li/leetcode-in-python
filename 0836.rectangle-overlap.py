#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        overlap = lambda a, b: a[0] < b[1] and a[1] > b[0]

        return (
            rec1[0] < rec1[2]
            and rec1[1] < rec1[3]
            and rec2[0] < rec2[2]
            and rec2[1] < rec2[3]
            and overlap((rec1[0], rec1[2]), (rec2[0], rec2[2]))
            and overlap((rec1[1], rec1[3]), (rec2[1], rec2[3]))
        )


# @lc code=end
