#
# @lc app=leetcode id=1576 lang=python3
#
# [1576] Replace All ?'s to Avoid Consecutive Repeating Characters
#

# @lc code=start
from re import sub


class Solution:
    def modifyString(self, s: str) -> str:
        return (
            self.modifyString(
                sub(
                    r"(^|.)(\?)(.|$)",
                    lambda m: m.group(1)
                    + ({"a", "b", "c"} - {m.group(1), m.group(3)}).pop()
                    + m.group(3),
                    s,
                )
            )
            if "?" in s
            else s
        )


# @lc code=end
