#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
from datetime import datetime
from re import sub


class Solution:
    def reformatDate(self, date: str) -> str:
        return datetime.strptime(sub(r"st|nd|rd|th", "", date), "%d %b %Y").strftime("%Y-%m-%d")


# @lc code=end
