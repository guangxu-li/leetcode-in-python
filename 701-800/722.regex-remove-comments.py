#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
from re import sub


class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        return filter(None, sub(r"//.*|/\*(.|\n)*?\*/", "", "\n".join(source)).split('\n'))
# @lc code=end
